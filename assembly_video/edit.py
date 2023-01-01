import moviepy.editor as mpy
import moviepy.video.fx.all as vfx

vcodec =   "libx264"

videoquality = "24"

# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "fast"

title = "assembly_video/bg2_video"
loadtitle = title + '.mp4'
savetitle = "final_test" + '.mp4'
#Assuming 12,5 characters per seconds

def edit_video(loadtitle, savetitle):
    # load file
    video = mpy.VideoFileClip(loadtitle)
    audioclip = mpy.AudioFileClip("get_voice_script/voices/voice1.mp3").set_start(1)
    
    video = video.set_audio(audioclip)


    screenshot = (mpy.ImageClip("get_screenshots/images/teste_ultimoclan0.png")
          .set_duration(3)
          .set_start(5)
          #.resize(height=50) # if you need to resize...
          #.margin(right=8, top=8, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

    screenshot = screenshot.fx(vfx.fadein, duration=1) 

    final = mpy.CompositeVideoClip([video, screenshot])

    # save file
    final.write_videofile(savetitle, threads=4, fps=24,
                               codec=vcodec,
                               preset=compression,
                               ffmpeg_params=["-crf",videoquality])
    

    video.close()


if __name__ == '__main__':
    edit_video(loadtitle, savetitle)
