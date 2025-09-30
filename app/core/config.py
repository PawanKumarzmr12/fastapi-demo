import os

class Settings:
    PROJECT_NAME: str = "FastAPI Demo"
    VERSION: str = "1.0.0"
    # future me DB url, JWT secret etc. add kar sakte ho
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
