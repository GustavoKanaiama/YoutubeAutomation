import moviepy.editor as mpy
import moviepy.video.fx.all as vfx
from json import load
import os
    

def makingVideo(json_obj):
    videos=[]
    audio_clip = list()

    REPLIES_FLAG = False # Replies_Flag indicates when exist replies inside a comment, so we need iterate those anwsers inside each comment
                         # and indicates to insert comment audio in front of all replies audios(audio_clip).

    NUMBER_REPLIES = 0


    for i in range(len(json_obj)):

        # Arrange all replies in one audio
        for j in range(len(json_obj[i]['respostas'])):
            replie = json_obj[i]['respostas'][j]['comentario_resp']

            if (replie != "") and (replie != " "):
                NUMBER_REPLIES += 1


        for j in range(NUMBER_REPLIES):

            audio_resp = mpy.AudioFileClip(f'get_voice_script/voices/voice_c[{i}]_r[{j}].mp3')
            audio_clip.append(audio_resp)

        
        audio_comment = mpy.AudioFileClip(f'get_voice_script/voices/voice_c[{i}].mp3')

        #if exist replies, insert comment audio in front of them and concatenate all
        if NUMBER_REPLIES != 0:
            
            audio_clip.insert(0, audio_comment)
            audio_clip = mpy.concatenate_audioclips(audio_clip)
        
        else:
            audio_clip = audio_comment



        image_clip = mpy.ImageClip(f'get_images/images/image_test{i}.jpeg',
                         duration=audio_clip.duration)
        image_clip.fps = 30
        image_clip = image_clip.set_audio(audio_clip)
        image_clip = image_clip.set_end(image_clip.duration)

        videos.append(image_clip)

        #Reset variables
        NUMBER_REPLIES = 0
        audio_clip = []

    final_clip = mpy.concatenate(videos)
    

    background_image = (mpy.ImageClip("assembly_video/wallpaper_test_video.jpg", duration=final_clip.duration))

    final_clip = mpy.CompositeVideoClip([background_image, final_clip.set_position("center")])


    # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
    compression = "fast"

    final_clip = final_clip.fadein(0.35, 0)

    final_clip.write_videofile("assembly_video/videos/final2.mp4", threads=4, fps=30,
                               codec="libx264",
                               preset=compression,
                               ffmpeg_params=["-crf","30"])
    

with open('comments_script.json', 'r') as openfile:
    json_object = load(openfile) #json.load()

makingVideo(json_object)



"""
    # save file
    final_clip.write_videofile("final.mp4", threads=4, fps=30,
                               codec=mpy.vcodec,
                               preset=mpy.compression,
                               ffmpeg_params=["-crf",mpy.videoquality])
    

    videos.close()
"""