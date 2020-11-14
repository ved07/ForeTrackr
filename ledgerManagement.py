import hashManager

class Block():
    def __init__(self):
        self.ledger = []
        self.block = {}
        self.id =1
    """ format for ledger =
    {  
        type:"Log In", "Log Out" or "Upload",
        user: "xxxxxxx",
        timeUTC: "12:34",
        hash_of_evidence:"xxxxxxxxxx"
        is_hash_identical:"true"/"false",
        previous_hashed_ledger: xxxx
    }
        """
    def add(self,type, username, time,evidence,is_hash_identical):
        id = self.id
        ledge = {"id": id, "type": type, "user": username, "timeUTC": time}
        hashOfEvidence = hashManager.hashFile(evidence)
        ledge["hash_of_evidence"] = hashOfEvidence
        ledge["is_hash_identical"] = str(is_hash_identical)
        if self.id != 1:
            ledge["previous_hashed_ledger"] = hashManager.hashLedger(str(self.ledger[-1]))
        self.ledger.append(ledge)
        self.block[id] = ledge
        self.id = id +1