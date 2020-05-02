import requests
import os
import json
import threading
import time

destinationFolder = input("destination folder: ")
jsonFile = input("JSON file name: ")

threads = list()

# Laste ned xxx json fil
def downloadFile(url, imgName):
    imageData = requests.get(url)
    with open(destinationFolder + imgName + '.jpg', 'wb') as handler:
      handler.write(imageData.content)
      print("saving image" + imgName)


with open(jsonFile) as json_file:
  data = json.load(json_file)
  for page in data['publication']['pages']:
    url = page['prends'][-1]['url']
    name = page['name']
    thread = threading.Thread(target=downloadFile, args=(url, name))
    threads.append(thread)
    thread.start()
    time.sleep(0.1) # 100 ms intervall mellom hver request
