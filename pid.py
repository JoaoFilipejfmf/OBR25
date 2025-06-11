from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch
import robo
from robo import LIMIAR_BRANCO, LIMIAR_PRETO

def pid(leitura_dir, leitura_esq, robo):
    erro = leitura_dir - leitura_esq

    robo.integral += erro
    derivada = erro - robo.erro_anterior
    correcao = robo.Kp * erro + robo.Ki * robo.integral + robo.Kd * derivada
    robo.erro_anterior = erro

    velocidade_esq = robo.velocidade_base - correcao
    velocidade_dir = robo.velocidade_base + correcao

    robo.motor_esquerdo.run(velocidade_esq)
    robo.motor_direito.run(velocidade_dir)

def curva_reta(leitura_esq, leitura_dir, robo):
    if leitura_esq < LIMIAR_PRETO and leitura_dir > LIMIAR_BRANCO:
        # Curva fechada para a esquerda
        robo.motor_esquerdo.run(-robo.velocidade_base)
        robo.motor_direito.run(robo.velocidade_base)
        wait(100)  # Ajuste esse valor conforme necessário
        return True
    elif leitura_dir < LIMIAR_PRETO and leitura_esq > LIMIAR_BRANCO:
        # Curva fechada para a direita
        robo.motor_esquerdo.run(robo.velocidade_base)
        robo.motor_direito.run(-robo.velocidade_base)
        wait(100)  # Ajuste esse valor conforme necessário
        return True