"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Demo script making calls with text to the TERMite API

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '1.0'
__copyright__ = '(c) 2018, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from termite_toolkit import termite
from pprint import pprint


# specify termite API endpoint
termite_home = "http://localhost:9090/termite"

# specify entities to annotate
entities = "DRUG"

# initialise a request builder
t = termite.TermiteRequestBuilder()
# individually add items to your TERMite request
t.set_url(termite_home)
t.set_fuzzy(True)
t.set_text("citrate macrophage colony sildenafil stimulating factor influenza hedgehog")
t.set_entities(entities)
t.set_subsume(True)
t.set_input_format("txt")
t.set_output_format("doc.jsonx")
t.set_reject_ambiguous(False)
t.set_options({'fragmentSize': 20})

# execute the request
termite_response = t.execute(display_request=True)

pprint(termite_response)
