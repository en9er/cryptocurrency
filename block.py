import datetime
import hashlib


class Block:
    blockN = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('ascii') +
            str(self.data).encode('ascii') +
            str(self.previous_hash).encode('ascii') +
            str(self.timestamp).encode('ascii') +
            str(self.blockN).encode('ascii')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block hash: " + str(self.hash() + "\nBlock number:" + str(self.blockN))




