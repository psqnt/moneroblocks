"""
moneroblocks.info api wrapper

http://moneroblocks.info/api/
"""

import requests


class MoneroBlocks:
    """
    A wrapper class for the moneroblocks.info api
    """

    def __init__(self):
        self.base_url = 'https://moneroblocks.info/api/'

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
        stats_method = 'get_stats/'
        url = self.base_url + stats_method
        return requests.get(url).json()

    def get_block_header(self, arg):
        """
        Request a given block header by height or hash
        """
        block_header_method = 'get_block_header/'
        url = self.base_url + block_header_method + arg
        return requests.get(url).json()
    
    def get_block_data(self, arg):
        """
        Request a given block data by height or hash
        """
        block_data_method = 'get_block_data/'
        url = self.base_url + block_data_method + arg
        return requests.get(url).json()
    
    def get_current_block_header(self):
        """
        Request the current block header by height
        """
        height = self._get_current_block_height()
        return self.get_block_header(height)
    
    def get_current_block_data(self):
        """
        Request the current block data by height
        """
        height = self._get_current_block_height()
        return self.get_block_data(height)

    def get_transaction_data(self, hash):
        """
        Request a given transaction by hash
        """
        transaction_data_method = 'get_transaction_data/'
        url = self.base_url + transaction_data_method + hash
        return requests.get(url).json()

    def is_key_image_spent(self, key_image):
        """
        Verify the spent state of a given key image
        """
        method = 'is_key_image_spent/'
        url = self.base_url + method + key_image
        return requests.get(url).json()
