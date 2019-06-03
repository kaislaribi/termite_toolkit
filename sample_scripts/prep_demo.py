from termite_toolkit import prep
from termite_toolkit import termite

# specify termite API endpoint
termite_home = "http://localhost:9090/termite"

# specify entities to annotate
entities = "GENE,INDICATION,DRUG,HPO"

# initialise a request builder
t = termite.TermiteRequestBuilder()

# individually add items to your TERMite request
t.set_url(termite_home)
t.set_fuzzy(True)
t.set_text("BRCA1 is associated with breast cancer")
t.set_entities(entities)
t.set_subsume(True)
t.set_input_format("txt")
t.set_output_format("doc.jsonx")

# execute the request
termite_response = t.execute(display_request=True)

# markup takes doc.jsonx output and replaces/augments hits found in your processed documents
# full list of options can be found in the docstring
print('\nmarkup docstring: \n%s' % (prep.markup.__doc__))
print('\nmarkup output:')
print(prep.markup(termite_response, vocabs=entities.split(','), wrap=True))

# text_markup is a minimal version of the above which accepts and returns plain text
# you do not need to TERMite the text before sending it to text_markup
print('\ntext_markup output:')
print(prep.text_markup('Albert was the first in his family to be affected by asthma', 
	vocabs=['INDICATION']))

# replacementDict allows you to define what text you want to be used to replace found entities
# ~NAME~, ~TYPE~ and ~ID~ are special terms that get replaced by data from the TERMite results
print('\ntext_markup with replacementDict output:')
print(prep.text_markup('Albert was the first in his family to be affected by asthma', 
	vocabs=['INDICATION'], 
	replacementDict={'INDICATION':'~NAME~ (~ID~)'}))

# label text as to which characters/words refer to which type of entity for use in NER ML tasks
print('\nlabel output (word level first, then character level:')
print(prep.label(termite_response, vocabs=entities.split(',')))
print(prep.label(termite_response, vocabs=entities.split(','), labelLevel='char'))
