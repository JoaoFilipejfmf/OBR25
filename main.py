#Fé gera vitória, Deus segura o robô

from pybricks.tools import wait, StopWatch
from pybricks.parameters import Icon
from pid import pid, curva_reta
from obstaculo import verificar_obstaculo, desviar_obstaculo
from cores import verificar_cores
import robot

robo = robot.Robo()

# Cronômetro
stopwatch = StopWatch()
stopwatch_cal = StopWatch()

# Variável para controle de tempo
tempo_anterior = 0

branco = robo.sensor_direito.reflection()
preto = robo.sensor_esquerdo.reflection()

robot.limiar_branco = branco - (branco - preto) / 5
robot.limiar_preto = preto + (branco - preto) / 5
RESGATE = branco * 1.2

while not robo.hub.imu.ready():
    wait(100)

robo.hub.imu.reset_heading(0)

# Loop principal
while True:
    # Verifica distância do obstáculo
    if(robo.sensor_ultrassonico.distance() < 100):
        verificar_obstaculo(stopwatch=stopwatch, robo=robo)

    # === PID ===
    leitura_esq = robo.sensor_esquerdo.reflection()
    leitura_dir = robo.sensor_direito.reflection()

    if stopwatch_cal.time() > 2000:
        robot.valor_calibragem = leitura_dir - leitura_esq
        stopwatch_cal.reset()
        stopwatch_cal.pause()

    if leitura_dir > RESGATE and leitura_esq > RESGATE:
        robo.hub.display.icon(Icon.HEART / 2)
    else:
        robo.hub.display.icon(Icon.CIRCLE / 2)
    # Lê os ângulos dos 3 eixos
    # if leitura_esq < robot.limiar_PRETO and leitura_dir > robot.limiar_BRANCO:
    #     # Curva fechada para a esquerda
    #     robo.motor_esquerdo.run(-robo.velocidade_base)
    #     robo.motor_direito.run(robo.velocidade_base)
    #     wait(10)  # Ajuste esse valor conforme necessário
    #     continue
    # elif leitura_dir < robot.limiar_PRETO and leitura_esq > robot.limiar_BRANCO:
    #     # Curva fechada para a direita
    #     robo.motor_esquerdo.run(robo.velocidade_base)
    #     robo.motor_direito.run(-robo.velocidade_base)
    #     wait(10)  # Ajuste esse valor conforme necessário
    #     continue
    pid(leitura_dir, leitura_esq, robo)

    # === HSV (a cada 250ms) ===
    if stopwatch.time() >= 150:
        if(verificar_cores(robo)):
            break
        stopwatch.reset()

    wait(10)






#Em Nome de Jesus!!!!    