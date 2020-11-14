from ledgerManagement import Block
from blockchain import chainedBlocks
from datetime import date
from datetime import time
from datetime import datetime
from hashManager import hashFile


class CoreManagement:
    def __init__(self,evidence):
        self.date = date.today()
        self.chain = chainedBlocks()
        self.block = Block()
        self.evidenceHash = hashFile(evidence)
    def onAccess(self,type=None,user=None,evidence=None):
        if self.date != date.today():
            self.chain.addBlock(self.block.block, date)
            self.block = Block()
        isHashIden = hashFile(evidence) == self.evidenceHash
        self.block.add(type=type, time=datetime.now().time(),username=user,evidence=evidence, is_hash_identical=isHashIden)
