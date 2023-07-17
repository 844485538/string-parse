import json
from io import StringIO


def json_parse(jsonStr):
    if None == jsonStr and '' == jsonStr:
        return ''
    __bu = StringIO('')
    __last = '\0'
    __current = '\0'
    __indent = 0
    isInQuotationMarks = False

    for i in jsonStr:
        __last = __current
        __current = i
        if __current == '"':
            if __last != '\\':
                isInQuotationMarks = not isInQuotationMarks
            __bu.write(__current)
        elif __current == '{':
            __bu.write(__current)
            if not isInQuotationMarks:
                __bu.write('\n')
                __indent += 1
                __addIndentBlank(__bu, __indent)
        elif __current == '[':
            __bu.write(__current)
            if not isInQuotationMarks:
                __bu.write('\n')
                __indent += 1
                __addIndentBlank(__bu, __indent)
        elif __current == '}':
            if not isInQuotationMarks:
                __bu.write('\n')
                __indent -= 1
                __addIndentBlank(__bu, __indent)
            __bu.write(__current)
        elif __current == ']':
            if not isInQuotationMarks:
                __bu.write('\n')
                __indent -= 1
                __addIndentBlank(__bu, __indent)
            __bu.write(__current)
        elif __current == ',':
            __bu.write(__current)
            if __last != '\\' and (not isInQuotationMarks):
                __bu.write('\n')
                __addIndentBlank(__bu, __indent)
        else:
            __bu.write(__current)
    return __bu.getvalue()


def __addIndentBlank(bu, indent):
    for i in range(indent):
        bu.write('\t')


def json_compress(json_str):
    try:
        json_obj = json.loads(json_str)
    except Exception as e:
        print(e)
        return ""
    else:
        return json.dumps(json_obj, separators=(",", ":"))
