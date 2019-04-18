"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Demo script making calls with text to the TERMite API

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '2.0'
__copyright__ = '(c) 2019, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from termite_toolkit import termite
import os
from pprint import pprint

parentDir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
small_input_file = "medline_sample.zip"

# initialise a request builder
t = termite.TermiteRequestBuilder()

# build the request
t.set_binary_content(small_input_file)
t.set_input_format("medline.xml")
t.set_output_format("doc.jsonx")

# make request
termite_multidoc_docjsonx = t.execute(display_request=True)
pprint(termite_multidoc_docjsonx)

# do some post-processing
termite_dataframe = termite.payload_dataframe(termite_multidoc_docjsonx, "totnosyns")
print(termite.all_entities(termite_multidoc_docjsonx))

entity_hits_df = termite.entity_hits_dataframe(termite_multidoc_docjsonx)
print(termite.entity_freq(termite_multidoc_docjsonx))

top_hits_df = termite.top_hits(termite_multidoc_docjsonx, entitySubset='GENE,MPATH, SBIO', selection=5,
                               includeDocs=True)
print(top_hits_df)
