import requests as req
import shutil

def getBarCode(playlistID):
    web = "https://scannables.scdn.co/uri/plain/png/000000/white/640/spotify:playlist:"
    web += playlistID
    response = req.get(web, stream=True)
    file = open("./sample_image.png", "wb")
    file.write(response.content)
    file.close()

# pass in the id of the created playlist
getBarCode(playlistID)
