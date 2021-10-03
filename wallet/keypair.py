import ecdsa
import binascii
import hashlib
import base58


def private_key_to_public_key(s):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(s), curve=ecdsa.SECP256k1)
    vk = binascii.hexlify(sk.verifying_key.to_string()).decode('ascii')
    return vk


def pub_key_to_address(public_key):
    # hash sha 256 of pubkey
    sha256_1 = hashlib.sha256(public_key)

    # hash ripemd of sha of pubkey
    ripemd160 = hashlib.new("ripemd160")
    ripemd160.update(sha256_1.digest())

    # checksum
    hashed_public_key = bytes.fromhex("00") + ripemd160.digest()
    checksum_full = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()

    checksum = checksum_full[:4]
    bin_addr = hashed_public_key + checksum

    # encode address to base58 and print
    result_address = base58.b58encode(bin_addr)
    return result_address.decode('ascii')


class Keypair:
    private_key = None
    private_key_hex = None
    uncompressed_public_key_hex = None
    public_base58_address = None

    def __init__(self, private_key=None):
        if private_key is None:
            self.private_key = ecdsa.SigningKey.generate(ecdsa.SECP256k1)
            self.public_key = self.private_key.verifying_key
            self.private_key_hex = binascii.hexlify(self.private_key.to_string()).decode('ascii')
            self.uncompressed_public_key_hex = private_key_to_public_key(self.private_key_hex)
            self.public_base58_address = pub_key_to_address(bytes.fromhex(self.uncompressed_public_key_hex))
        elif type(private_key) == str:
            self.private_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
            self.public_key = self.private_key.verifying_key
            self.private_key_hex = binascii.hexlify(self.private_key.to_string()).decode('ascii')
            self.uncompressed_public_key_hex = private_key_to_public_key(self.private_key_hex)
            self.public_base58_address = pub_key_to_address(bytes.fromhex(self.uncompressed_public_key_hex))
        else:
            raise NotImplementedError(f"Method was not implemented for private_key of type{type(private_key)}")

    def sign_message(self, message):
        if type(message) is not str:
            raise ValueError(f"Required type for sign is str, but received is {type(message)}")
        else:
            message = bytes(message, 'ascii')
            return self.private_key.sign(message)

    @staticmethod
    def verify(sign_owner_public_key, digital_sign, message):
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(sign_owner_public_key), curve=ecdsa.SECP256k1, hashfunc=hashlib.sha1)
        res = False
        mtype = type(message)
        if mtype == str:
            message = bytes(message, 'ascii')
        elif mtype == bytes:
            pass
        else:
            raise ValueError(f"Expected 'bytes' or 'str' type message, but received {mtype}")

        try:
            res = vk.verify(digital_sign, message)
        except ecdsa.keys.BadSignatureError:
            pass
        finally:
            return res

    def generate_vanity_address(self, pattern):
        if pattern[0] != '1':
            print("Pattern must start with 1. Example: 1Stop")
            return
        count = 0
        while True:
            private_key = ecdsa.SigningKey.generate(ecdsa.SECP256k1)
            public_key = private_key.verifying_key
            private_key_hex = binascii.hexlify(private_key.to_string()).decode('ascii')
            uncompressed_public_key_hex = '04' + private_key_to_public_key(private_key_hex)
            public_base58_address = pub_key_to_address(bytes.fromhex(uncompressed_public_key_hex))
            if pattern in public_base58_address[0:len(pattern)]:
                print(public_base58_address)
                print("Match found")
                self.private_key = private_key
                self.public_key = public_key
                self.private_key_hex = private_key_hex
                self.uncompressed_public_key_hex = uncompressed_public_key_hex
                self.public_base58_address = public_base58_address
                return
            count += 1
            if count % 1000 == 0:
                print(count)

