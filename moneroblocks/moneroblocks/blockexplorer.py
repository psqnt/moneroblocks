from . import util


def _get_current_block_height(self):
    """
    Request the most recent block header by height.

    Use to get current block data
    """
    return str(self.get_stats()['height'])


def get_stats(self):
    """
    Request current coin stats

    :return json: response 
    """
    resource = 'get_stats/'
    response = util.call_api(resource)
    return response  # build util class for this


def get_block_header(self, arg):
    """
    Request a given block header by height or hash
    :param str arg: block height or block hash
    :return:
    """
    resource = f'get_block_header/{arg}'
    response = util.call_api(resource)
    return response


def get_block_data(self, arg):
    """
    Request a given block data by height or hash
    :param str arg: block height or block hash
    :return:
    """
    resource = f'get_block_data/{arg}'
    response = util.call_api(resource)
    return response


def get_current_block_header(self):
    """
    Request the current block header by height
    :return: 
    """
    height = self._get_current_block_height()
    return self.get_block_header(height)


def get_current_block_data(self):
    """
    Request the current block data by height
    :return:
    """
    height = self._get_current_block_height()
    return self.get_block_data(height)


def get_transaction_data(self, hash):
    """
    Request a given transaction by hash
    :param str hash: tx hash/id
    :return:
    """
    resource = f'get_transaction_data/{hash}'
    response = util.call_api(resource)
    return response


def is_key_image_spent(self, key_image):
    """
    Verify the spent state of a given key image
    :param str key_image: monero key image hash
    """
    resource = f'is_key_image_spent/{key_image}'
    response = util.call_api(resource)
    return response
