"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Example script to call TExpress on a text string

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '1.0'
__copyright__ = '(c) 2018, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from pprint import pprint
from termite_toolkit import texpress

# specify termite API endpoint
termite_home = "http://localhost:9090/termite"
# specify the pattern you wish to search for- this can created in the TERMite UI
pattern = ":(INDICATION):{0,5}:(GENE)"

t = texpress.TexpressRequestBuilder()

# individually add items to your TERMite request
t.set_url(termite_home)
t.set_text("breast cancer brca1")
t.set_subsume(True)
t.set_input_format("txt")
t.set_output_format("json")
t.set_allow_ambiguous(False)
t.set_pattern(pattern)

# execute the request
texpress_response = t.execute(display_request=True)
pprint(texpress_response)
