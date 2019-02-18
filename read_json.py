import twitter
def read_json(json_, path):
    """
    (object, list) -> object
    Returns a part of json file which is stated in "path".
    """
    value = json_[path[0]]
    if len(path) == 1:
        return value
    else:
        return read_json(value, path[1:len(path)])

