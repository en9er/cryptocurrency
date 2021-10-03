import bip39
import random
import binascii


class Mnemonic:

    @staticmethod
    def generate_mnemonic_words():
        mnemonic_words = []
        mnemonic_phrase = ""
        entropy = ""
        for i in range(128):
            entropy += str(random.randint(0, 1))
        entropy = [entropy[d:d + int(len(entropy) / 16)] for d in range(0, len(entropy), int(len(entropy) / 16))]
        hex_entropy = []
        for word in entropy:
            hex_entropy.append(int(word, 2))
        mnemonic_words = bip39.encode_bytes(bytes(hex_entropy))

        for word in mnemonic_words:
            mnemonic_phrase += word

        return mnemonic_phrase

    @staticmethod
    def mnemonic_passphrase_to_seed(mnemonic_phrase):
        if mnemonic_phrase is None:
            raise Exception("Received mnemonic phrase is None")
        elif type(mnemonic_phrase) != str:
            raise Exception(f"Expected type for mnemonic phrase is 'str', but received {type(mnemonic_phrase)}")

        if bip39.check_phrase(mnemonic_phrase):
            return binascii.hexlify(bip39.phrase_to_seed(mnemonic_phrase)).decode('ascii')
        else:
            raise Exception("Received passphrase is invalid")
