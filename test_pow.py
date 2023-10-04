import hashlib
import json
from os import urandom

def read_file(file):
    with open(file, 'r') as f:
        return json.load(f)

def mine_block(data_json):
    while True:
        nonce = urandom(16).hex()
        data_json['nonce'] = nonce
        cipher = hashlib.new('sha3_256')
        cipher.update(json.dumps(data_json).encode())
        hash_block = cipher.hexdigest()

        # check hash start with 4 zero trailing bit
        j = 4
        if hash_block[:j] == "0"*j:
            return hash_block

class Blockchain_Template:
    def __init__(self):
        self.JSON_TEMPLATE = {
          "previous_hash": "0",
          "time_stamp" : "00-00-0000",
          "nonce" : "",
          "transaction" : {
            "nama":"mr white",
            "nim" : "14123123",
            "perihal" : "perihal apa yang dilakukan kucing tersebut ?",
            "issuer": "hamdani arif"
            }
          }
    def get_template(self):
        """return dict"""
        return self.JSON_TEMPLATE



def pass_block():
    pass

if __name__ == "__main__":
    CATATAN_BLOCKCHAIN = []

    # mine genesis_block atau block pertama
    FIRST_BLOCK = Blockchain_Template()
    FIRST_BLOCK.JSON_TEMPLATE['hash'] = mine_block(FIRST_BLOCK.get_template())
    CATATAN_BLOCKCHAIN.append(FIRST_BLOCK.get_template())

    # mine block kedua sampe ke empat
    for i in range(3):
        block = Blockchain_Template()
        block.JSON_TEMPLATE['previous_hash'] = CATATAN_BLOCKCHAIN[i]['hash']
        block_hash = mine_block(block.get_template())
        block.JSON_TEMPLATE['hash'] = block_hash
        CATATAN_BLOCKCHAIN.append(block.get_template()) 
    for block in CATATAN_BLOCKCHAIN:
        print(f'block hash : {block["hash"]} -> previous_hash {block["previous_hash"]}')
