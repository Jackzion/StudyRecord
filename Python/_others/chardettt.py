import chardet
print(chardet.detect('草泥马'.encode('utf-8')))
print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))
