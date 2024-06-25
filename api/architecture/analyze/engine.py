from architecture.analyze.analyze_interface import *

class Engine(Analyze):

    nodes = {}
    
    header = ['Packet ID', 'TIME', 'Size', 'eth.src', 'eth.dst', 'IP.src', 'IP.dst', 'IP.proto', 'port.src', 'port.dst']
    IP_DEVICE = 5
    TIMESTAMP = 1
    
    def create_update_node(self, origin: str, last_modified: int):
        self.nodes[origin] = last_modified

    def receive_data(self, data: [str]):
        for node in data:
            self.create_update_node(node[self.IP_DEVICE], node[self.TIMESTAMP])

        return self.nodes
