import hashlib

class Block:
    def __init__(self, onceki_hash, islem):
        self.islem = islem
        self.onceki_hash = onceki_hash
        string_to_hash = "".join(islem) + onceki_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()