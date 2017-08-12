# list all New Release From Hindi Malayalam amd Tamil
  import bs4,requests

  url = ["http://mio.to/Malayalam/Movie+Songs", "http://mio.to/Hindi/Movie+Songs","http://mio.to/Tamil/Movie+Songs"]
  for i in url:
      mio = requests.get(i)
      mio_soup = bs4.BeautifulSoup(mio.text,"html.parser")
      for i in mio_soup.find_all('div', {'id' : '#trending-now'}):
          for j in i.select("a"):
               print(j.find("h2").text+"\t http://mio.to" + j["href"])
