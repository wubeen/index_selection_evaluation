import json

class Style():
    def __init__(self, label, color, marker, hatch):
        self.label = label
        self.color = color
        self.marker = marker
        self.hatch = hatch
        self.index_history = None

styles = {
    'epic': Style('Extend', '#4e79a7', 'd', '/'),
    'drop_heuristic': Style('Drop', '#f28e2b', 'P', 'o'),
    'microsoft': Style('AutoAdmin', '#e15759', '.', '.'),
    'microsoft_naive_2': Style('Naive 2', '#9c755f', '.', ''),
    'dexter': Style('Dexter', '#bab0ac', 'X', 'x'),
    'ibm': Style('DB2Advis', '#59a14f', '*', '*'),
    'no_index': Style('No Index', '#76b7b2', '-', 'O'),
    'cophy': Style('CoPhy', '#b07aa1', 'p', '\\'),
    'relaxation': Style('Relaxation', '#ff9da7', '8', '-'),
    'dta_anytime': Style('DTA Anytime', '#edc948', '1', '+'),
    'reinforcement_learning': Style('Deep RL', '#edc948', '1', '+')
}

def get_costs(df):
    costs = []

    for _, row in df.iterrows():
        row_cost = 0
        for column in df.columns:
            if column[0] == 'q':
                row_cost += float(json.loads(row[column])['Cost'])
        costs.append(row_cost)

    return costs

def b_to_gb(b):
    return b / 1000 / 1000 / 1000

def gb_to_b(gb):
    return gb * 1000 * 1000 * 1000

def mb_to_gb(mb):
    return mb / 1000

def s_to_m(s):
    return s / 60