import json
from functools import wraps


def debug(func):
    function = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return {'error': ex, 'function': function}
    return wrapper


@debug
def read_json(filename):
    with open(filename) as json_file:
        json_data = json.load(json_file)
        return json_data


@debug
def write_to_json_file(filename, data, json_array=None):
    current_data = read_json(filename)
    if json_array is None:
        current_data.update(data)
    else:
        current_data[json_array].append(data)
    with open(filename, 'w') as f_json:
        json.dump(current_data, f_json)


@debug
def delete_from_json_file(filename, key, val=None, json_array=None):
    current_data = read_json(filename)
    if json_array is not None:
        filtered_array = [record for record in current_data[json_array] if not (key in record and record[key] == val)]
        current_data[json_array] = filtered_array
    else:
        if val is not None:
            if key in current_data and current_data[key] == val:
                del current_data[key]
        else:
            del current_data[key]
    with open(filename, 'w') as f_json:
        json.dump(current_data, f_json)
