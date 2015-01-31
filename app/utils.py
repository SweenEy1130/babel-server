# app.utils

from datetime import datetime
import time

"""
Convert string date to datetime type
date_str format `11/30/1991 10:20:12`
"""
def escapeDatetime(date_str):
    dt_obj = datetime.strptime(date_str, "%m/%d/%Y %H:%M:%S")
    return dt_obj
