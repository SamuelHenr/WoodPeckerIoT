from architecture.monitor.read_file import *
from architecture.analyze.engine import *
from architecture.report.inspect import *

class Order:

    def __init__(self):
        self.reader = Reader()
        self.engine = Engine()
        self.inspect = Inspect()

    def execute(self, tickets, threshold, timestamp):
        lines = self.reader.get_data(tickets)
        nodes = self.engine.receive_data(lines)
        review = self.inspect.get_nodes(nodes, threshold, timestamp)
        return review