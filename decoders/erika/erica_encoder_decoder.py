import json
# import sys
# sys.path.append('./')
class DDR_ASCII():
    
    CONVERSION_TABLE_PATH = r"C:\Program Files (x86)\sigrok\PulseView\share\libsigrokdecode\decoders\erika\charTranslation.json"
    
    def __init__(self, *args, **kwargs):
        self.read_conversion_table()
        print("init :)")
    
    def read_conversion_table(self):
        """read conversion table from file and populate 2 dicts"""
        with open(self.CONVERSION_TABLE_PATH, encoding="UTF-8") as f:
            self.ascii_2_ddr = json.load(f)
        self.ddr_2_ascii = {value: key for 
                            key, value in self.ascii_2_ddr.items()}
    
    def encode(self, data):
        return self.ascii_2_ddr[data]

    def try_encode(self, data, input_as_default = True):
        default = data if input_as_default else None
        return self.ascii_2_ddr.get(data, default)

    def decode(self, data):
        return self.ddr_2_ascii[data]

    def try_decode(self, data, input_as_default = True):
        default = data if input_as_default else None
        print(data)
        return self.ddr_2_ascii.get(data, default)