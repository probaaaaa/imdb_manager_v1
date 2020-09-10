from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Change this to your own IMDb email and password if you don't want to set them to PATH
# Example: EMAIL = 'example@example.com'    PASS = 'password123'
EMAIL = os.getenv('ACC_EMAIL')
PASS = os.getenv('ACC_PASS')
