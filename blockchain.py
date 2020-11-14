import json
class chainedBlocks():
    def __init__(self):
        self.chain = {}

    def addBlock(self, block, date):
        self.chain[str(date)] = block
        print(self.chain)
