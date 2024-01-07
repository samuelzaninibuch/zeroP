stored_values = []
data = []

def store(value):
    stored_values.append(value)

def values():
    return stored_values

def list(x, y, value, group,):
    data.append({'x': x, 'y': y, 'value': value, 'group': group})


def listvalue(x, y):
    for row in data:
        if row['x'] == x and row['y'] == y:
            return row['value'], row['group']
    return None

def listposall():
    for row in data:
        print(f'value: {row["value"]} [x={row["x"]}, y={row["y"],} group={row["group"]}]')

def listpos(x1, y1, x2, y2):
    for row in data:
        if x1 <= row['x'] <= x2 and y1 <= row['y'] <= y2:
            print(f'value: {row["value"]} [x={row["x"]}, y={row["y"]}]')
