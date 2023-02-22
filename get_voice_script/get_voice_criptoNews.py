from json import load
from pydub import AudioSegment
from get_voice_script.tiktok_voice.get_tiktokVoice import get_tts


def get_voices_criptoNews(json_obj, silent_duration=500, voice='br_004'):


    json_object = json_obj
    

    #Get silence
    silence = AudioSegment.silent(duration=silent_duration)

    
    for i in range(len(json_object)):

        text = json_object[i]['title_and_lead']


        with open(f'get_voice_script/buffer_generateText/readtext[{i}].txt', 'w') as generateText:
           generateText.write(text) #write text in buffer

        #Get comment voices
        get_tts(init_url='api16-normal-c-useast1a.tiktokv.com', voice=voice, sessionid='f4d76bf6387273f91dc7b1ae35c7bcec', readfile=f'get_voice_script/buffer_generateText/readtext[{i}].txt', filename=f'get_voice_script/criptoNews_voices/voice_news[{i}].wav')

        
        audio = AudioSegment.from_file(f'get_voice_script/criptoNews_voices/voice_news[{i}].wav')
        result = audio + silence

        
        result.export(f'get_voice_script/criptoNews_voices/voice_news[{i}].wav', format="wav")

        print(f"-- Voice[{i}] Generated --")
        
       
    

    #insert Fade_in audio in the first comment
    fade_in = AudioSegment.silent(duration=500)
    audio = AudioSegment.from_file('get_voice_script/criptoNews_voices/voice_news[0].wav')
    result = fade_in + audio
        
    result.export('get_voice_script/criptoNews_voices/voice_news[0].wav', format="wav")

    print("\n -------- ENDING OF VOICE GENERATION ------\n")


with open('json_files/cripto_news.json', 'r') as openfile:
    json_object = load(openfile) #json.load()


#get_tts(init_url='api16-normal-c-useast1a.tiktokv.com', voice='br_005', sessionid='f4d76bf6387273f91dc7b1ae35c7bcec', readfile='get_voice_script/tiktok_voice/teste.txt', filename=f'teste2.mp3')



get_voices_criptoNews(json_object)


