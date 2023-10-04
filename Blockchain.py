import json

class Block:
    self.block = dict()

    """
    block = {
    "previous block": "test",
    "time_stamp" : "asdasd",
    "transaction" : {
        "nama":"mr white",
        "nim" : "14123123",
        "perihal" : "asdasd"
        "issuer": 
        }
    }
    """
    
    def __init__(self, transac_json):
        self.block = json.load(transac_json)
        pass

    def 

