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

branco = robo.sensor_direito.hsv()[2]
preto = robo.sensor_esquerdo.hsv()[2]

robo.limiar_branco = branco - (branco - preto) / 5
robo.limiar_preto = preto + (branco - preto) / 5
RESGATE = branco * 1.33

while not robo.hub.imu.ready():
    wait(100)

robo.hub.imu.reset_heading(0)

def calibrar():
    robo.hub.imu.reset_heading(0)
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    wait(3300)
    robo.motor_direito.run(-100)
    robo.motor_esquerdo.run(100)
    while(abs(robo.hub.imu.heading()) < 90):
        pass
    for i in range(50):
        robo.valor_calibragem += robo.sensor_direito.reflection() - robo.sensor_esquerdo.reflection()
    print(robo.valor_calibragem)
    robo.valor_calibragem /= 50.0
    print(robo.valor_calibragem)
    robo.hub.imu.reset_heading(0)
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(-100)
    while(abs(robo.hub.imu.heading()) < 90):
        pass

calibrar()

# Loop principal
while True:
    # Verifica distância do obstáculo
    if(robo.sensor_ultrassonico.distance() < 100):
        verificar_obstaculo(stopwatch=stopwatch, robo=robo)

    # === PID ===
    hsv_esq = robo.sensor_esquerdo.hsv()
    hsv_dir = robo.sensor_direito.hsv()
    leitura_esq = hsv_esq[2]
    leitura_dir = hsv_dir[2]

    if leitura_dir > RESGATE and leitura_esq > RESGATE:
        robo.hub.display.icon(Icon.HEART / 2)
    else:
        robo.hub.display.icon(Icon.CIRCLE / 2)
    # if leitura_esq < robo.limiar_preto and leitura_dir > robo.limiar_branco:
    #     # Curva fechada para a esquerda
    #     robo.motor_esquerdo.run(-robo.velocidade_base)
    #     robo.motor_direito.run(robo.velocidade_base)
    #     wait(10)  # Ajuste esse valor conforme necessário
    #     continue
    # elif leitura_dir < robo.limiar_preto and leitura_esq > robo.limiar_branco:
    #     # Curva fechada para a direita
    #     robo.motor_esquerdo.run(robo.velocidade_base)
    #     robo.motor_direito.run(-robo.velocidade_base)
    #     wait(10)  # Ajuste esse valor conforme necessário
    #     continue
    pid(leitura_dir, leitura_esq, robo)

    # === HSV (a cada 250ms) ===
    if hsv_dir[1] >= 30 or hsv_esq[1] >= 30:
        if(verificar_cores(robo) == 1):
            break
    wait(5)

#Em Nome de Jesus!!!!    