from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction

# Inicialização
class Robo:
    def __init__(self):
        self.valor_calibragem = 0
        self.limiar_branco = 0
        self.limiar_preto = 0
        self.resgate = 0
        self.Kp = 16
        self.Ki = 0
        self.Kd = 0
        self.velocidade_base = 120
        self.integral = 0
        self.erro_anterior = 0
        self.hub = PrimeHub()
        self.sensor_esquerdo = ColorSensor(Port.A)
        self.sensor_direito = ColorSensor(Port.B)
        self.motor_esquerdo = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.motor_direito = Motor(Port.D, Direction.CLOCKWISE)
        self.sensor_ultrassonico = UltrasonicSensor(Port.E)
    def distancia_ultrassonico_centro(self, distancia_do_centro = 49):
        return self.sensor_ultrassonico.distance() + distancia_do_centro