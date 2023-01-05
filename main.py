from assembly_video.assembly_video import makingVideo
from get_images.get_images import drawImage#, breakline_text
from get_script_reddit.simplePrawComments import get_redditComments #insert cred
from get_voice_script.get_voice_pt_script import get_voices_pt

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

url = 'https://www.reddit.com/r/RelatosDoReddit/comments/zynl95/fale_um_poder_in%C3%BAtil_e_a_outra_pessoa_vai_deixar/'
num_comment = 5

get_redditComments(cred, url, num_comment, 'top')

## Getting voices
with open('comments_script.json', 'r') as jsonfile:
    json_object = load(jsonfile) 

get_voices_pt(json_object)

## Get images
drawImage(json_object)

# Make Video
makingVideo(json_object, "assembly_video/wallpaper_test_video.jpg")



