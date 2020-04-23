from json import dumps, loads


def to_json(obj):
    json_str = ''
    if type(obj) is int or type(obj) is float:
        json_str = str(obj)
    elif type(obj) is str:
        json_str = "\"" + obj + "\""
    elif type(obj) is bool:
        if obj:
            json_str = 'true'
        else:
            json_str = 'false'
    elif obj is None:
        json_str = 'null'
    elif type(obj) is list or type(obj) is tuple:
        json_str += '['
        for i in range(len(obj)):
            json_str += to_json(obj[i])
            if i != len(obj) - 1:
                json_str += ', '
        json_str += ']'
    elif type(obj) is dict:
        json_str += '{'
        for key in obj:
            json_str += '"' + str(key) + '"' + ': ' + to_json(obj.get(key)) + ', '
        json_str = json_str[:-2]
        json_str += '}'
    return json_str



