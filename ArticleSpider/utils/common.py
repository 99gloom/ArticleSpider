# encoding: utf-8
import re

__author__ = 'mtianyan'
__date__ = '2018/1/18 0018 03:52'
import hashlib


def get_md5(url):
    # str就是unicode了.Python3中的str对应2中的Unicode
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

def extract_num(text):
    #从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

if __name__ == "__main__":
    print(get_md5("http://jobbole.com".encode("utf-8")))