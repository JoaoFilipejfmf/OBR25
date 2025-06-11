#Fé gera vitória, Deus segura o robô

from pybricks.tools import wait, StopWatch
from pid import pid, curva_reta
from obstaculo import verificar_obstaculo, desviar_obstaculo
from cores import verificar_cores
from robo import Robo, LIMIAR_BRANCO, LIMIAR_PRETO

robo = Robo()

# Cronômetro
stopwatch = StopWatch()

# Variável para controle de tempo
tempo_anterior = 0



# Loop principal
while True:
    # Verifica distância do obstáculo
    if(robo.sensor_ultrassonico.distance() < 100):
        verificar_obstaculo(stopwatch=stopwatch, robo=robo)

    # === PID ===
    leitura_esq = robo.sensor_esquerdo.reflection()
    leitura_dir = robo.sensor_direito.reflection()
    if leitura_esq < LIMIAR_PRETO and leitura_dir > LIMIAR_BRANCO:
        # Curva fechada para a esquerda
        robo.motor_esquerdo.run(-robo.velocidade_base)
        robo.motor_direito.run(robo.velocidade_base)
        wait(100)  # Ajuste esse valor conforme necessário
        continue
    elif leitura_dir < LIMIAR_PRETO and leitura_esq > LIMIAR_BRANCO:
        # Curva fechada para a direita
        robo.motor_esquerdo.run(robo.velocidade_base)
        robo.motor_direito.run(-robo.velocidade_base)
        wait(100)  # Ajuste esse valor conforme necessário
        continue
    pid(leitura_dir, leitura_esq, robo)

    # === HSV (a cada 250ms) ===
    if stopwatch.time() >= 150:
        verificar_cores(robo)
        stopwatch.reset()

    wait(10)






#Em Nome de Jesus!!!!    