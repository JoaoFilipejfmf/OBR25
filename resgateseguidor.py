from pybricks.pupdevices import UltrasonicSensor, Motor
from pybricks.hubs import PrimeHub
from pybricks.parameters import Port, Direction, Icon
from pybricks.tools import wait
from robot import Robo
from pid import girar_angulo

ladrilho_atual = [0,0]
sentido_atual = 1

class ArenaResgate():
    num_linhas = 0
    num_colunas = 0

def mapear(robo: Robo) -> int:
    distancia = robo.distancia_ultrassonico_centro()
    print(distancia)
    num_colunas = round(distancia / 300) if distancia < 1200 else -1
    print(num_colunas)
    # if num_colunas == -1:
    #     return -1
    # se 0, seguir
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    if num_colunas != 0:
        while(robo.distancia_ultrassonico_centro() > num_colunas * 300 - 160):
            wait(10)
        robo.motor_direito.stop()
        robo.motor_esquerdo.stop()
    girar_angulo(robo, 90)
    sentido_atual = 0
    distancia = robo.distancia_ultrassonico_centro()
    print(distancia)
    ladrilhos_a_direita = round((distancia - 145) / 300) if distancia < 1200 else -1
    girar_angulo(robo, -180)
    # # se 0, seguir
    # if ladrilhos_a_direita == -1:
    #     return -1
    distancia = robo.distancia_ultrassonico_centro()
    print(distancia)
    ladrilhos_a_esquerda = round((distancia - 145) / 300) if distancia < 1200 else -1
    ladrilho_atual[1] = ladrilhos_a_esquerda
    # # se 0, seguir
    # if ladrilhos_a_esquerda == -1:
    #     return -1
    num_linhas = ladrilhos_a_direita + ladrilhos_a_esquerda + 1 if ladrilhos_a_direita != -1 and ladrilhos_a_esquerda != -1 else 0
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    while(robo.distancia_ultrassonico_centro() > 2 * 300 - 160):
        wait(10)
    robo.motor_direito.stop()
    robo.motor_esquerdo.stop()
    girar_angulo(robo, 90)
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    while(robo.distancia_ultrassonico_centro() > 1 * 300 - 160):
        wait(10)
    robo.motor_direito.stop()
    robo.motor_esquerdo.stop()
    girar_angulo(robo, -90)
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    wait(4000)
    robo.hub.display.icon(Icon.CIRCLE)
    # print(f'Linhas: {num_linhas}')
    # print(f'ladrilhos a direita: {ladrilhos_a_direita}')
    # print(f'ladrilhos a esquerda: {ladrilhos_a_esquerda}')
    # seguir_ladrilhos(robo, 1)

def seguir_ladrilhos(robo: Robo, numero_ladrilhos: int):
    temp = 3 - ladrilho_atual[sentido_atual] - numero_ladrilhos
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    print(temp * 300 - 160)
    if numero_ladrilhos != 0:
        while(robo.distancia_ultrassonico_centro() > temp * 300 - 160):
            wait(10)
    robo.motor_direito.stop()
    robo.motor_esquerdo.stop()
