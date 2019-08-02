import google as google
import youdao as youdao
from exceptions import TranslateException


def get_trans(word):
    try:
        trans = youdao.get_trans(word, False)
    except TranslateException:
        trans = google.get_trans(word)

    return trans
