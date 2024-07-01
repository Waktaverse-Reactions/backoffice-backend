import httpx
import jwt

from os import getenv
from dotenv import load_dotenv

from app.common.exceptions import CloudflareUnauthorizedException


class JwtPlugin:
    load_dotenv()
    certs = (httpx.get("https://spacewak.cloudflareaccess.com/cdn-cgi/access/certs")).json()

    def __init__(self):
        pass

    async def get_user(self, token: str) -> dict:
        try:
            # kid값이 .env의 CF_ACCESS_AUD 값과 일치하는 cert를 가져옵니다.
            current_certs = next(
                filter(lambda x: x["kid"] == getenv("CF_ACCESS_AUD"), self.certs["public_certs"])
            )

            return (jwt.decode(token, public_key=current_certs["cert"], algorithms=["HS256"]))[
                "custom"
            ]
        except:
            raise CloudflareUnauthorizedException
