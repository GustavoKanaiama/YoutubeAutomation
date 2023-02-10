import shutil
import os

shutil.rmtree("get_voice_script/reddit_voices")
os.mkdir("get_voice_script/reddit_voices")

shutil.rmtree("get_images/images")
os.mkdir("get_images/images")

os.remove("assembly_video/videos/final.mp4")