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

def mapear_z_esquerda(robo: Robo):
    robo.motor_direito.run(200)
    robo.motor_esquerdo.run(200)
    while(robo.distancia_ultrassonico_centro() > 400):
        wait(10)
    girar_angulo(robo, -90)
    robo.motor_direito.run(-140)
    robo.motor_esquerdo.run(-140)
    wait(2000)
    robo.direcao.straight(600)
    robo.motor_direito.run(140)
    robo.motor_esquerdo.run(140)
    wait(2000)
    robo.direcao.drive(-20, 0)
    while(robo.distancia_ultrassonico_centro() < 140):
        wait(10)
    robo.direcao.stop()
    girar_angulo(robo, 90)
    robo.direcao.straight(300 + 145)
    girar_angulo(robo, 20)
    robo.motor_direito.run(80)
    robo.motor_esquerdo.run(-80)
    while(robo.sensor_esquerdo.reflection() > robo.limiar_preto and robo.sensor_direito.reflection() > robo.limiar_preto):
        wait(10)
    wait(1000)

def mapear_z_direita(robo: Robo):
    robo.motor_direito.run(200)
    robo.motor_esquerdo.run(200)
    while(robo.distancia_ultrassonico_centro() > 400):
        wait(10)
    girar_angulo(robo, 90)
    robo.motor_direito.run(-140)
    robo.motor_esquerdo.run(-140)
    wait(2000)
    robo.direcao.straight(600)
    robo.motor_direito.run(140)
    robo.motor_esquerdo.run(140)
    wait(2000)
    robo.direcao.drive(-20, 0)
    while(robo.distancia_ultrassonico_centro() < 140):
        wait(10)
    robo.direcao.stop()
    girar_angulo(robo, -90)
    robo.direcao.straight(300 + 145)
    girar_angulo(robo, 20)
    robo.motor_direito.run(80)
    robo.motor_esquerdo.run(-80)
    while(robo.sensor_esquerdo.reflection() > robo.limiar_preto and robo.sensor_direito.reflection() > robo.limiar_preto):
        wait(10)
    wait(1000)

def mapear_l_esquerda(robo: Robo):
    robo.motor_direito.run(200)
    robo.motor_esquerdo.run(200)
    while(robo.distancia_ultrassonico_centro() > 400):
        wait(10)
    girar_angulo(robo, -90)
    robo.motor_direito.run(-140)
    robo.motor_esquerdo.run(-140)
    wait(2000)
    robo.direcao.straight(600)
    robo.motor_direito.run(140)
    robo.motor_esquerdo.run(140)
    wait(2000)
    robo.direcao.drive(-20, 0)
    while(robo.distancia_ultrassonico_centro() < 140):
        wait(10)
    robo.direcao.stop()
    girar_angulo(robo, 90)
    robo.direcao.straight(300 + 80)
    robo.direcao.drive(-20, 0)
    while(robo.distancia_ultrassonico_centro() < 140):
        wait(10)
    girar_angulo(robo, -90)
    robo.direcao.straight(140)
    girar_angulo(robo, 20)
    robo.motor_direito.run(80)
    robo.motor_esquerdo.run(-80)
    while(robo.sensor_esquerdo.reflection() > robo.limiar_preto and robo.sensor_direito.reflection() > robo.limiar_preto):
        wait(10)
    wait(1000)

def mapear_l_direita(robo: Robo):
    robo.motor_direito.run(200)
    robo.motor_esquerdo.run(200)
    while(robo.distancia_ultrassonico_centro() > 400):
        wait(10)
    girar_angulo(robo, 90)
    robo.motor_direito.run(-140)
    robo.motor_esquerdo.run(-140)
    wait(2000)
    robo.direcao.straight(600)
    robo.motor_direito.run(140)
    robo.motor_esquerdo.run(140)
    wait(2000)
    robo.direcao.drive(-20, 0)
    while(robo.distancia_ultrassonico_centro() < 140):
        wait(10)
    robo.direcao.stop()
    girar_angulo(robo, -90)
    robo.direcao.straight(300 + 80)
    robo.direcao.drive(-20, 0)
    while(robo.distancia_ultrassonico_centro() < 140):
        wait(10)
    girar_angulo(robo, 90)
    robo.direcao.straight(140)
    girar_angulo(robo, 20)
    robo.motor_direito.run(80)
    robo.motor_esquerdo.run(-80)
    while(robo.sensor_esquerdo.reflection() > robo.limiar_preto and robo.sensor_direito.reflection() > robo.limiar_preto):
        wait(10)
    wait(800)

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
