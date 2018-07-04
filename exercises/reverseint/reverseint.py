def reverseint(n):
    if n == 0:
        return 0
    elif n < 0:
        strip = str(n).replace('-', '')
        return int(strip[::-1]) * -1
    elif n > 0:
        return int(str(n)[::-1])
