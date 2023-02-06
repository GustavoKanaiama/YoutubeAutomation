import espeakng

esng = espeakng.Speaker()
#esng.voice = 'portuguese-br'

esng.pitch = 32
esng.speed = 150
print(esng.voice)

esng.say("[[h@l'oU w'3:ld]]")