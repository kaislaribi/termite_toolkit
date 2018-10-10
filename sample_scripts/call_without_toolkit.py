"""

Example script for multipart call using requests.

"""""

import requests
import os

testfile = "medline_sample.zip"


def get_termite_xml(zipfile, format='medline.xml', output='xml'):
    """
    Function for sending a multipart request to TERMite.

    :param zipfile:
    :param format:
    :param output:
    :return:
    """

    url = 'http://localhost:9090/termite'
    form_data = {
        'format': format,
        'output': output,
        'subsume': 'true',
        'rejectMinorHits' : 'true',
        'fuzzy' : 'true',
        'opts' : 'fzy.promote=true'
    }

    file_obj = open(zipfile, 'rb')
    file_name = os.path.basename(zipfile)
    binary_content = {"binary": (file_name, file_obj)}
    response = requests.post(url, data=form_data, files=binary_content)

    return response.text


print(get_termite_xml(testfile))
