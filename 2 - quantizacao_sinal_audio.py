import numpy as np
import matplotlib.pyplot as plot 
import soundfile as sf
import soundcard as sc

b = 1 # numbero de bits
temp_Rep = 20 # define tempo de reprodução

# lê o arquivo de som e retorna: o som em forma de array (x),
# a taxa de amostragem (Fs)
x, Fs = sf.read("sorri_sou_rei.wav");
# recorta um trecho de audio de acordo com o tempo de reprodução
x = x[0:temp_Rep*Fs,0]

delta = (max(x) - min(x))/(2**b - 1)# define o passo de quantização
xq = np.round(x/delta) # realiza a quantização do sinal


speaker = sc.default_speaker() # obtem o alto-falante padrão do sistema
speaker.play(xq,Fs) # reproduz o audio original

# plota gráfico do sinal original das amostras 17000 a 20000
plot.plot(x[17000:20000],'b+') 
# plota gráfico do sinal quantizado das amostras 17000 a 20000
plot.plot(xq[17000:20000],'k') 
# plota gráfico dos dois sinais acima subtraídos 
plot.plot(x[17000:20000] - xq[17000:20000],'r')

plot.xlabel('Tempo') # legenda eixo x
plot.ylabel('Amplitude') # legenda eixo y
plot.title('Quantização do sinal') # título do gráfico

plot.grid(True, which='both') # exibe grid no gráfico
plot.axhline(y = 0, color = 'k') # cria linha do eixo x
plot.show() # exibe o gráfico
