import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = self.get_utc_time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None

    def get_utc_time(self):
        format = '%H:%M %d/%m/%Y'
        return datetime.now().strftime(format)

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()
        hash_str = hash_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.root = None

    def add_block(self, data):

        if self.root == None:
            self.root = Block(data, 0)

        else:
            current = self.root

            while current.next:
                current = current.next

            previous_hash = current.hash
            current.next = Block(data, previous_hash)

    def print_blockchain(self):

        if self.root == None:
            print("There is no block!")
            return
        else:
            current = self.root
            index = 0
            print()
            print("----------------")
            print("Blockchain Is Printing..")
            print("----------------")

            while current:
                print("Index:", index)
                print("Timestamp:", current.timestamp)
                print("Data:", current.data)
                print("SHA256 Hash:", current.hash)
                print("Prev_Hash:", current.previous_hash)
                print("--------------->")

                current = current.next
                index += 1

            print("")


bitcoin = Blockchain()

bitcoin.print_blockchain()
bitcoin.add_block("block1 Data")
bitcoin.add_block("block2 Data")
bitcoin.add_block("block3 Data")
bitcoin.add_block("block4 Data")
bitcoin.print_blockchain()
bitcoin.add_block("block5 Data")
bitcoin.add_block("block6 Data")
bitcoin.print_blockchain()