import os

from dotenv import load_dotenv
from solana.rpc.api import Client

load_dotenv()
ENDPOINT = os.getenv("ENDPOINT")
ADDRESS_0 = os.getenv("ADDRESS_0")

client = Client(ENDPOINT)


lamports = client.get_balance(ADDRESS_0)["result"]["value"]
print(lamports)
