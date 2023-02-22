from assembly_video.assembly_video import makingVideo
from get_images.get_images import drawImage#, breakline_text
from get_script.simplePrawComments import get_redditComments, get_redditComments_en #insert cred
from get_voice_script.get_voice_pt_script import get_voices_pt
import shutil

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
"""
url = "https://www.reddit.com/r/AskReddit/comments/10g9cjg/whats_something_you_learned_embarrassingly_late/"

#Resetting folders (deleting all folders used like 'buffer')
shutil.rmtree("get_voice_script/reddit_voices")
os.mkdir("get_voice_script/reddit_voices")

shutil.rmtree("get_images/images")
os.mkdir("get_images/images")
#Ending of reset

number_show_comments = 128

number_selected_comments = 4

LANG_EN = True #True -> esta em ingles // False -> esta em portugues

if LANG_EN: get_redditComments_en(cred, url,number_show_comments, number_selected_comments, 'best') 
else: get_redditComments(cred, url,number_show_comments, number_selected_comments, 'best')

print("\n------- ENDING OF GET THE COMMENTS -------")
"""
## Getting voices
with open('json_files/comments_script.json', 'r') as jsonfile:
    json_object = load(jsonfile) 

get_voices_pt(json_object, silent_duration=1000, voice='br_005')

## Get images
drawImage(json_object)


with open('json_files/comments_script.json', 'r') as jsonfile:
    json_object = load(jsonfile) 


bgvideo_inteval = [60, 120]
bgaudio_interval = [52, 115]

# Make Video
makingVideo(json_object, "assembly_video/bg_videos/bg_video2.mp4", bgvideo_interval=bgvideo_inteval)

shutil.rmtree("get_voice_script/buffer_generateText")
os.mkdir("get_voice_script/buffer_generateText")


