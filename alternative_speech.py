import requests
import os

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"410f6609143648848426e65c11d6303e"}

payload = "f=48khz_16bit_mono&c=MP3&r=0&hl=pt-br&r=9&v=Dinis&src=para vc ser ruim precisa melhorar muito"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "0c29a9c03bmshd14362915c28807p1e591djsn0aae422a53b2",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

#print(type(response.content))

with open("output.mp3", "wb") as f:
    f.write(response.content)
"""
"""

