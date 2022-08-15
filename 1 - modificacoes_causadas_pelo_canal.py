import math
import numpy as np
import matplotlib.pyplot as plot 

# cria um sinal de ondas quadradas
sqrWave = np.concatenate([np.ones(10), np.zeros(10), np.ones(10), np.zeros(10), np.ones(10), np.zeros(10)])

corruptWave = [] # define a varável da onda modificada
nP = 0.1 # quantidade de ruído

# menu
corruptType =  input("Escolha uma modificação causada pelo canal:\n\n0) Ruído\n1) Atenuação\n2) Distorção\nOpção: ")

# modificação do sinal de acordo com a opção selecionada
if (corruptType == "0"): # adição de ruído aleatório no sinal
    corruptWave = sqrWave + math.sqrt(nP)*np.random.randn(len(sqrWave))

elif (corruptType == "1"): # atenução do sinal em 0.5
    corruptWave = 0.5 * sqrWave
elif (corruptType == "2"): # distorção do sinal utilizando convolução
    corruptWave = np.convolve(sqrWave.astype(float), 0.4*np.array([0.2, 0.3, 0.5, 0.4, 0.35, 0.31, 0.27]))

plot.plot(sqrWave) # plotaçào do gráfico do sinal original 
plot.plot(corruptWave) # plotação do gráfico do sinal modificado

plot.xlabel('Tempo') # legenda do eixo x
plot.ylabel('Amplitude') # legenda do eixo y
plot.title('Modificações causadas pelo canal') # titulo do gráfico

plot.grid(True, which='both') # exibe as linhas de grade
plot.axhline(y = 0, color = 'k') # exibe linha no eixo x

plot.show() # exibe gráfico
