def expo(base, power):
    if base == 0 and power == 0:
        raise ArithmeticError
    if base == 1 or power == 0:
        return 1
    if base == 0:
        return 0
    if (base != 0 or base != 1) and power > 0:
        result = base
        while power > 1:
            result *= base
            power -= 1
        if base < 0 < result:
            result -= 2 * result
        return result
    if (base != 0 or base != 1) and power < 0:
        result = base
        power = abs(power)
        while power > 1:
            result *= base
            power -= 1
        if base < 0 < result:
            result -= 2 * result
        return 1 / result


if __name__ == "__main__":
    num = int(input())
    to = int(input())
    res = expo(num, to)
    print(res)
