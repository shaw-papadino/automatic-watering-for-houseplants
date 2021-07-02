from __future__ import print_function
import qwiic_soil_moisture_sensor
import sys
import time

def runExample():

	print("\nSparkFun qwiic soil moisture sensor Example 1\n")
	mySoilSensor = qwiic_soil_moisture_sensor.QwiicSoilMoistureSensor(address=0x28)

	if mySoilSensor.connected == False:
		print("The Qwiic Soil Moisture Sensor device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	mySoilSensor.begin()

	print("Initialized.")

	while True:
		mySoilSensor.read_moisture_level()
		print (mySoilSensor.level)
		mySoilSensor.led_on()
		time.sleep(1)
		mySoilSensor.led_off()
		time.sleep(1)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)
