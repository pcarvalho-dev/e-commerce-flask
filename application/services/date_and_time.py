import datetime

import pytz


def get_now(t=None):
    timezone = pytz.timezone("America/Sao_Paulo")

    if t == 'year':
        now = datetime.datetime.now(tz=timezone).year

    elif t == 'month':
        now = datetime.datetime.now(tz=timezone).month

    elif t == 'day':
        now = datetime.datetime.now(tz=timezone).day

    elif t == 'today':
        now = datetime.datetime.now(tz=timezone).date()

    else:
        now = datetime.datetime.now(tz=timezone)

    return now
