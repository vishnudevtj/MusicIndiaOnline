# Made by :  Nemesis
# Discription :This downloads The songs from site named mio.to
# syantax : python3 -i mio.py
# Requirements : python modules bs4
# System Package : eyed3 [User for insterting artwork]

import bs4
import requests
import sys
import re
import subprocess
import os

movie_list = []

def download_album(s):

    #Downloads the webpage and create a Beautifull Soup Object
    
    # url=sys.argv[1]
    # url = "http://mio.to/album/Aashiqui+2+%282013%29"

    url = str(s)
    mio = requests.get(url)
    mio_soup = bs4.BeautifulSoup(mio.text,'html.parser')

    #Extracts some informations :

    movie_name = re.search(r".*?\([0-9]+\)",mio_soup.select('div.heading')[0].text).group(0)
    art_work = mio_soup.select('div.group.info > img["src"]')[0]["src"]
    year = re.search(r'\(([0-9][0-9]+)\)',movie_name).group(1)
    link = re.search(r'http://media-images.mio.to/(.*?)/(.*)/Art-350.jpg',art_work).group(1)
    artwork_path = movie_name+"/artwork.jpg"

    print("\nMovie Name : "+movie_name )

    subprocess.call(["mkdir" ,"-p",movie_name])

    #Downloading the artwork
    print("Downloading Artwork")
    if not os.path.exists(artwork_path):
        subprocess.call(["wget","-q","--show-progress" ,"-c",art_work,"-O",artwork_path])

    #Finds all the songs links and downloads the and inserts the tags

    for i in mio_soup.find_all("tr" ,{"class" : "song-link"}):
        artist = ",".join(re.findall('"(.*?)"',i['track_artist']))
        album_name = movie_name
        track_number = i["track_number"]
        disk_number = i["disc_number"]
        track_name = i["track_name"]
        path = album_name+"/"+track_name+".mp3"
        #Create the download links of the mp3
        mp3_link = "http://media-audio.mio.to/"+link+"/"+i["album_id"][0]+"/"+i["album_id"]+"/"+disk_number+"_"+track_number+" - "+track_name+"-vbr-V5.mp3"
        print("Downloading ",track_name,"  ...","\n")
        subprocess.call(["wget","-q","--show-progress","-c",mp3_link,"-O",path])
        # Inserting the tag details
        command = ["eyeD3","--add-image",artwork_path+":FRONT_COVER",path,"-a",artist,"-A",album_name,"-t",track_name,"-n",track_number,"-Y",year]
        with open("log",'a') as log_file:
            subprocess.call(command,stdout=log_file,stderr=log_file)

def new():
    url = ["http://mio.to/Malayalam/Movie+Songs", "http://mio.to/Hindi/Movie+Songs","http://mio.to/Tamil/Movie+Songs"]
    global movie_list
    movie_list = []
    for i in url:
        mio = requests.get(i)
        mio_soup = bs4.BeautifulSoup(mio.text,"html.parser")
        for i in mio_soup.find_all('div', {'id' : '#trending-now'}):
            movie_list = movie_list + [ [j.find("h2").text , "http://mio.to"+j["href"]] for j in i.select("a")]
    for i in movie_list:
        print(" {0:20}: {1} ".format(i[0],i[1]))
    # return movie_list
    
            
def search_album(s):
    global movie_list
    movie_list = []
    s = s.replace(' ','+')
    url = "http://mio.to/search/" + s
    mio = requests.get(url)
    mio_soup = bs4.BeautifulSoup(mio.text,"html.parser")
    for i in mio_soup.find_all('div', {'id' : 'albums'}):
        movie_list = [ [ re.search(r'\<span\>(.*)\</span\>',str(j.select('span')[0])).group(1) , "http://mio.to"+j['href'] ] for j in i.select('a')[1:] ]
    for i in movie_list:
        print(" {0:20}: {1} ".format(i[0],i[1]))
    # return movie_list[0:5]

def download():
    global movie_list
    index = 1
    for i in movie_list:
        print(str(index)+ " {0:20}: {1} ".format(i[0],i[1]))
        index = index + 1
    print("Enter the number to Download : ")
    index = int(input())
    download_album(movie_list[index-1][1])
