"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Demo script making using the utilities functions

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '2.0'
__copyright__ = '(c) 2019, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from termite_toolkit import utilities
from pprint import pprint

# specify termite ac API endpoint
acapi_home = 'http://localhost:9090/termite/toolkit/autocomplete.api'

# specify vocab to use
vocab = "DRUG"

ac_example = utilities.UtilitiesRequestBuilder()
ac_example.set_url(acapi_home)
ac_response = ac_example.call_autocomplete('sild', vocab)

pprint(ac_response)
