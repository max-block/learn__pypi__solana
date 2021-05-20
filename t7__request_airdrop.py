import time

from solana.account import Account
from solana.rpc.api import Client
from solana.rpc.commitment import Recent, Root

client = Client("http://localhost:8899")

acc = Account()

res = client.request_airdrop(acc.public_key(), lamports=1 * 10 ** 9, commitment=Root)

time.sleep(1)
print(client.get_balance(acc.public_key(), commitment=Recent))
