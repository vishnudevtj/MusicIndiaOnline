import bs4,requests

url = ["http://mio.to/Malayalam/Movie+Songs", "http://mio.to/Hindi/Movie+Songs","http://mio.to/Tamil/Movie+Songs"]
movie_list = []
for i in url:
    mio = requests.get(i)
    mio_soup = bs4.BeautifulSoup(mio.text,"html.parser")
    for i in mio_soup.find_all('div', {'id' : '#trending-now'}):
        movie_list = [ [j.find("h2").text , "http://mio.to"+j["href"]] for j in i.select("a")]

# movie_list = []
# url = "http://mio.to/search/jub+we+met"
# mio = requests.get(url)
# mio_soup = bs4.BeautifulSoup(mio.text,"html.parser")
# for i in mio_soup.find_all('div', {'id' : 'albums'}):
#     movie_list = [ [ re.search(r'\<span\>(.*)\</span\>',str(j.select('span')[0])).group(1) , "http://mio.to"+j['href'] ] for j in i.select('a')[1:] ]
