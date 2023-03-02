import requests
import urllib.request
import json

class İnstagramVideoDownloader(object):
    def __init__(self, url:str) -> None:
        self.token = self.readConfig()
        self.url = url
        
        
    def readConfig(self):
        return json.loads(open("config.json", mode="r", encoding="utf-8").read())["key"]
        
    def GetVideoUrl(self):
        url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

        querystring = {"url":str(self.url)}

        headers = {
            "X-RapidAPI-Key": str(self.token),
            "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()["media"]
        return response
    
    def Downloader(self):
        file_name = self.url.split("/")[-2]
        urllib.request.urlretrieve(self.GetVideoUrl(), f'{file_name}.mp4')
        print(f"{file_name} Dosyası başarıyla indi") 

        



