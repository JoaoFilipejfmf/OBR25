from pybricks.tools import wait

def calibrar(robo):
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

    robo.hub.imu.reset_heading(0)
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    wait(1000)
    robo.motor_direito.run(-100)
    robo.motor_esquerdo.run(100)
    while(abs(robo.hub.imu.heading()) < 90):
        pass
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(100)
    wait(1000)

    # Ao invés de fazer uma leitura simples, fazemos uma média simples de 50 leituras para garantir que seja o erro médio central
    for i in range(50):
        robo.valor_calibragem += robo.sensor_direito.reflection() - robo.sensor_esquerdo.reflection()
        wait(10)
    print(robo.valor_calibragem)
    robo.valor_calibragem /= 50.0
    print(robo.valor_calibragem)

    robo.motor_direito.run(-100)
    robo.motor_esquerdo.run(-100)
    wait(1500)
    robo.hub.imu.reset_heading(0)
    robo.motor_direito.run(100)
    robo.motor_esquerdo.run(-100)
    while(abs(robo.hub.imu.heading()) < 90):
        pass