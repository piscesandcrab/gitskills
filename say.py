#_*_ coding: UTF-8 _*_

#from urllib import request
import urllib.request

if __name__ == "__main__":
    respone = urllib.request.urlopen("https://github.com")
    print(respone.read())