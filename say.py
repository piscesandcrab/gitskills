# _*_ coding: UTF-8 _*_

from urllib import request
import chardet

if __name__ == "__main__":
    respone = request.urlopen("https://fanyi.baidu.com")
    html = respone.read()
    charset = chardet.detect(html)
    print(charset)