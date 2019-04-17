"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Utility functions- including autocomplete

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '2.0'
__copyright__ = '(c) 2019, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

import requests
from pprint import pprint

class UtilitiesRequestBuilder():
    """
    Class for creating utility requests.
    """

    def __init__(self):
        self.url = ''
        self.basic_auth = ()
        self.verify_request = True

    def set_url(self, url):
        """
        Set the URL of the TERMite instance e.g. for local instance http://localhost:9090/termite/toolkit/autocomplete.api

        :param url: the URL of the TERMite instance to be hit
        :return:
        """
        self.url = url

    def set_basic_auth(self, username, password, verification=True):
        """
        Pass basic authentication credentials.
        ** ONLY change verification if you are calling a known source **

        :param username: username to be used for basic authentication
        :param password: password to be used for basic authentication
        :return:
        """
        self.basic_auth = (username, password)
        self.verify_request = verification

    def call_autocomplete(self, input, vocab, taxon=''):
        """


        :param input:
        :param vocab:
        :param taxon:
        :return:
        """

        if len(input) < 3:
            return 'Please provide a string longer than 3 chars..'

        response = requests.post(self.url, data={"term": input, "e": vocab, "limit": taxon})

        if response.ok:
            ac_json = response.json()
            return ac_json

        else:
            return response.status_code
