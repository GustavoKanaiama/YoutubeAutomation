# import all the modules that we will need to use

from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = "/home/gukanaiama/.local/lib/python3.10/site-packages/TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/pt/cv/vits")
print()
print(model_item)
print()
voc_path, voc_config_path, _ = model_manager.download_model('vocoder_models/universal/libri-tts/wavegrad') #model_item["default_vocoder"]
print()
print(_)
print()
syn = Synthesizer(
    tts_checkpoint=model_path,# model_path
    tts_config_path=config_path,
    vocoder_checkpoint=voc_path,
    vocoder_config=voc_config_path
)

text = "Hello from a machine, do you want to have a really good sex? with a machine?"
texto = "Fale um poder inútil e a outra pessoa vai deixar mais inutil ainda."
outputs = syn.tts(text)
syn.save_wav(outputs, "audio-1.wav")