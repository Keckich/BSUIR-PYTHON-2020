def int_check(obj):
    try:
        int(obj)
        return True
    except:
        return False


def float_check(obj):
    try:
        float(obj)
        return True
    except:
        return False


def from_json_str(text, pos=1):
    i = pos
    while text[i] != '"':
        i += 1
    return text[pos:i], i


def from_json_number(text, pos=0):
    i = pos
    while text[i] != ',' and text[i] != ']' and text[i] != '}':
        i += 1
        if i is len(text) - 1:
            if int_check(text):
                return int(text)
            else:
                return float(text)
    return [text[pos:i], i - 1]


def from_json(text):
    if text[0] is '[':
        return from_json_list(text, 1)[0]
    elif text[0] is '"':
        return from_json_str(text, 1)[0]
    elif text[0] is '{':
        return from_json_dict(text, 1)[0]
    elif text[0] is 'n':
        return None
    elif text[0] is 't':
        return True
    elif text[0] is 'f':
        return False
    else:
        return from_json_number(text, 0)


def from_json_list(text, pos=1):
    objects = []
    i = pos
    while i < len(text):
        if text[i] is ']':
            return objects, i
        elif text[i] is ',' or text[i] is ' ':
            i += 1
            continue
        elif text[i] is '[':
            obj = from_json_list(text, i + 1)
            objects.append(obj[0])
            i = obj[1]
        elif text[i] is '{':
            obj = from_json_dict(text, i + 1)
            objects.append(obj[0])
            i = obj[1]
        elif text[i] is '"':
            obj = from_json_str(text, i + 1)
            objects.append(obj[0])
            i = obj[1]
        elif text[i] is 'n':  # means null
            objects.append(None)
            i += 3
        elif text[i] is 't':  # means true
            objects.append(True)
            i += 3
        elif text[i] is 'f':  # means false
            objects.append(False)
            i += 4
        else:
            obj = from_json_number(text, i)
            if int_check(obj[0]):
                objects.append(int(obj[0]))
            else:
                objects.append(float(obj[0]))
            i = obj[1]
        i += 1


def from_json_dict(text, pos=1):
    objects = {}
    i = pos
    while i < len(text):
        if text[i] is '}':
            return objects, i
        elif text[i] is ',' or text[i] is ' ' or text[i] is ':':
            i += 1
            continue
        elif text[i] is '"':
            obj = from_json_str(text, i + 1)
            key, i = obj[0], obj[1]
            i += 1
            while i < len(text):
                if text[i] is ':' or text[i] is ' ':
                    i += 1
                    continue
                elif text[i] is '"':
                    obj = from_json_str(text, i + 1)
                    objects[key], i = obj[0], obj[1]
                elif text[i] is '[':
                    obj = from_json_list(text, i + 1)
                    objects[key], i = obj[0], obj[1]
                elif text[i] is '{':
                    obj = from_json_dict(text, i + 1)
                    objects[key], i = obj[0], obj[1]
                elif text[i] is 'n':  # null
                    objects[key] = None
                    i += 3
                elif text[i] is 't':  # true
                    objects[key] = True
                    i += 3
                elif text[i] is 'f':  # false
                    objects[key] = False
                    i += 4
                else:
                    obj = from_json_number(text, i)
                    if int_check(obj[0]):
                        objects[key] = int(obj[0])
                    else:
                        objects[key] = float(obj[0])
                    i = obj[1]
                break
        i += 1


