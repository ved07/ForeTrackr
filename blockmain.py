"""   THE LEDGER is stored on a block every day, once the day changes a new block is created and the old block is added to the chain, the format of each ledger is below:
 {type:"Log In", "Log Out" or "Upload",
        user: "xxxxxxx",
        timeUTC: "12:34",
        hash_of_evidence:"xxxxxxxxxx"
        is_hash_identical:"true"/"false",
        previous_hashed_ledger: xxxx}
There are many ledgers in a block, and many blocks in the chain, you should only need the chain stored in coreManagement.chain.chain
 """
import sys
from datetime import datetime
from management import CoreManagement

filename = sys.argv[1]
action = sys.argv[2]
username = sys.argv[3]

print (filename)

manager = CoreManagement(evidence=filename)
"""Example below to make a record:"""

manager.onAccess(type = action, user=username, evidence=filename)


##manager.onAccess(type = "Log In", user="ved", evidence="myfile.txt")
##manager.onAccess(type = "Log In", user="ved", evidence="myfile.txt")
##manager.onAccess(type = "Log In", user="ved", evidence="myfile.txt")
##manager.onAccess(type = "Log In", user="ved", evidence="myfile.txt")
##manager.onAccess(type = "Log In", user="ved", evidence="myfile.txt")
manager.addToChain()

print ("-----------------")

print (manager.chain.chain)

