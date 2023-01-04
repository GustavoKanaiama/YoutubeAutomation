from gtts import gTTS
from json import load

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
            print(repr(comentario_resp))

            text = comentario_resp
            tts = gTTS(text=text, lang=language)
            tts.save(f'get_voice_script/voices/voice_c[{i}]_r[{j}].mp3')



