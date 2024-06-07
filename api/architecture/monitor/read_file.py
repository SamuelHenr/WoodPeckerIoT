from architecture.monitor.monitor_interface import *

class Reader(Monitor):

    header = ['Packet ID', 'TIME', 'Size', 'eth.src', 'eth.dst', 'IP.src', 'IP.dst', 'IP.proto', 'port.src', 'port.dst']

    def __init__(self):
        self.last_line = 0

    # This function is expected to return an array of features from header
    def get_data(self, tickets: int) -> str:
        file = open('storage/data.csv', 'r')
        result = []

        for i in range(tickets + self.last_line):
            line = file.readline()
            if i < self.last_line:
                continue
            result.append(line.strip().split(','))

        file.close()
        self.last_line = self.last_line + tickets

        return result