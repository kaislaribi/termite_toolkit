"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Example script to call TExpress and extract entities from the hits

"""

__author__ = 'SciBite DataScience'
__version__ = '2.0'
__copyright__ = '(c) 2019, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from pprint import pprint
from termite_toolkit import texpress

termite_home = "http://localhost:9090/termite"
input_file = "medline_sample.zip"
options = {"format": "medline.xml", "output": "json", "pattern": ":(INDICATION):{0,5}:(GENE)",
           "opts"  : "reverse=false"}

termite_json_response = texpress.annotate_files(termite_home, input_file, options)
entity_hits = texpress.get_entity_hits_from_json(termite_json_response, score_cutoff=2)

pprint(entity_hits)
