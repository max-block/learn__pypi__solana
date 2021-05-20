import os

from dotenv import load_dotenv
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction

import commons

load_dotenv()

from_address = os.getenv("ADDRESS_0")
private_key = os.getenv("PRIVATE_KEY_0")
to_address = os.getenv("ADDRESS_1")
endpoint = os.getenv("ENDPOINT")

client = Client(endpoint)

acc = commons.get_account(private_key)

lamports = int(0.001 * 10 ** 9)
tx = Transaction(fee_payer=acc.public_key())
tx.add(transfer(TransferParams(from_pubkey=PublicKey(from_address), to_pubkey=PublicKey(to_address), lamports=lamports)))
res = client.send_transaction(tx, acc)
print(res)
