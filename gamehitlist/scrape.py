import urllib.request

#url = 'https://store.steampowered.com/app/728880/Overcooked_2/'
url = 'https://store.steampowered.com/search/?term=overcooked+2'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
print(text)



#As an alternative to screenscraping, you can use https://store.steampowered.com/api/appdetails?appids=320240 to get a JSON object back containing the data about a game

#http://api.steampowered.com/ISteamApps/GetAppList/v0002/ gets a list of all games - if loaded this into a collection could match name against it to get steam app id

#could still use screenscrape to add games from other sources