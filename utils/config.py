import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    # app: Parabank
    base_url: str = os.getenv("BASE_URL", "https://parabank.parasoft.com/parabank/index.htm")
    api_base_url: str = os.getenv("API_BASE_URL", "") # Example for future API tests

config = Config()