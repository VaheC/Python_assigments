import time
from datetime import datetime as dt
def display_time(sleep_period):
    time.sleep(sleep_period)
    return dt.now().time()
    