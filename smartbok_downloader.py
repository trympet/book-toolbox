import requests
import os

urlstring = input("JPG URL: ")

pages = input("Pages in book: ")
destinationFolder = input("destination folder: ")
cookies = {
 'CloudFront-Key-Pair-Id': input("Key-Pair-Id: "), 
 'CloudFront-Signature': input("CloudFront-Signature: "),
 'CloudFront-Policy': input("CloudFront-Policy: ")
}

if not os.path.exists(destinationFolder):
  os.makedirs(destinationFolder)
  print("created directory.")  
  
for pageNumber in range(int(pages)):
  paddedNumber = str(pageNumber + 1).rjust(4, '0')
  imageUrl = urlstring + "page" + paddedNumber + '.png'
  imageData = requests.get(imageUrl, cookies=cookies)
  with open(destinationFolder + paddedNumber + '.png', 'wb') as handler:
    handler.write(imageData.content)
    print("saving image" + paddedNumber)
