from urllib import request
resp = request.urlopen("https://wikipedia.org")
print(resp.code)
print(resp.length)
print(resp.peek())

data = resp.read()
print(type(data))
print(len(data))

html = data.decode("UTF-8")
print(type(html))
print(html)

print(resp.read())


print("============")
# resp = request.urlopen("http://www.google.com/search?q=HarryPotter")

# https://www.youtube.com/watch?
# v=Lh3TokLzzmw
# t=0s

from urllib import parse

params = {"v": "Lh3TokLzzmw", "t": "0s"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://www.youtube.com/watch?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)

html = resp.read().decode("UTF-8")
print(html[:500])