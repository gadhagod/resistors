def get_sig_figs(value):
    str_value = str(value).replace(".", "")
    while str_value[0] == "0":
        str_value = str_value[1:]
    while str_value[-1] == "0":
        str_value = str_value[:-1]
    return int(str_value)

def reverse_dict(dict):
    return {i: j for j, i in dict.items()}

def get_digits(num):
    return [int(i) for i in str(num).replace(".", "")]
