import math
import numpy as np
import soundfile as sf
import soundcard as sc

nPower = 0.001 # quantidade de ruído
temp_Rep = 10 # tempo de reprodução

# lê o arquivo de som e retorna: o som em forma de array (x),
# a taxa de amostragem (Fs)
x, Fs = sf.read("sorri_sou_rei.wav")

# recorta um trecho de audio de acordo com o tempo de reprodução
x = x[0:temp_Rep*Fs, 0]

# criação do ruído
n = math.sqrt(nPower)*np.random.randn(temp_Rep*Fs)

xCorrupt = x + n # adição do ruído ao áudio original

speaker = sc.default_speaker() # obtem o alto-falante padrão do sistema
speaker.play(x,Fs) # reproduz o audio original
speaker.play(xCorrupt,Fs) # reproduz o audio com ruído

# calcula a media dos elementos da matriz ao quadrado = potência do sinal
Ps = np.mean(x**2)
# calcula a variancia dos elementos da matriz = potência do ruído
Pn = np.var(n)
RSR = Ps/Pn # cálculo da relação sinal ruído

print("Relação Sinal Ruído: ", RSR)
