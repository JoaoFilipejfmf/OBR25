from pybricks.tools import wait
from pybricks.parameters import Icon
import robot
def detectar_verde(h, s, robo):
    return 60 <= h <= 180 and s > 50

def detectar_vermelho(h, s, robo):
    return (0 <= h <= 60 or 300 <= h <= 360) and s > 50

def verificarVerdeFalso(robo, sensor):
    robo.motor_direito.run(80)
    robo.motor_esquerdo.run(80)
    for i in range(200):
        reflet = sensor.reflection()
        s1 = robo.sensor_esquerdo.hsv()[1]
        s2 = robo.sensor_direito.hsv()[1]
        if (s1 < 40 and s2 < 40) and (reflet < robo.limiar_preto):
            return True
        wait(10)
    return False

def verificarVerdeDuploFalso(robo):
    robo.motor_direito.run(80)
    robo.motor_esquerdo.run(80)
    for i in range(200):
        r1 = robo.sensor_esquerdo.reflection()
        r2 = robo.sensor_direito.reflection()
        s1 = robo.sensor_esquerdo.hsv()[1]
        s2 = robo.sensor_direito.hsv()[1]
        if (s1 < 40 and s2 < 40) and (r1 < robo.limiar_preto and r2 < robo.limiar_preto):
            return True
        wait(10)
    return False

def verificar_cores(robo: robot.Robo):
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    for i in range(5):
        if robo.sensor_esquerdo.hsv()[1] < 30 and robo.sensor_direito.hsv()[1] < 30:
            return -1
        wait(50)
    h1, s1, v1 = robo.sensor_esquerdo.hsv()
    h2, s2, v2 = robo.sensor_direito.hsv()
    verde_esq = detectar_verde(h1, s1, robo)
    verde_dir = detectar_verde(h2, s2, robo)
    vermelho = detectar_vermelho(h1, s1, robo) and detectar_vermelho(h2, s2, robo)
    if vermelho:
        robo.hub.display.icon(Icon.HAPPY)
        robo.motor_esquerdo.stop()
        robo.motor_direito.stop()
        wait(7500)
    elif verde_esq and verde_dir:
        # Meia volta
        a = verificarVerdeDuploFalso(robo)
        if a:
            robo.hub.display.icon(Icon.DOWN)
            robo.hub.imu.reset_heading(0)
            robo.motor_esquerdo.run(200)
            robo.motor_direito.run(-200)
            while(abs(robo.hub.imu.heading()) < 175):
                wait(10)
            robo.direcao.straight(-60)
            robo.hub.display.icon(Icon.CIRCLE)
    elif verde_esq:
        a = verificarVerdeFalso(robo, robo.sensor_esquerdo)
        # Vira para a esquerda
        if a:
            robo.hub.display.icon(Icon.LEFT)

            robo.motor_esquerdo.run(200)
            robo.motor_direito.run(200)
            wait(1000)
            robo.hub.imu.reset_heading(0)
            robo.motor_esquerdo.run(-100)
            robo.motor_direito.run(100)
            while(abs(robo.hub.imu.heading()) < 85):
                wait(10)
            robo.direcao.straight(-30)
            robo.hub.display.icon(Icon.CIRCLE)
    elif verde_dir:
        # Vira para a direita
        a = verificarVerdeFalso(robo, robo.sensor_direito)
        if a:
            robo.hub.display.icon(Icon.RIGHT)

            robo.motor_esquerdo.run(200)
            robo.motor_direito.run(200)
            wait(1000)
            robo.hub.imu.reset_heading(0)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(-100)
            while(abs(robo.hub.imu.heading()) < 85):
                wait(10)
            robo.direcao.straight(-30)
            robo.hub.display.icon(Icon.CIRCLE)