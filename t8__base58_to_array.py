import os

import base58
from dotenv import load_dotenv

load_dotenv()

base58_key = os.getenv("PRIVATE_KEY_0")

arr_key = [x for x in base58.b58decode(base58_key)]
print(arr_key)
