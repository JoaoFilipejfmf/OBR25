from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch
import robot

def pid(leitura_dir, leitura_esq, robo : robot.Robo):
    pre_erro = leitura_dir - leitura_esq
    erro = pre_erro if abs(pre_erro) > 4 else 0
    
    robo.erros.append(erro)
    if len(robo.erros) >= 40:
        robo.erros.pop(0)
    
    soma_erros = (sum((i + 1)**(7/6) * abs(valor) for i, valor in enumerate(robo.erros)))
    robo.velocidade_base = max(60, 200 - soma_erros / 200)
    print(f'{erro}, {robo.velocidade_base}')

    robo.integral += erro
    derivada = erro - robo.erro_anterior
    correcao = robo.Kp * erro + robo.Ki * robo.integral + robo.Kd * derivada
    robo.erro_anterior = erro

    velocidade_esq = robo.velocidade_base - correcao
    velocidade_dir = robo.velocidade_base + correcao

    robo.motor_esquerdo.run(velocidade_esq)
    robo.motor_direito.run(velocidade_dir)

def curva_reta(leitura_esq, leitura_dir, robo):
    if leitura_esq < robot.limiar_preto and leitura_dir > robot.limiar_branco:
        # Curva fechada para a esquerda
        robo.motor_esquerdo.run(-robo.velocidade_base)
        robo.motor_direito.run(robo.velocidade_base)
        wait(100)  # Ajuste esse valor conforme necessário
        return True
    elif leitura_dir < robot.limiar_preto and leitura_esq > robot.limiar_branco:
        # Curva fechada para a direita
        robo.motor_esquerdo.run(robo.velocidade_base)
        robo.motor_direito.run(-robo.velocidade_base)
        wait(100)  # Ajuste esse valor conforme necessário
        return True
    
def girar_angulo(robo, angulo_desejado):
    """
    Gira o robô no lugar usando o giroscópio e controle proporcional.
    
    Parâmetros:
    - robo: objeto do robô com motores 'motor_esquerdo', 'motor_direito' e 'hub.imu'.
    - angulo_desejado: ângulo a girar em graus (positivo = horário, negativo = anti-horário)
    """

    # Resetar o heading para referência zero
    robo.hub.imu.reset_heading(0)

    # Controle proporcional
    Kp = 2.0
    VELOCIDADE_MAX = 100
    VELOCIDADE_MIN = 50
    TOLERANCIA = .4  # grau de tolerância para parar

    while True:
        erro = angulo_desejado - robo.hub.imu.heading()

        if abs(erro) < TOLERANCIA:
            break

        velocidade = Kp * erro

        # Limitar velocidade
        if velocidade > 0:
            velocidade = max(min(velocidade, VELOCIDADE_MAX), VELOCIDADE_MIN)
        else:
            velocidade = min(max(velocidade, -VELOCIDADE_MAX), -VELOCIDADE_MIN)

        # Aplicar velocidade nos motores (giro no lugar)
        robo.motor_esquerdo.run(velocidade)
        robo.motor_direito.run(-velocidade)

        wait(10)

    # Parar os motores ao final
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()