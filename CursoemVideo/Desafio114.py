import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O SITE NÃO ESTÁ DISPONÍVEL NO MOMENTO.')
else:
    print('O SITE ESTÁ DISPONÍVEL')
