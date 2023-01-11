import moviepy.editor as mpy
import moviepy.audio.fx.all as afx
import moviepy.video.fx.all as vfx
from moviepy.audio.fx import volumex
from moviepy.video.fx.resize import resize
from json import load
    

def makingVideo(json_obj, bg_video_path, bg_audio_path):
    videos=[]
    audio_clip = list()
    final_voice_clip = list()

    MARGEM = 25
    OPACITY = 0.85

    # when exist replies inside a comment, so we need iterate those anwsers inside each comment
    # and indicates to insert comment audio in front of all replies audios(audio_clip).

    NUMBER_REPLIES = 0


    #background logic

    background_video = mpy.VideoFileClip(bg_video_path)
    size_background_video = background_video.size 

    width_proportional = int(size_background_video[1]*9/16)-1 #Ratio 9:16
    
    val_inicial=int((size_background_video[0] - width_proportional)/2)

    background_video = background_video.crop(x1=val_inicial, width=width_proportional)

    #insert the title
    
    audio_title = mpy.AudioFileClip(f'get_voice_script/voices/voice_t.mp3')
    title_image_clip = mpy.ImageClip(f'get_images/images/image_test_title.jpeg',
                         duration=audio_title.duration)
    # Start --- crop logic for the title

    title_init_width = title_image_clip.size[0]
    title_final_width = width_proportional - (2*MARGEM)

    title_proportion = title_final_width/title_init_width

    title_image_clip = resize(title_image_clip, title_proportion)
    # Finish --- crop logic title

    title_image_clip = title_image_clip.set_audio(audio_title)
    title_image_clip = title_image_clip.set_opacity(OPACITY)

    videos.append(title_image_clip) #creating video clip with title



    #Comments and Replies logic
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
        image_size = image_clip.size
        image_init_width = image_size[0]
        image_final_width = width_proportional - (2*MARGEM)

        proportion = image_final_width/image_init_width

        image_clip = resize(image_clip, proportion)

        image_clip = image_clip.set_audio(audio_clip)
        image_clip = image_clip.set_opacity(OPACITY)

        videos.append(image_clip)

        #Reset variables
        NUMBER_REPLIES = 0
        audio_clip = []

    final_clip = mpy.concatenate(videos)
    final_clip = afx.volumex(final_clip, factor=0.8)
    
    # guardar a duração do video (das imagens concatenadas)
    final_clip_duration = final_clip.duration

    
    background_audio = mpy.AudioFileClip(bg_audio_path)
    background_audio = afx.audio_fadein(background_audio, 1)
    background_audio = afx.volumex(background_audio, 0.03)

    background_video = background_video.set_duration(final_clip.duration)

    final_clip = mpy.CompositeVideoClip([background_video, final_clip.set_position(("center", 0.2), relative=True)])

    final_audio = mpy.CompositeAudioClip([background_audio, final_clip.audio])#insert audioclips(voices)


    final_clip = final_clip.set_audio(final_audio).set_duration(final_clip_duration)


    # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
    compression = "veryslow"

    final_clip = final_clip.fadein(0.35, 0)
    

    final_clip.write_videofile("assembly_video/videos/final.mp4", threads=4, fps=final_clip.fps,
                               codec="libx264", #libx264
                               preset=compression, bitrate = '4000k')
    

"""
with open('comments_script.json', 'r') as openfile:
    json_object = load(openfile) #json.load()

makingVideo(json_object, "assembly_video/bg_videos/bg_video0.mp4", "assembly_video/bg_audios/bg_audio0.mp3")



    # save file
    final_clip.write_videofile("final.mp4", threads=4, fps=30,
                               codec=mpy.vcodec,
                               preset=mpy.compression,
                               ffmpeg_params=["-crf",mpy.videoquality])
    

    videos.close()
"""