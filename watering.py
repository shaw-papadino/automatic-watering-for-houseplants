from watering_tool import Pomp
from soil_moisture_sensor import SoilMoistureSensor
from house_plant import HousePlant

from time import sleep
import argparse

class Watering:
    def __init__(self, watering_tool, soil_moisture, measure_interval, water_interval):
        self.watering_tool = watering_tool
        self.soil_moisture = soil_moisture
        self.measure_interval = measure_interval
        self.water_interval = water_interval

    def isWatering(self, house_plant):
        return self.soil_moisture.measure() <= house_plant.need_water

    def waterFor(self, house_plant):
        while self.isWatering(house_plant):
            self.watering_tool.water()
            sleep(self.water_interval)

        
    def run(self, house_plant):
        while True:
            self.waterFor(house_plant)
            sleep(self.measure_interval)

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--measure_interval", help="Interval for measuring moisture. It's second.", type=int)
    parser.add_argument("-w", "--water_interval", help="Interval for watering to house plants. It's second.", type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = args()
    
    watering_tool = Pomp()
    soil_moisture = SoilMoistureSensor()
    watering = Watering(watering_tool, soil_moisture, args.measure_interval, args.water_interval)

    house_plant = HousePlant(120)
    watering.run(house_plant)