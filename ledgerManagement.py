import hashManager
import json
import os
class Block():
    def __init__(self):
        self.ledger = []
        self.id =1
    """ format for ledger =
    {  
        type:"Log In", "Log Out" or "Upload",
        user: "xxxxxxx",
        timeUTC: "12:34",
        hash_of_evidence:"xxxxxxxxxx"
    }
        """
    def add(self,type, username, time,evidence):
        id = self.id
        ledge = {"id": id, "type": type, "user": username, "timeUTC": time}
        hashOfEvidence = hashManager.hashFile(evidence)
        ledge["hash_of_evidence"] = hashOfEvidence
        if self.id != 1:
            ledge["previous_hash"] = hashManager.hashLedger(str(self.ledger[-1]))

        self.ledger.append(ledge)
        self.id = id +1
        print(self.ledger)