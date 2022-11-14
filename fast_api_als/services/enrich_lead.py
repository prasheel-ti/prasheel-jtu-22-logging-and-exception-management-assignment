import calendar
import time
import logging
from dateutil import parser
from fast_api_als.database.db_helper import db_helper_session

from fast_api_als import constants

"""
what exceptions can be thrown here?
"""

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def get_enriched_lead_json(adf_json: dict) -> dict:
    type_check = isinstance(dict, adf_json)

    if not type_check:
        raise TypeError("Invalid input type")

    value = dict()
    return value