from pybricks.pupdevices import UltrasonicSensor, Motor
from pybricks.hubs import PrimeHub
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from robot import Robo
from pid import girar_angulo

class ArenaResgate():
    num_linhas = 0
    num_colunas = 0

def mapear(robo: Robo):
    distancia = robo.distancia_ultrassonico_centro()
    print(distancia)
    num_colunas = round(distancia / 300) if distancia < 1200 else 0
    print(num_colunas)
    # se 0, seguir
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    if num_colunas != 0:
        while(robo.distancia_ultrassonico_centro() > num_colunas * 300 - 145):
            wait(10)
        robo.motor_direito.stop()
        robo.motor_esquerdo.stop()
    girar_angulo(robo, 90)
    distancia = robo.distancia_ultrassonico_centro()
    print(distancia)
    ladrilhos_a_direita = round((distancia - 145) / 300) if distancia < 1200 else 0
    girar_angulo(robo, -180)
    # se 0, seguir
    distancia = robo.distancia_ultrassonico_centro()
    print(distancia)
    ladrilhos_a_esquerda = round((distancia - 145) / 300) if distancia < 1200 else 0
    # se 0, seguir
    num_linhas = ladrilhos_a_direita + ladrilhos_a_esquerda + 1
    print(f'Linhas: {num_linhas}')
    print(f'ladrilhos a direita: {ladrilhos_a_direita}')
    print(f'ladrilhos a esquerda: {ladrilhos_a_esquerda}')