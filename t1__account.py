import base58
from nacl.public import PrivateKey
from solana.keypair import Keypair


def generate_new_account():
    keypair = Keypair.generate()
    public_key = keypair.public_key.to_base58().decode("utf-8")
    private_key_arr = [x for x in keypair.secret_key]
    private_base58 = base58.b58encode(keypair.secret_key).decode()
    print("---  generate_new_account  ---")
    print("public", public_key)
    print("private_base58", private_base58)
    print("private_key_arr", private_key_arr)
    print("\n\n")


def get_keypair_by_private_base58(private_key_base58: str):
    print("--  get_keypair_by_private_base58  ---")
    keypair =  Keypair(PrivateKey(base58.b58decode(private_key_base58)[:32]))
    print("public", keypair.public_key.to_base58().decode())
    print("private_key_base58", private_key_base58)
    print("\n\n")





def main():
    generate_new_account()
    get_keypair_by_private_base58("42YyaeDPyoEcm5WiiSidB5VW6EZnQ5f4WwuskB3wF8UncqPxM9zqU1wBEEoPdi8zmLoMNvxE2DdZZu9VggBXo6eA")


if __name__ == "__main__":
    main()