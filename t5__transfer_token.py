import os

from dotenv import load_dotenv
from solana.rpc.api import Client
from solana.transaction import Transaction
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import TransferParams, transfer

import commons

load_dotenv()

FROM_WALLET_ACCOUNT = os.getenv("ADDRESS_0")
PRIVATE_KEY = os.getenv("PRIVATE_KEY_0")
TO_WALLET_ACCOUNT = os.getenv("ADDRESS_1")
ENDPOINT = os.getenv("ENDPOINT")
TOKEN = os.getenv("TOKEN")

client = Client(ENDPOINT)

acc = commons.get_account(PRIVATE_KEY)

from_token_pubkey = commons.get_token_account(client, TOKEN, FROM_WALLET_ACCOUNT)

dest_address = commons.get_token_account(client, TOKEN, TO_WALLET_ACCOUNT)

tx = Transaction(fee_payer=acc.public_key(), recent_blockhash=commons.get_recent_blockhash(client))
tx.add(
    transfer(
        TransferParams(
            program_id=TOKEN_PROGRAM_ID,
            source=from_token_pubkey,
            dest=dest_address,
            owner=acc.public_key(),
            amount=23 * 10 ** 9,
        )
    )
)
res = client.send_transaction(tx, acc)
print(res)
