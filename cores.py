from pybricks.tools import wait
import robot
def detectar_verde(h, s, robo):
    return 100 <= h <= 140 and s > 30

def detectar_vermelho(h, s, robo):
    return (0 <= h <= 20 or 340 <= h <= 360) and s > 30

def verificarVerdeFalso(robo, sensor):
    robo.motor_direito.stop()
    robo.motor_esquerdo.stop()
    wait(500)
    robo.motor_direito.run(50)
    robo.motor_esquerdo.run(50)
    for i in range(400):
        reflet = sensor.reflection()
        s1 = robo.sensor_esquerdo.hsv()[1]
        s2 = robo.sensor_direito.hsv()[1]
        print(f'{s1}, {s2}, {reflet}')
        if (s1 < 20 and s2 < 20) and (reflet < robo.limiar_preto):
            return True
        wait(10)
    return False

def verificarVerdeDuploFalso(robo):
    robo.motor_direito.stop()
    robo.motor_esquerdo.stop()
    wait(500)
    robo.motor_direito.run(50)
    robo.motor_esquerdo.run(50)
    for i in range(400):
        r1 = robo.sensor_esquerdo.reflection()
        r2 = robo.sensor_direito.reflection()
        s1 = robo.sensor_esquerdo.hsv()[1]
        s2 = robo.sensor_direito.hsv()[1]
        if (s1 < 20 and s2 < 20) and (r1 < robo.limiar_preto and r2 < robo.limiar_preto):
            return True
        wait(10)
    return False

def verificar_cores(robo):
    if robo.sensor_esquerdo.hsv()[1] < 30 and robo.sensor_direito.hsv()[1] < 30:
        return -1
    robo.motor_esquerdo.stop()
    robo.motor_direito.stop()
    for i in range(20):
        if robo.sensor_esquerdo.hsv()[1] < 30 and robo.sensor_direito.hsv()[1] < 30:
            return -1
        wait(100)
    h1, s1, v1 = robo.sensor_esquerdo.hsv()
    h2, s2, v2 = robo.sensor_direito.hsv()
    verde_esq = detectar_verde(h1, s1, robo)
    verde_dir = detectar_verde(h2, s2, robo)
    vermelho = detectar_vermelho(h1, s1, robo) and detectar_vermelho(h2, s2, robo)
    if vermelho:
        print('legal')
        robo.motor_esquerdo.stop()
        robo.motor_direito.stop()
        return 1
    elif verde_esq and verde_dir:
        # Meia volta
        a = verificarVerdeDuploFalso(robo)
        if a:
            robo.hub.imu.reset_heading(0)
            robo.motor_esquerdo.run(200)
            robo.motor_direito.run(-200)
            while(abs(robo.hub.imu.heading()) < 175):
                wait(10)
    elif verde_esq:
        # Vira para a esquerda
        a = verificarVerdeFalso(robo, robo.sensor_esquerdo)
        if a:
            robo.motor_esquerdo.run(0)
            robo.motor_direito.run(0)
            wait(1000)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(100)
            wait(2000)
            robo.hub.imu.reset_heading(0)
            robo.motor_esquerdo.run(-100)
            robo.motor_direito.run(100)
            while(abs(robo.hub.imu.heading()) < 85):
                wait(10)                
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(100)
            wait(1000)
    elif verde_dir:
        # Vira para a direita
        a = verificarVerdeFalso(robo, robo.sensor_direito)
        if a:
            robo.motor_esquerdo.run(0)
            robo.motor_direito.run(0)
            wait(1000)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(100)
            wait(2000)
            robo.hub.imu.reset_heading(0)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(-100)
            while(abs(robo.hub.imu.heading()) < 85):
                wait(10)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(100)
            wait(1000)