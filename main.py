from wallet.HDwallet import create_wallet, create_wallet_from_mnemonic, print_information

if __name__ == '__main__':
    message = "aue"
    wallet = create_wallet()
    mnemonic = wallet.mnemonic()

    print_information(wallet)
    wallet = create_wallet_from_mnemonic(mnemonic)
    print_information(wallet)
    # key = Keypair()
    # key2 = Keypair()
    # print(key.mnemonic_words)
    # sign = key.sign_message(message)
    # # = key.sign_message(message)
    # key1 = Keypair()
    # print(key1.verify(key.uncompressed_public_key_hex, sign, message))
    # mnemonic = Mnemonic()
    # mnem_words = "peanut silly noodle fluid action beach forum erode vibrant rough warrior direct"
    # print(mnem_words)
    # print(mnemonic.mnemonic_passphrase_to_seed(mnem_words))
