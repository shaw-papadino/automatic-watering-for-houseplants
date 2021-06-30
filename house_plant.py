from soil_moisture_sensor import SoilMoistureSensor
# 観葉植物
class HousePlant:
    # TODO:水分量の閾値をもつ変数と必要な水分量をはっきりさせたい
    def __init__(self, need_water):
        self.need_water = need_water