from wrapper import MoneroBlocks

monero = MoneroBlocks()

# get current monero stats
current_stats = monero.get_stats()
print(current_stats)


# get most recent block information
current_block_header = monero.get_current_block_header()
current_block_data = monero.get_current_block_data()
print(current_block_header)
print(current_block_data)


# get block data by height
height = '1830280'
header = monero.get_block_header(height)
block = monero.get_block_data(height)
print(block)


# get block data by block hash
block_hash = '2fc8ecbe785fd8eaa27835e66106b74a1db568926d6098a09477697d80520970'
header = monero.get_block_header(block_hash)
block = monero.get_block_data(block_hash)
print(block)


# get transaction data
tx_hash = '2ecbd1c3bacef9dc1cb0ab96c989b4b908208261bb1d6c9f8e5cdbf0b66d077e'
tx_data = monero.get_transaction_data(tx_hash)
print(tx_data)


# check if key image is spent
is_key_image_spent = monero.is_key_image_spent(tx_hash)
print(is_key_image_spent)