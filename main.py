#Fé gera vitória, Deus segura o robô

from pybricks.tools import wait, StopWatch
from pybricks.parameters import Icon, Axis
from pid import pid, curva_reta
from obstaculo import verificar_obstaculo, desviar_obstaculo
from cores import verificar_cores
from init import calibrar
from resgateseguidor import mapear
import robot

robo = robot.Robo()

# Cronômetro
stopwatch = StopWatch()
stopwatch_cal = StopWatch()

NUM_RESGATE = 150
contador_resgate = NUM_RESGATE
pitchs = []

calibrar(robo)
print(robo.resgate)
robo.hub.display.icon(Icon.CIRCLE)
# Loop principal
while True:
    # === Obstáculo ===    
    if(robo.sensor_ultrassonico.distance() < 100):
        verificar_obstaculo(stopwatch=stopwatch, robo=robo)

    # === PID ===
    leitura_dir = robo.sensor_direito.reflection()
    leitura_esq = robo.sensor_esquerdo.reflection()

    pid(leitura_dir, leitura_esq, robo)

    # === Resgate ===
    pitchs.append(robo.hub.imu.tilt()[0])
    if len(pitchs) >= 150:
        pitchs.pop(0)
    if (leitura_dir > robo.resgate and leitura_esq > robo.resgate) or contador_resgate < NUM_RESGATE:
        contador_resgate -= 1
        if max(pitchs) - min(pitchs) > 5:
            contador_resgate = NUM_RESGATE
        if contador_resgate <= 0:
            contador_resgate = NUM_RESGATE
            robo.hub.display.icon(Icon.HEART)
            mapear(robo)
        

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

    # === HSV (a cada 250ms) ===
    if(stopwatch.time() > 250):
        hsv_esq = robo.sensor_esquerdo.hsv()
        hsv_dir = robo.sensor_direito.hsv()
        if hsv_dir[1] >= 30 or hsv_esq[1] >= 30:
            if(verificar_cores(robo) == 1):
                break
        stopwatch.reset()
    
    wait(10)

#Em Nome de Jesus!!!!    