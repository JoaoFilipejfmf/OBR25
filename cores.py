from pybricks.tools import wait
def detectar_verde(h, s, robo):
    return 100 <= h <= 140 and s > 30

def detectar_vermelho(h, s, robo):
    return (0 <= h <= 20 or 340 <= h <= 360) and s > 30

def verificarVerdeFalso(s1, v1, s2, v2, robo):
    robo.motor_direito.stop()
    robo.motor_esquerdo.stop()
    wait(500)
    robo.motor_direito.run(50)
    robo.motor_esquerdo.run(50)
    for i in range(30):
        h1, s1, v1 = robo.sensor_esquerdo.hsv()
        h2, s2, v2 = robo.sensor_direito.hsv()
        if (s1 < 20 and v1 < 40) or (s2 < 20 and v2 < 40):
            return True
        wait(50)
    return False

def verificar_cores(robo):
    h1, s1, v1 = robo.sensor_esquerdo.hsv()
    h2, s2, v2 = robo.sensor_direito.hsv()
    verde_esq = detectar_verde(h1, s1, robo)
    verde_dir = detectar_verde(h2, s2, robo)
    vermelho = detectar_vermelho(h1, s1, robo) and detectar_vermelho(h2, s2, robo)
    if vermelho:
        robo.motor_esquerdo.stop()
        robo.motor_direito.stop()
        return True
    elif verde_esq and verde_dir:
        # Meia volta
        a = verificarVerdeFalso(s1, v1, s2, v2, robo)
        if a:
            robo.motor_esquerdo.run(200)
            robo.motor_direito.run(-200)
            wait(1800)
    elif verde_esq:
        # Vira para a esquerda
        a = verificarVerdeFalso(s1, v1, s2, v2, robo)
        if a:
            robo.motor_esquerdo.run(0)
            robo.motor_direito.run(0)
            wait(1000)
            robo.motor_esquerdo.run(50)
            robo.motor_direito.run(50)
            wait(400)
            robo.motor_esquerdo.run(-100)
            robo.motor_direito.run(100)
            wait(2000)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(100)
            wait(1000)
    elif verde_dir:
        # Vira para a direita
        a = verificarVerdeFalso(s1, v1, s2, v2, robo)
        if a:
            robo.motor_esquerdo.run(0)
            robo.motor_direito.run(0)
            wait(1000)
            robo.motor_esquerdo.run(50)
            robo.motor_direito.run(50)
            wait(400)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(-100)
            wait(1700)
            robo.motor_esquerdo.run(100)
            robo.motor_direito.run(100)
            wait(1000)