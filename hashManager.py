
import hashlib

def hashFile(fileName):
    hasher = hashlib.sha3_256()
    with open(fileName, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)

        return hasher.hexdigest()
def hashLedger(ledger):
    return hashlib.sha3_256(ledger.encode()).hexdigest()