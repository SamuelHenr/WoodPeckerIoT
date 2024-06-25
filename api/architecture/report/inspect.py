from architecture.report.report_interface import *

class Inspect(Report):

    review = {}

    def get_nodes(self, nodes: dict, threshold: int, current_timestamp: int):
        for key, value in nodes.items():
            if (int(value) + threshold) < current_timestamp:
                self.review[key] = False
            else:
                self.review[key] = True
        
        return self.review
