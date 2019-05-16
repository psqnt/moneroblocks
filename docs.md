# moneroblocks
a python 3 api wrapper for https://moneroblocks.info

# Usage
## Install package
```
pip install moneroblocks
```

## Import into project
```python
from moneroblocks import blockexplorer
```

# General Statistics
## get current monero coin stats
```python
current_stats = blockexplorer.get_stats()
```
`get_stats()` returns an instance of `MoneroStats` class

`MoneroStats` class fields:
```
+ difficulty
+ height
+ hashrate
+ total_emission
+ last_reward
+ last_timestamp
```
Fields can be accessed like any python class variable
```python
stats = blockexplorer.get_stats()

difficulty = stats.difficulty
height = stats.height
hashrate = stats.hashrate
total_emission = stats.total_emission
last_reward = stats.last_reward
last_timestamp = stats.last_timestamp
```

# Block Header
`BlockHeader` class fields:
```python
+ status
+ depth
+ difficulty
+ hash
+ height
+ major_version
+ minor_version
+ nonce
+ orphan_status
+ prev_hash
+ reward
+ timestamp
```
Fields can be accessed like any python class variable
```python
current_block_header = blockexplorer.get_current_block_header()

status = current_block_header.status
depth = current_block_header.depth
difficulty = current_block_header.difficulty
hash = current_block_header.hash
height = current_block_header.height
major_version = current_block_header.major_version
minor_version = current_block_header.minor_version
nonce = current_block_header.nonce
orphan_status = current_block_header.orphan_status
prev_hash = current_block_header.prev_hash
reward = current_block_header.reward
timestamp = current_block_header.timestamp
```

## get most recent block header
```python
current_block_header = blockexplorer.get_current_block_header()
```
`get_current_block_header` returns an instance of `BlockHeader` class.

The data returned will be from the most recent block on the Monero blockchain

## get block header by height
```python
height = '1830280'
header = blockexplorer.get_block_header(height)
```
`get_block_header` returns an instance of `BlockHeader` class

`height` parameter must be an existing block height in the monero block chain starting at `1`. Visit http://moneroblocks.info to see current highest block height or call the function: `_get_current_block_height()` or `get_stats().height`

## get block header by block hash
```python
block_hash = '2fc8ecbe785fd8eaa27835e66106b74a1db568926d6098a09477697d80520970'
header = blockexplorer.get_block_header(block_hash)
```

# Block
`Block` class fields:
```
+ status
+ id
+ json_rpc
+ block_header: BlockHeader class
```
Fields can be accessed like any python class variable
```python
current_block = blockexplorer.get_current_block()

status = current_block.status
id = current_block.id
json_rpc = current_block.json_rpc
block_header = current_block.block_header
```

## get most recent block
```python
current_block_data = blockexplorer.get_current_block()
```
`get_current_block` returns an instance of `Block` class.

The data returned will be from the most recent block on the Monero blockchain

## get block by height
```python
height = '1830280'
block = blockexplorer.get_block(height)
```
`get_block()` returns an instance of `Block` class

`height` parameter must be an existing block height in the monero block chain starting at `1`. Visit http://moneroblocks.info to see current highest block height or call the function: `_get_current_block_height()` or `get_stats().height`

## get block by hash
```python
block_hash = '2fc8ecbe785fd8eaa27835e66106b74a1db568926d6098a09477697d80520970'
block = blockexplorer.get_block(block_hash)
```

# Transaction
`Transaction` class fields:
```
+ status
+ version
+ unlock_time
+ vin
+ vout
+ extra
+ signatures
+ rctsig_prunable
```
Fields can be accessed like any python class variable
```python
tx = blockexplorer.get_transaction(tx_hash)

status = tx.status
version = tx.version
unlock_time = tx.unlock_time
vin = tx.vin
vout = tx.vout
extra = tx.extra
signatures = tx.signatures
rctsig_prunable = tx.rctsig_prunable
```

## get transaction data
```python
tx_hash = '2ecbd1c3bacef9dc1cb0ab96c989b4b908208261bb1d6c9f8e5cdbf0b66d077e'
tx_data = blockexplorer.get_transaction(tx_hash)
```
`get_transaction` returns an instance of `Transaction` class.

`tx_hash` parameter must be a monero transaction hash as shown in the example

# Key Image
`KeyImage` class fields:
```
+ spent_status
```
Fields can be accessed like any python class variables
```python
key_image = blockexplorer.is_key_image_spent(tx_hash)

spent_status = key_image.spent_status
```
## check if key image is spent
```python
is_key_image_spent = blockexplorer.is_key_image_spent(tx_hash)
```
`is_key_image_spent` returns an instance of `KeyImage` class

`tx_hash` parameter must be a monero transaction hash as shown in the example
