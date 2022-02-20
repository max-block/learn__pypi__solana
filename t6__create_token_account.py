import os

from dotenv import load_dotenv
from solana.publickey import PublicKey
from solana.rpc.api import Client
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID

import commons

load_dotenv()

ACCOUNT_0 = os.getenv("ADDRESS_0")
ACCOUNT_1 = os.getenv("ADDRESS_1")
PRIVATE_KEY_0 = os.getenv("PRIVATE_KEY_0")
ENDPOINT = os.getenv("ENDPOINT")
TOKEN = os.getenv("TOKEN")

acc = commons.get_keypair(PRIVATE_KEY_0)

client = Client(ENDPOINT)
token_account = commons.get_token_account(client, TOKEN, ACCOUNT_0)
token_client = Token(client, PublicKey(TOKEN), program_id=TOKEN_PROGRAM_ID, payer=acc)

res = token_client.create_account(owner=PublicKey(ACCOUNT_1))

print(res)
