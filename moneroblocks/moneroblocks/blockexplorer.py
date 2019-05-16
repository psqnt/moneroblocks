from . import util


class MoneroStats:
    """
    Coin Stats util class
    """
    def __init__(self, stats):
        self.difficulty = stats['difficulty']
        self.height = stats['height']
        self.hashrate = stats['hashrate']
        self.total_emission = stats['total_emission']
        self.last_reward = stats['last_reward']
        self.last_timestamp = stats['last_timestamp']
    
    def __str__(self):
        stats = f"Difficulty: {self.difficulty}\n" \
                f"Height: {self.height}\n" \
                f"Hashrate: {self.hashrate}\n" \
                f"Total Emission: {self.total_emission}\n" \
                f"Last Reward: {self.last_reward}\n" \
                f"Last Timestamp: {self.last_timestamp}\n"
        return stats


class BlockHeader:
    """
    Monero Block Header Util
    """
    def __init__(self, header):
        self.status = header['status']
        self.depth = header['block_header']['depth']
        self.difficulty = header['block_header']['difficulty']
        self.hash = header['block_header']['hash']
        self.height = header['block_header']['height']
        self.major_version = header['block_header']['major_version']
        self.minor_version = header['block_header']['minor_version']
        self.nonce = header['block_header']['nonce']
        self.orphan_status = header['block_header']['orphan_status']
        self.prev_hash = header['block_header']['prev_hash']
        self.reward = header['block_header']['reward']
        self.timestamp = header['block_header']['timestamp']
    
    def __str__(self):
        header = f'block hash: {self.hash}'
        return header


class Block:
    """
    Monero Block util
    """
    def __init__(self, block):
        self.status = block['status']
        self.id = block['block_data']['id']
        self.json_rpc = block['block_data']['jsonrpc']
        self.block_header = BlockHeader(block['block_data']['result'])
        #self.tx_hashes = block['tx_hashes']  # not returned in json

    def __str__(self):
        block = f'id: {self.id}\nheader:\n {self.block_header}\n'
        return block


class KeyImage:
    """
    Key image utl
    """
    def __init__(self, ki):
        self.spent_status = ki['spent_status']
    
    def __str__(self):
        spent_status = f'Key Image Spent: {self.spent_status}'
        return spent_status


class Transaction:
    """
    Monero Transaction util
    """
    def __init__(self, tx):
        self.status = tx['status']
        self.version = tx['transaction_data']['version']
        self.unlock_time = tx['transaction_data']['unlock_time']
        self.vin = tx['transaction_data']['vin']  # needs class
        self.vout = tx['transaction_data']['vout']  # needs class
        self.extra = tx['transaction_data']['extra'] # needs something
        self.signatures = tx['transaction_data']['rct_signatures'] # needs class
        self.rctsig_prunable = tx['transaction_data']['rctsig_prunable']

    def __str__(self):
        tx = f'version: {self.version}\n' \
             f'unlock time: {self.unlock_time}\n' \
             f'vin: {self.vin}\n' \
             f'vout: {self.vout}\n' \
             f'extra: {self.extra}\n' \
             f'rct_sigs: {self.signatures}\n' \
             f'rctsig_prunable: {self.rctsig_prunable}\n'
        return tx


def _get_current_block_height():
    """
    Request stats and return block height

    Used to get current block data
    :return: height variable in MoneroStats object
    """
    return get_stats().height


def get_stats():
    """
    Request current coin stats

    :return: an instance of :class:`MoneroStats` class 
    """
    resource = 'get_stats/'
    response = util.call_api(resource)
    return MoneroStats(response)


def get_block_header(arg):
    """
    Request a given block header by height or hash
    :param str arg: block height or block hash
    :return: an instance of :class:`BlockHeader` class
    """
    resource = f'get_block_header/{arg}'
    response = util.call_api(resource)
    return BlockHeader(response)


def get_block(arg):
    """
    Request a given block data by height or hash
    :param str arg: block height or block hash
    :return: an instance of :class:`Block` class
    """
    resource = f'get_block_data/{arg}'
    response = util.call_api(resource)
    return Block(response)


def get_current_block_header():
    """
    Request the current block header by height
    :return: an instance of :class:`BlockHeader` class
    """
    height = _get_current_block_height()
    return get_block_header(height)


def get_current_block():
    """
    Request the current block data by height
    :return: an instance of :class:`Block` class
    """
    height = _get_current_block_height()
    return get_block(height)


def get_transaction(hash):
    """
    Request a given transaction by hash
    :param str hash: tx hash/id
    :return: an instance of :class:`Transaction` class
    """
    resource = f'get_transaction_data/{hash}'
    response = util.call_api(resource)
    return Transaction(response)


def is_key_image_spent(key_image):
    """
    Verify the spent state of a given key image
    :param str key_image: monero key image hash
    :return: an instance of :class:`KeyImage` class
    """
    resource = f'is_key_image_spent/{key_image}'
    response = util.call_api(resource)
    return KeyImage(response)
