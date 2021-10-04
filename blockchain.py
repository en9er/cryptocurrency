import hashlib
from block import Block


class Blockchain:
    diff = 20
    max_nonce = 2**32
    target = 2**(256 - diff)

    block = Block("Genesis")
    start = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockN = self.block.blockN + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.max_nonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(str(block) + "\n" + "hashes: " + str(n))
                break
            else:
                block.nonce += 1
            print(n)
