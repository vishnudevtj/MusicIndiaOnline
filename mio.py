# Made by :  Nemesis
# Discription :This downloads The songs from site named mio.to
# syantax : python3 mio.py <link>
# Requirements : python modules bs4,taglib
# System Package : eyed3 [User for insterting artwork]

import bs4,requests,sys,re,taglib,subprocess,os

#Downloads the webpage and create a Beautifull Soup Object
url=sys.argv[1]
# url = "http://mio.to/album/Aashiqui+2+%282013%29"
mio = requests.get(url)
mio_soup = bs4.BeautifulSoup(mio.text,'html.parser')

#Extracts some informations :

movie_name = re.search(r".*?\([0-9]+\)",mio_soup.select('div.heading')[0].text).group(0)
art_work = mio_soup.select('div.group.info > img["src"]')[0]["src"]
year = re.search(r'\(([0-9][0-9]+)\)',movie_name).group(1)
link = re.search(r'http://media-images.mio.to/(.*?)/(.*)/Art-350.jpg',art_work).group(1)
artwork_path = movie_name+"/artwork.jpg"

print("\nMovie Name : "+movie_name )
# print("Music Director : "+music_director)

subprocess.call(["mkdir" ,"-p",movie_name])

#Downloading the artwork
if not os.path.exists(artwork_path):
    subprocess.call(["wget","-c",art_work,"-O",artwork_path])

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
    print("Downloading ",track_name,"  ...")
    # if not os.path.exists(path):
    subprocess.call(["wget","-c",mp3_link,"-O",path])
    # Inserting the tag details
    command = ["eyeD3","--add-image",artwork_path+":FRONT_COVER",path,"-a",artist,"-A",album_name,"-t",track_name,"-n",track_number,"-Y",year]
    subprocess.call(command)
