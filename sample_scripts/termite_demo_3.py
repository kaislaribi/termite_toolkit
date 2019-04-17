"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Demo script making calls via the TERMite API and post-processing plus example call to get info around a specific entity

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '2.0'
__copyright__ = '(c) 2019, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from pprint import pprint
from termite_toolkit import termite

# specify termite API endpoint
termite_home = "http://localhost:9090/termite"
input_file = "medline_sample.zip"
options = {"format": "medline.xml", "output": "json", "entities": "HUCELL"}
termite_json_response = termite.annotate_files(termite_home, input_file, options)
entity_hits = termite.get_entity_hits_from_json(termite_json_response, "HUCELL", score_cutoff=2)
pprint(entity_hits)

text_list = [
    "sildenafil is a drug. sildenafil is a drug. sildenafil is a drug. sildenafil is a drug. sildenafil is a drug",
    "macrophage colony stimulating factor"]

options = {"format": "txt", "output": "json", "entities": "DRUG,GENE,HUCELL"}

for i, text in enumerate(text_list):
    termite_json_response = termite.annotate_text(termite_home, text, options)
    entity_hits = termite.get_entity_hits_from_json(termite_json_response, "DRUG,GENE,HUCELL")
    print("row_" + str(i), ":", entity_hits)

print("\n--EXAMPLE call to show retrieval of entity metadata--\n")

pprint(termite.get_entity_details(termite_home, 'NFKB1', 'GENE'))
