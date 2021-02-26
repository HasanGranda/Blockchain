from block import Block
blockchain = []

genesis_block = Block("Chancellor on brink of second bailout for banks", ["Hasan sent 1 Coin to X",
                                                                          "Ahmet sent 5 Coin to Mehmet",
                                                                          "Burak sent 10 Coin to Selçuk"])

second_block = Block(genesis_block.block_hash, ["Esra sent 3 Coin to Hasan",
                                                "Pınar sent 4 Coin to Büşra"])


print("Block hash: Genesis Block\n",genesis_block.block_hash)
print("Block hash: Second Block\n",second_block.block_hash)
