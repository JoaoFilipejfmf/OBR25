from pybricks.tools import wait
from pybricks.parameters import Icon
from pid import girar_angulo
import robot

# 1 = esquerda, -1 = direita
def desviar_obstaculo(direcao, robo: robot.Robo):
    robo.motor_esquerdo.run(-200)
    robo.motor_direito.run(-200)
    wait(750)
    # 1. Parar por um momento
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(500)
    
    # 2. Girar 90° para a esquerda
    girar_angulo(robo, -90)
    wait(200)
    
    # 3. Seguir reto por um tempo (aproximadamente 15cm)
    robo.motor_esquerdo.run(200)
    robo.motor_direito.run(200)
    wait(2800)  # Ajuste este tempo conforme necessário
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(200)
    
    # 4. Girar 90° para a direita
    girar_angulo(robo, 90)
    wait(200)
    
    # 5. Seguir reto por um tempo (aproximadamente 15cm)
    robo.motor_esquerdo.run(200)
    robo.motor_direito.run(200)
    wait(5900)  # Ajuste este tempo conforme necessário
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    wait(200)
    
    # 6. Girar 90° para a direita novamente
    girar_angulo(robo, 90)
    wait(200)
    
    robo.direcao.straight(80)
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

    robo.motor_esquerdo.run(200)
    robo.motor_direito.run(200)
    wait(1000)
    

    girar_angulo(robo, -90)

    robo.motor_esquerdo.run(-150)
    robo.motor_direito.run(-150)
    wait(1000)

# -1 direita, 1 esquerda
def verificar_obstaculo(stopwatch, robo : robot.Robo):
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
            wait(5000)
            robo.hub.display.icon(Icon.TRUE)
            wait(200)
            robo.hub.display.off()
            wait(200)
            robo.hub.display.icon(Icon.TRUE)
            wait(200)
            robo.hub.display.off()
            wait(200)
            robo.hub.display.icon(Icon.TRUE)
            wait(200)
            robo.hub.display.off()
            wait(200)
            robo.hub.display.icon(Icon.CIRCLE)
            desviar_obstaculo(1, robo)
            stopwatch.reset()
            break
        wait(50)
        distancia = robo.sensor_ultrassonico.distance()