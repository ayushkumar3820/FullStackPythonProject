from typing import List, ClassVar
from pydantic import field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOW_ORIGINS: List[str] = []
    GEMINI_API_KEY: str = ""
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "defaultsecret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @field_validator("ALLOW_ORIGINS", mode="before")
    def parse_allowed_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v or ["*"]

    model_config: ClassVar = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "ignore",
    }

# ✅ ADD THIS LINE - Create an instance that can be imported
settings = Settings()