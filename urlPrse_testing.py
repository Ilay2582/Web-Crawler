import urlparser

original = 'http://netloc/path;parameters?query=argument#fragment'
print ('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', parsed.geturl())