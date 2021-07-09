#!/usr/bin/python3

from soil_moisture_sensor import SoilMoistureSensor
from house_plant import HousePlant

import os
import csv
import datetime
from time import sleep
import argparse

class Moisturing:

    def __init__(self, soil_moisture, plant, measure_interval):
        self.soil_moisture = soil_moisture
        self.plant = plant
        self.measure_interval = measure_interval

    def record(self, measure_days, filename):

        isfile = True if os.path.isfile(filename) else False

        header = ["time", "moisture"]
        today = datetime.date.today()
        finish_date = today + datetime.timedelta(days=measure_days)
        while datetime.date.today() <= finish_date:
            with open(filename, "a", buffering=1) as f:
                writer = csv.writer(f)
                if isfile != False:
                    writer.writerow(header)
                writer.writerow(
                    [
                        f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                        self.translate(self.soil_moisture.measure(), self.plant.min, self.plant.max)
                    ]
                )
            sleep(self.measure_interval)
        print("記録を終了します")

    def isRange(self, value):
        return self.plant.min <= value <= self.plant.max

    def translate(self, value, fromLow, fromHigh, toLow=0, toHigh=100):
        if self.isRange:
            return -1
        return toHigh - (value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mi", "--measure_interval", help="Interval for measuring moisture. It's second.", type=int)
    parser.add_argument("-md", "--measure_days", help="Days for measuring moisture. It's day.", type=int)
    parser.add_argument("-fn", "--filename", help="Days for measuring moisture. It's day.")
    return parser.parse_args()

def set_filename(measure_days):
    today = datetime.date.today()
    finish_date = today + datetime.timedelta(days=measure_days)
    return f"./result/{str(today)}_{str(finish_date)}.csv"

if __name__ == "__main__":
    args = args()
    measure_interval = 3600 if args.measure_interval is None else args.measure_interval
    measure_days = 1 if args.measure_days is None else args.measure_days
    filename = set_filename() if args.filename is None else args.filename

    soil_moisture = SoilMoistureSensor()
    house_plant = HousePlant()
    Moisturing(soil_moisture, house_plant, measure_interval).record(measure_days, filename)
