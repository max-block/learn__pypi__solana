import os
import time

from dotenv import load_dotenv
from solana.account import Account
from solana.rpc.api import Client
from solana.rpc.commitment import Recent, Root

load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")

# client = Client(ENDPOINT)
client = Client("http://localhost:8899")

acc = Account()
print(acc.public_key())

res = client.request_airdrop(acc.public_key(), lamports=1 * 10 ** 9, commitment=Root)
print(res)
res = client.get_confirmed_transaction(res["result"], encoding="json")
print(res)


time.sleep(1)
print(client.get_balance(acc.public_key(), commitment=Recent))
