
def is_close(a, b):
    return a.unit == b.unit and (a-b)/a <= 0.01
