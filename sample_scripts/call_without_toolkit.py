"""

  ____       _ ____  _ _         _____ _____ ____  __  __ _ _         _____           _ _    _ _
 / ___|  ___(_) __ )(_) |_ ___  |_   _| ____|  _ \|  \/  (_) |_ ___  |_   _|__   ___ | | | _(_) |_
 \___ \ / __| |  _ \| | __/ _ \   | | |  _| | |_) | |\/| | | __/ _ \   | |/ _ \ / _ \| | |/ / | __|
  ___) | (__| | |_) | | ||  __/   | | | |___|  _ <| |  | | | ||  __/   | | (_) | (_) | |   <| | |_
 |____/ \___|_|____/|_|\__\___|   |_| |_____|_| \_\_|  |_|_|\__\___|   |_|\___/ \___/|_|_|\_\_|\__|


Example script for sending requests to the TERMite API without the toolkit


"""

import requests
import os

__author__ = 'Joe Mullen'
__version__ = '2.0'

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
print(call_termite_file(MEDLINEZIP, format='docstore'))
