import csv,json
config_file = open("config.json","r")
config = json.load(config_file)

class WriteCsv:
    def __init__(self, data,file):
        self.data = data
        self.file = file
    def write(self):
        with open(self.file, "a", encoding="utf-8") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(self.data)
