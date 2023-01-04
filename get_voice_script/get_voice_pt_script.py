from gtts import gTTS
from json import load
from pydub import AudioSegment
    
def get_voices_pt(json_obj):
    
    json_object = json_obj
    
    language = 'pt-br'

    with open('comments_script.json', 'r') as openfile:
        json_object = load(openfile) #json.load()


    for i in range(len(json_object)):

        text = json_object[i]['comentario']

        # Create a gTTS object
        tts = gTTS(text=text, lang=language)

        tts.save(f'get_voice_script/voices/voice_c[{i}].mp3')
        
        for j in range(len(json_object[i]['respostas'])):

            comentario_resp = json_object[i]['respostas'][j]['comentario_resp']

            if comentario_resp != " " and comentario_resp != "":

                text = comentario_resp
                tts = gTTS(text=text, lang=language, slow=0.3)
                tts.save(f'get_voice_script/voices/voice_c[{i}]_r[{j}].mp3')




with open('comments_script.json', 'r') as openfile:
    json_object = load(openfile) #json.load()


audio = AudioSegment.from_file('get_voice_script/voices/voice_c[0].mp3')
fast_audio = audio.speedup(1.15)
fast_audio.export('fast_audio_comment_0.mp3', format='mp3')


#get_voices_pt(json_object)

