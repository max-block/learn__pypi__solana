import os
import random
from pprint import pprint

from dotenv import load_dotenv
from solana.rpc.api import Client
from solana.rpc.commitment import Finalized

load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")


client = Client(endpoint=ENDPOINT)

res = client.get_slot(commitment=Finalized)
current_slot = res["result"]
print(current_slot)

res = client.get_block(current_slot)
tx = random.choice(res["result"]["transactions"])
pprint(tx)
