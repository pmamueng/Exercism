def slices(series, length):
    final_list = []
    index = 0

    if len(series) < length or length < 1 or series == None:
        raise ValueError("NO!")

    while index <= len(series):
        x = series[index:index+length]
        if len(x) == length:
            final_list.append(x)
        index += 1

    return final_list
