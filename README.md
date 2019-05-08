# moneroblocks_api_wrapper
A Python wrapper class for moneroblocks.info Monero Block Explorer

reference: https://moneroblocks.info/api

( This may be out of date, the json responses I have been getting have been slightly different than the ones displayed )

```python
from wrapper import MoneroBlocks

monero = MoneroBlocks()

# get stats

stats = monero.get_stats()

```

