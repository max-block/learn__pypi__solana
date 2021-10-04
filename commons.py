from typing import Optional

import base58
import pydash
from nacl.public import PrivateKey
from solana.account import Account
from solana.blockhash import Blockhash
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts


def get_account(private_key_base58: str) -> Account:
    return Account(base58.b58decode(private_key_base58)[:32])

def get_keypair(private_key_base58: str) -> Keypair:
    return Keypair(PrivateKey(base58.b58decode(private_key_base58)[:32]))


def get_token_account(client: Client, token_mint: str, wallet_account: str) -> Optional[PublicKey]:
    res = client.get_token_accounts_by_owner(PublicKey(wallet_account), TokenAccountOpts(mint=PublicKey(token_mint)))
    pubkey = pydash.get(res, "result.value.0.pubkey")
    if pubkey:
        return PublicKey(pubkey)


def get_recent_blockhash(client: Client) -> Blockhash:
    res = client.get_recent_blockhash()
    return Blockhash(res["result"]["value"]["blockhash"])
