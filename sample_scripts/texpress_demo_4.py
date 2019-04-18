"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Example script to call TExpress on an input file and process output

NOTE- please ensure, that before running this script, the BioMarker bundle is loaded on the server- 
    this can be done via <server_url>/termite/toolkit/bundler.html

"""

__author__ = 'Joe Mullen & Michael Hughes'
__version__ = '2.0'
__copyright__ = '(c) 2019, SciBite Ltd'
__license__ = 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License'

from termite_toolkit import texpress

input_file = "texpress_sample.txt"
termite_home = "http://localhost:9090/termite"

# initialise a request builder
t = texpress.TexpressRequestBuilder()

# build the request
t.set_url(termite_home)
t.set_binary_content(input_file)
t.set_subsume(False)
t.set_allow_ambiguous(True)
t.set_bundle('BiomarkerFinder')
t.set_reverse(False)

# make request
result = t.execute(display_request=True)

# create dataframe from returned JSON
pandas_df = texpress.texpress_dataframe(result)
print(pandas_df)
