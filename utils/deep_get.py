from functools import reduce
from utils.locale import LOCALE


def deep_get(user_lang: str, keys:tuple):
    return reduce(lambda acc, key:acc[key], keys, LOCALE[user_lang])