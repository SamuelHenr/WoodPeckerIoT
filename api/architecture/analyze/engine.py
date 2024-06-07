from architecture.analyze.analyze_interface import *

class Engine(Analyze):

    nodes = {}

    def create_update_node(self, origin: str, last_modified: int):
        self.nodes[origin] = last_modified

    def receive_data(self, data: [str]):
        for node in data:
            self.create_update_node(node[5], node[1])

        return self.nodes