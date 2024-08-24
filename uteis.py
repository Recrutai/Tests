import os
from dotenv import load_dotenv

load_dotenv()

def get_variable(key):
    return str(os.getenv(key))
