#pip install python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()
token_telegram = os.environ['token']
print(os.environ['token'])