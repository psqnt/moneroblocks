from moneroblocks import blockexplorer


# get current monero stats
current_stats = blockexplorer.get_stats()
print(current_stats)

# get most recent block header
current_block_header = blockexplorer.get_current_block_header()
print(current_block_header)

# get most recent block
current_block_data = blockexplorer.get_current_block()
print(current_block_data)

# get block header by height
height = '1830280'
header = blockexplorer.get_block_header(height)
print(header)

# get block by height
height = '1830280'
block = blockexplorer.get_block(height)
print(block)

# get block header by block hash
block_hash = '2fc8ecbe785fd8eaa27835e66106b74a1db568926d6098a09477697d80520970'
header = blockexplorer.get_block_header(block_hash)
print(header)

# get block by hash
block_hash = '2fc8ecbe785fd8eaa27835e66106b74a1db568926d6098a09477697d80520970'
block = blockexplorer.get_block(block_hash)
print(block)

# get transaction data
tx_hash = '2ecbd1c3bacef9dc1cb0ab96c989b4b908208261bb1d6c9f8e5cdbf0b66d077e'
tx_data = blockexplorer.get_transaction(tx_hash)
print(tx_data)

# check if key image is spent
is_key_image_spent = blockexplorer.is_key_image_spent(tx_hash)
print(is_key_image_spent)
