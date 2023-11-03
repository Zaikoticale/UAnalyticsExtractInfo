class AnalyticsReport:
    def __init__(self, group, type, name, view_id, start_date, end_date, metrics, dimensions):
        self.group = group
        self.type = type
        self.name = name
        self.view_id = view_id
        self.start_date = start_date
        self.end_date = end_date
        self.metrics = metrics
        self.dimensions = dimensions
