from pybricks.tools import wait
from pid import girar_angulo
from pybricks.parameters import Icon
from robot import Robo

def calibrar(robo: Robo):
    robo.hub.display.icon(Icon.SQUARE)
    robo.sensor_direito.lights.off()
    robo.sensor_esquerdo.lights.off()
    while not robo.hub.imu.ready():
        wait(100)

    # Ler os valores de branco e preto na iluminação atual
    branco = robo.sensor_direito.reflection()
    preto = robo.sensor_esquerdo.reflection()

    # Configurar valores para serem considerados branco ou preto 
    variacao = branco - preto
    robo.limiar_branco = branco - variacao / 5
    robo.limiar_preto = preto + variacao / 5

    # Configurar valor para inicializar o resgatee
    robo.resgate = branco * 1.33

    # Às vezes, há uma diferença na leitura de refletância dos sensores, que faz com que o robô curve em segmentos que deveria ir reto
    # Por isso, antes de começar o loop principal, fazemos um movimento para ambos os sensores ficarem sobre a cor branca
    # Após isso, fazemos a leitura do branco em ambos os sensores e calculamos a diferença da leitura entre eles
    # Esse valor será considerado no algoritmo PID

    girar_angulo(robo, 30)

    robo.motor_direito.run(200)
    robo.motor_esquerdo.run(200)
    wait(500)

    # Ao invés de fazer uma leitura simples, fazemos uma média simples de 50 leituras para garantir que seja o erro médio central
    for i in range(50):
        robo.valor_calibragem += robo.sensor_direito.reflection() - robo.sensor_esquerdo.reflection()
        wait(10)
    robo.valor_calibragem /= 50.0

    robo.motor_direito.run(-400)
    robo.motor_esquerdo.run(-400)
    wait(700)

    girar_angulo(robo, -30)