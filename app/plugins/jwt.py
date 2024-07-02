import httpx
import jwt

from os import getenv
from dotenv import load_dotenv
from pydantic import BaseModel

from app.common.exceptions import CloudflareUnauthorizedException


class CloudflareJwtDto(BaseModel):
    id: str  # "902700864748273704"
    email: str  # "kms0219kms+1@gmail.com"
    name: str  # "Ayaan"
    preferred_username: str  # "iam.ayaan"

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "902700864748273704",
                    "email": "kms0219kms+1@gmail.com",
                    "name": "Ayaan",
                    "preferred_username": "iam.ayaan",
                }
            ]
        }
    }


class JwtPlugin:
    load_dotenv()
    certs = (httpx.get("https://spacewak.cloudflareaccess.com/cdn-cgi/access/certs")).json()

    def __init__(self):
        pass

    async def get_user(self, token: str) -> CloudflareJwtDto:
        try:
            # kid값이 .env의 CF_ACCESS_AUD 값과 일치하는 cert를 가져옵니다.
            current_certs = next(
                filter(lambda x: x["kid"] == getenv("CF_ACCESS_AUD"), self.certs["public_certs"])
            )

            decodedToken = jwt.decode(token, public_key=current_certs["cert"], algorithms=["HS256"])

            return CloudflareJwtDto(
                id=decodedToken["custom"]["id"],
                email=decodedToken["email"],
                name=decodedToken["custom"]["name"],
                preferred_username=decodedToken["custom"]["preferred_username"],
            )
        except:
            raise CloudflareUnauthorizedException
