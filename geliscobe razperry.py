#les bibliotheques imu et vector3d mawjoudin sur internet, telechargihom from imu import MPU6050
from time import sleep_ms
import time
from machine import Pin, I2C, Timer
import math
i2c = I2C(0, sda=Pin(0), scl=Pin (1), freq=400000)
imu = MPU6050(i2c)
def map (value, in_min, in_max, out_min, out_max):
     value = max(in_min, min(in_max, value))
     return (value in_min) * (out_max out_min) / (in_max in_min) + out_min

while True:
   ax = imu.accel.x
   ay = imu.accel.y
   az = imu.accel.z
Xangle = math.atan2 (ay, math.sqrt(ax**2 + az**2)) * 180 / math.pi
Yangle = math.atan2 (ax, math.sqrt(ay**2 + az**2)) * 180 / math.pi
tem = round(imu.temperature, 2)
led = int(map (Xangle 0 10,2, 8))
Pin(led Pin.OUT value = 0).on()
time.sleep_ms(50)
Pin(led Pin.OUT value = 0).off()
print("X angle:", round (Xangle, 2), "ty angle:", round (Yangle, 2), "tTemper