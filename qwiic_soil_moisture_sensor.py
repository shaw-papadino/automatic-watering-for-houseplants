from smbus2 import SMBus

class QwiicSoilMoistureSensor:
    led_off = 0x00
    led_on = 0x01
    get_value = 0x05
    
    default_address = 0x28
    
    bus = SMBus(1)
    
    def get_value(self):
        b = self.bus.write_byte_data(self.get_value, 0, self.default_address)
        print(b)