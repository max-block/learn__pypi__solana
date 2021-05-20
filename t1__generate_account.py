from solana.account import Account

acc = Account()
public_key = acc.public_key().to_base58().decode("utf-8")
private_key = acc.keypair().decode()
print("public", public_key)
print("private", private_key)
