# moneroblocks
A Python 3 api-wrapper for moneroblocks.info Monero Block Explorer

docs: https://github.com/pasquantonio/moneroblocks/blob/master/docs.md

api reference: https://moneroblocks.info/api

( API reference is out of date, the json responses are slightly different than the ones displayed in api reference)

## Install
```
pip install moneroblocks
```
if not in python3 virtualenv, make sure to specify python3 pip
```
pip3 install moneroblocks
```

## Usage
```python
from moneroblocks import blockexplorer

# get stats
stats = get_stats()

# get block by height
height = '1830280'
block = blockexplorer.get_block(height)

# get transaction
tx_hash = '2ecbd1c3bacef9dc1cb0ab96c989b4b908208261bb1d6c9f8e5cdbf0b66d077e'
tx_data = blockexplorer.get_transaction(tx_hash)
```

## Issues
API reference on monerblocks.info shows a block returns tx hashes but it no longer does this
