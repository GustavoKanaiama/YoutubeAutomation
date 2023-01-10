from assembly_video.assembly_video import makingVideo
from get_images.get_images import drawImage#, breakline_text
from get_script_reddit.simplePrawComments import get_redditComments #insert cred
from get_voice_script.get_voice_pt_script import get_voices_pt

import shutil

from gtts import gTTS
from pydub import AudioSegment

import praw
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

import moviepy.editor as mpy
import moviepy.video.fx.all as vfx
from json import load
import os


cred = praw.Reddit(
    client_id="PYFGWTGyI46_WGX3R3jYOw",
    client_secret="kmPvW3nrQQH0DTuUDqsGpsoDwUmi4g",
    password="",
    user_agent="u/theuserr",
    username="",
)

## Write json object with reddit comments information

url = 'https://www.reddit.com/r/RelatosDoReddit/comments/106snlw/homem_pode_usar_calcinha/'
num_comment = 6


#Resetting folders (deleting all folders used like 'buffer')
shutil.rmtree("get_voice_script/voices")
os.mkdir("get_voice_script/voices")

shutil.rmtree("get_images/images")
os.mkdir("get_images/images")

#os.remove("assembly_video/videos/final.mp4")
#Ending of reset
number_show_comments = 20
number_selected_comments = 3

get_redditComments(cred, url,number_show_comments, number_selected_comments, 'best')
print("\n------- ENDING OF GET THE COMMENTS -------")
## Getting voices
with open('comments_script.json', 'r') as jsonfile:
    json_object = load(jsonfile) 

get_voices_pt(json_object)

## Get images
drawImage(json_object)

# Make Video
makingVideo(json_object, "assembly_video/bg_videos/bg_video0.mp4", "assembly_video/bg_audios/bg_audio0.mp3")



