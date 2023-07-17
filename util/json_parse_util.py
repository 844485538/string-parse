import json


def json_parse(data_str):
    """JSON 字符串格式化"""

    return json.dumps(data_str, sort_keys=True, indent=4, separators=(',', ': '))
