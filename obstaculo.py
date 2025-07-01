from pybricks.tools import wait
import robot

# 1 = esquerda, -1 = direita
def desviar_obstaculo(direcao, robo):
    robo.motor_esquerdo.run(-200)
    robo.motor_direito.run(-200)
    wait(200)
    # 1. Parar por um momento
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(500)
    
    # 2. Girar 90° para a esquerda
    robo.hub.imu.reset_heading(0)
    robo.motor_esquerdo.run(-200 * direcao)
    robo.motor_direito.run(200 * direcao)
    while(abs(robo.hub.imu.heading()) < 90):
        pass
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(200)
    
    # 3. Seguir reto por um tempo (aproximadamente 15cm)
    robo.motor_esquerdo.run(200)
    robo.motor_direito.run(200)
    wait(2400)  # Ajuste este tempo conforme necessário
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(200)
    
    # 4. Girar 90° para a direita
    robo.hub.imu.reset_heading(0)
    robo.motor_esquerdo.run(200 * direcao)
    robo.motor_direito.run(-200 * direcao)
    while(abs(robo.hub.imu.heading()) < 90):
        pass
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(200)
    
    # 5. Seguir reto por um tempo (aproximadamente 15cm)
    robo.motor_esquerdo.run(200)
    robo.motor_direito.run(200)
    wait(4200)  # Ajuste este tempo conforme necessário
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(200)
    
    # 6. Girar 90° para a direita novamente
    robo.hub.imu.reset_heading(0)
    robo.motor_esquerdo.run(200 * direcao)
    robo.motor_direito.run(-200 * direcao)
    while(abs(robo.hub.imu.heading()) < 90):
        pass
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(200)
    
    # 7. Seguir reto até reencontrar a pista
    robo.motor_esquerdo.run(100)
    robo.motor_direito.run(100)
    a = False
    # Verifica se encontrou a linha novamente
    while(not a):
        leitura_dir = robo.sensor_direito.reflection()
        leitura_esq = robo.sensor_esquerdo.reflection()
        print(f'E:{leitura_esq}, D:{leitura_dir}')
        a = leitura_dir < robo.limiar_preto or leitura_esq < robo.limiar_preto
        wait(20)

    robo.motor_esquerdo.run(100)
    robo.motor_direito.run(100)
    wait(1800)
    

    robo.hub.imu.reset_heading(0)
    robo.motor_esquerdo.run(-200 * direcao)
    robo.motor_direito.run(200 * direcao)
    while(abs(robo.hub.imu.heading()) < 90):
        pass

# -1 direita, 1 esquerda
def verificar_obstaculo(stopwatch, robo):
    distancia = robo.sensor_ultrassonico.distance()
    verificadas = 0
    while distancia < 80:
        robo.motor_direito.run(100 * (distancia / 160))
        robo.motor_esquerdo.run(100 * (distancia / 160))
        if distancia < 50:
            verificadas += 1
        if verificadas > 5:
            robo.motor_esquerdo.stop()
            robo.motor_direito.stop()
            wait(500)
            desviar_obstaculo(1, robo)
            stopwatch.reset()
            break
        wait(50)
        distancia = robo.sensor_ultrassonico.distance()