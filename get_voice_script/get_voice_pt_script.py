from gtts import gTTS
from json import load
from pydub import AudioSegment
from get_voice_script.tiktok_voice.get_tiktokVoice import get_tts
import os
    
def get_voices_pt(json_obj, silent_duration=500, voice='br_004', sessionid='e3e8b55bf594956f6193f36e9535d014'):
    
    initial_url = 'api19-normal-useast1a.tiktokv.com'

    """
    api.tiktokv.com
    api16-normal-c-alisg.tiktokv.com
    api19-normal-useast1a.tiktokv.com
    api16-normal-c-alisg.tiktokv.com
    api16-normal-c-useast1a.tiktokv.com
    api16-normal-c-useast2a.tiktokv.com
    api16-normal-v4.tiktokv.com
    api16-normal-v6.tiktokv.com
    api16-va.tiktokv.com
    """



    json_object = json_obj
    
    with open('json_files/comments_script.json', 'r') as openfile:
        json_object = load(openfile) #json.load()
    
    #Get title voice
    title = json_object[0]['titulo']

    #Generate text (buffer)
    with open(f'get_voice_script/buffer_generateText/readtext_title.txt', 'w') as generateText:
           generateText.write(title) #write text in buffer

    #Get comment voices
    get_tts(init_url=initial_url, voice=voice, sessionid=sessionid, readfile=f'get_voice_script/buffer_generateText/readtext_title.txt', filename=f'get_voice_script/reddit_voices/voice_t.wav')

    silence = AudioSegment.silent(duration=silent_duration)
    title_voice = AudioSegment.from_file(f'get_voice_script/reddit_voices/voice_t.wav')
    title_voice = title_voice + silence

    title_voice.export(f'get_voice_script/reddit_voices/voice_t.wav', format="wav")


    for i in range(len(json_object)):

        text = json_object[i]['comentario']

        with open(f'get_voice_script/buffer_generateText/readtext_c[{i}].txt', 'w') as generateText:
           generateText.write(text) #write text in buffer

        #Get comment voices
        get_tts(init_url=initial_url, voice=voice, sessionid=sessionid, readfile=f'get_voice_script/buffer_generateText/readtext_c[{i}].txt', filename=f'get_voice_script/reddit_voices/voice_c[{i}].wav')


        silence = AudioSegment.silent(duration=silent_duration)
        audio = AudioSegment.from_file(f'get_voice_script/reddit_voices/voice_c[{i}].wav')
        result = audio + silence

        
        result.export(f'get_voice_script/reddit_voices/voice_c[{i}].wav', format="wav")

        """ #no working replies
        for j in range(len(json_object[i]['respostas'])):

            comentario_resp = json_object[i]['respostas'][j]['comentario_resp']

            if comentario_resp != " " and comentario_resp != "":

                text = comentario_resp
                tts = gTTS(text=text, lang=language, slow=0.3)
                tts.save(f'get_voice_script/reddit_voices/voice_c[{i}]_r[{j}].wav')

                silence = AudioSegment.silent(duration=2000)
                audio = AudioSegment.from_file(f'get_voice_script/reddit_voices/voice_c[{i}]_r[{j}].wav')
                result = silence + audio

                
                result.export(f'get_voice_script/reddit_voices/voice_c[{i}]_r[{j}].wav', format="wav")
        """

    #insert Fade_in audio in the first comment
    fade_in = AudioSegment.silent(duration=500)
    audio = AudioSegment.from_file(f'get_voice_script/reddit_voices/voice_t.wav')
    result = fade_in + audio
        
    result.export(f'get_voice_script/reddit_voices/voice_t.wav', format="wav")

"""
with open('json_files/comments_script.json', 'r') as openfile:
    json_object = load(openfile) #json.load()

get_voices_pt(json_object)



"""

