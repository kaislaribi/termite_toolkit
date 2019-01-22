"""

Example script for sending requests to TERMite without the toolkit.

"""""

import requests
import os

__author__ = 'Joe Mullen'
__version__ = '1.0'

MEDLINEZIP = "medline_sample.zip"
TERMITE_URL = 'http://localhost:9090/termite'
CERTIFICATE_PATH = 'PATH_TO_CERT'  # or False


def call_termite_file(zipfile, format='medline.xml', output='json'):
    """
    Function for sending a multipart request to TERMite.

    :param zipfile: path to zip file
    :param format: input format
    :param output: output format
    :return: response text
    """

    form_data = {
        'format': format,
        'output': output,
        'subsume': 'true',
        'rejectMinorHits': 'true',
        'fuzzy': 'true',
        'opts': 'fragmentSize=20&fzy.promote=true&rejectAmbig=false'
    }

    file_obj = open(zipfile, 'rb')
    file_name = os.path.basename(zipfile)
    binary_content = {"binary": (file_name, file_obj)}
    response = requests.post(TERMITE_URL, data=form_data, files=binary_content, verify=CERTIFICATE_PATH)

    return response.text


def call_termite_txt(text, format='txt', output='json'):
    """
    Function for sending a text request to TERMite.

    :param text: string to be annotated
    :param format: input format
    :param output: output format
    :return: response text
    """

    form_data = {
        'text': text,
        'format': format,
        'output': output,
        'subsume': 'true',
        'rejectMinorHits': 'true',
        'fuzzy': 'true',
        'opts': 'fragmentSize=20&fzy.promote=true&rejectAmbig=false'
    }

    response = requests.post(TERMITE_URL, data=form_data, verify=CERTIFICATE_PATH)

    return response.text


print(call_termite_txt('citrate macrophage colony sildenafil stimulating factor influenza hedgehog'))
print(call_termite_file(MEDLINEZIP))
