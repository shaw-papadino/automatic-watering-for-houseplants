import qwiic_soil_moisture_sensor
from time import sleep
# 土壌水分測定センサー
class SoilMoistureSensor:
    
    mySoilSensor = qwiic_soil_moisture_sensor.QwiicSoilMoistureSensor(address=0x28)

    def isConnected(self):
        return self.mySoilSensor.is_connected()

    def __init__(self):
        for i in range(5):
            if self.isConnected():
                self.mySoilSensor.begin()
                print("initialized.")
                return
            else:
                print("connecting...")
            sleep(0.5)
        raise OSError("Remote I/O Error.")

    def measure(self):
        self.mySoilSensor.read_moisture_level()
        return self.mySoilSensor.level

    def led_off(self):
        self.mySoilSensor.led_off()

if __name__ == "__main__":
    soil = SoilMoistureSensor()
    soil.led_off()
    print(soil.measure())
