import requests,bs4,sys
url = sys.argv[1]
while True:
      mio = requests.get(url)
      mio_soup = bs4.BeautifulSoup(mio.text,'html.parser')
      for i in mio_soup.find_all("a" , {"class" : "img-cover-175"}):
            print("http://mio.to"+i["href"])
      try:
          url = "http://mio.to" + mio_soup.find_all("a" , {"class" : "next-page"})[0]["href"]
      except IndexError:
                exit()
