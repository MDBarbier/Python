import urllib.request

#url = 'https://store.steampowered.com/app/728880/Overcooked_2/'
url = 'https://store.steampowered.com/search/?term=overcooked+2'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
print(text)