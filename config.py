
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    BROWSERSTACK_USERNAME: str
    BROWSERSTACK_ACCESSKEY: str

settings = Config(_env_file=".env")

print(settings.BROWSERSTACK_USERNAME)
print(settings.BROWSERSTACK_ACCESSKEY)
'''

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BROWSERSTACK_USERNAME: str
    BROWSERSTACK_ACCESSKEY: str

    class Config:
        env_file = ".env"

creds = Settings()
print(creds.BROWSERSTACK_USERNAME)
print(creds.BROWSERSTACK_ACCESSKEY)
'''
