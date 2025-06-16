class Data:
    def __init__(self, tempc, tempf, humidity):
        self.tempc = tempc
        self.tempf = tempf
        self.humidity = humidity


    def test():
        return "Test"
    
    def to_dict(self):
        return {
            "tempc": self.tempc,
            "tempf": self.tempf,
            "humidity": self.humidity
        }

