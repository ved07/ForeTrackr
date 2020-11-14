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
    def addToChain(self):
        self.chain.addBlock(self.block.block, date.today())
        self.block = Block()
    def onAccess(self,type=None,user=None,evidence=None):

        if self.date != date.today():
            self.addToChain()
        isHashIden = hashFile(evidence) == self.evidenceHash
        dateTime = str(datetime.utcnow())
        self.block.add(type=type, time=dateTime,username=user,evidence=evidence, is_hash_identical=isHashIden)
