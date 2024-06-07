from architecture.report.report_interface import *

class Inspect(Report):

    review = {}

    def get_current_timestamp(self) -> int:
        return 1474552815

    def get_nodes(self, nodes: dict, threshold: int):
        for key, value in nodes.items():
            if (int(value) + threshold) < self.get_current_timestamp():
                self.review[key] = False
            else:
                self.review[key] = True
        
        return self.review