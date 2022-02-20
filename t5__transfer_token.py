import os

from dotenv import load_dotenv
from solana.publickey import PublicKey
from solana.rpc.api import Client
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID

import commons

load_dotenv()

FROM_WALLET_ADDRESS = os.getenv("ADDRESS_0")
TO_WALLET_ADDRESS = os.getenv("ADDRESS_1")
PRIVATE_KEY_0 = os.getenv("PRIVATE_KEY_0")
ENDPOINT = os.getenv("ENDPOINT")
TOKEN = os.getenv("TOKEN")

acc = commons.get_keypair(PRIVATE_KEY_0)

token_client = Token(Client(ENDPOINT), PublicKey(TOKEN), program_id=TOKEN_PROGRAM_ID, payer=acc)


# get from_token_account
res = token_client.get_accounts(PublicKey(FROM_WALLET_ADDRESS))
token_accounts = res["result"]["value"]
if len(token_accounts) > 1:
    print("there are more than one token_account!")
    exit(1)
from_token_account = PublicKey(token_accounts[0]["pubkey"])
print("from_token_account", from_token_account)


# get to_token_account
res = token_client.get_accounts(PublicKey(TO_WALLET_ADDRESS))
token_accounts = res["result"]["value"]
if len(token_accounts) > 1:
    print("there are more than one token_account!")
    exit(1)
elif len(token_accounts) == 1:
    to_token_account = PublicKey(token_accounts[0]["pubkey"])
else:  # create a new to_token_account
    to_token_account = token_client.create_account(owner=PublicKey(TO_WALLET_ADDRESS))


res = token_client.transfer(source=from_token_account, dest=to_token_account, owner=acc, amount=100000)
print(res)
