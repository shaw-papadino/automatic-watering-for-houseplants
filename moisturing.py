from soil_moisture_sensor import SoilMoistureSensor

import csv
import datetime
from time import sleep
import argparse

class Moisturing:
    def __init__(self, soil_moisture, measure_interval):
        self.soil_moisture = soil_moisture
        self.measure_interval = measure_interval

    def record(self, measure_days):
        today = datetime.date.today()
        finish_date = today + datetime.timedelta(days=measure_days)
        header = ["time", "moisture"]
        print("csvに記録を始めます")
        with open(f"{str(today)}_{str(finish_date)}.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            while datetime.date.today() <= finish_date:
                writer.writerow([f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}", self.soil_moisture.measure()])
                sleep(self.measure_interval)
        print("記録を終了します")

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mi", "--measure_interval", help="Interval for measuring moisture. It's second.", type=int)
    parser.add_argument("-md", "--measure_days", help="Days for measuring moisture. It's day.", type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = args()
    soil_moisture = SoilMoistureSensor()
    Moisturing(soil_moisture, args.measure_interval).record(args.measure_days)