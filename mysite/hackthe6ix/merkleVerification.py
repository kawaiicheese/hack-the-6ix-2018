import merkletools
import hashlib

def hashfunc(inp):
    sha256 = getattr(hashlib, "sha256")
    inp=inp.encode('utf-8')
    return sha256(inp).hexdigest()

mt = merkletools.MerkleTools(hash_type="sha256")

def add_User(Username, Password):
    mt.add_leaf(Username,True)
    mt.add_leaf(Password, True)
    mt.make_tree()

def check_User(Username):
    userHash = hashfunc(Username)
    for i in range(mt.get_leaf_count()):
        if mt.validate_proof(mt.get_proof(i), userHash, mt.get_merkle_root()):
            return True
    return False

def check_Pass(Password):
    passHash = hashfunc(Password)
    for i in range(mt.get_leaf_count()):
        if mt.validate_proof(mt.get_proof(i), passHash, mt.get_merkle_root()):
            return True
    return False
