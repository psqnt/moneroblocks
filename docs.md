# moneroblocks
a python 3 api wrapper for moneroblocks.info

## Import into project
```python
from moneroblocks import blockexplorer
```

## get current monero coin stats
```python
current_stats = blockexplorer.get_stats()
```
`get_stats()` returns a `MoneroStats` object.

`MoneroStats` class contains these fields:
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

## get most recent block header
```python
current_block_header = blockexplorer.get_current_block_header()
```

## get most recent block
```python
current_block_data = blockexplorer.get_current_block()
```

## get block header by height
```python
height = '1830280'
header = blockexplorer.get_block_header(height)
```

## get block by height
```python
height = '1830280'
block = blockexplorer.get_block(height)
```

## get block header by block hash
```python
block_hash = '2fc8ecbe785fd8eaa27835e66106b74a1db568926d6098a09477697d80520970'
header = blockexplorer.get_block_header(block_hash)
```

## get block by hash
```python
block_hash = '2fc8ecbe785fd8eaa27835e66106b74a1db568926d6098a09477697d80520970'
block = blockexplorer.get_block(block_hash)
```

## get transaction data
```python
tx_hash = '2ecbd1c3bacef9dc1cb0ab96c989b4b908208261bb1d6c9f8e5cdbf0b66d077e'
tx_data = blockexplorer.get_transaction(tx_hash)
```

## check if key image is spent
```python
is_key_image_spent = blockexplorer.is_key_image_spent(tx_hash)
```
