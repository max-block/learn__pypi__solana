import os
from pprint import pprint

from dotenv import load_dotenv
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts

load_dotenv()
ENDPOINT = os.getenv("ENDPOINT")
ADDRESS_0 = os.getenv("ADDRESS_0")
TOKEN = os.getenv("TOKEN")

client = Client(ENDPOINT)
# res = client.get_token_accounts_by_owner(PublicKey(ADDRESS_0), TokenAccountOpts(mint=PublicKey(TOKEN)))
# pprint(res)
#
#
#
# res = client.get_token_account_balance(PublicKey("Fti7vpEmV6V9okZSdyaqiHeFKPoSMZ1fhXd8qgKzbqan"))
# pprint(res)

pprint(client.get_token_accounts_by_owner(PublicKey(ADDRESS_0), TokenAccountOpts(mint=PublicKey(TOKEN))))
