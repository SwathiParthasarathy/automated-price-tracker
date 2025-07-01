from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path(__file__).parent / ".env"
print("Looking for .env at:", dotenv_path)

load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("FIRECRAWL_API_KEY")
print("API key from .env:", api_key)
