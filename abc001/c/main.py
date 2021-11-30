from decimal import Decimal, ROUND_HALF_UP


def my_round(num):
    return 100 * Decimal(str(num)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def get_dir(deg):
    if 11.25 <= deg < 33.75:
        return "NNE"
    elif 33.75 <= deg < 56.25:
        return "NE"
    elif 56.25 <= deg < 78.75:
        return "ENE"
    elif 78.75 <= deg < 101.25:
        return "E"
    elif 101.25 <= deg < 123.75:
        return "ESE"
    elif 123.75 <= deg < 146.25:
        return "SE"
    elif 146.25 <= deg < 168.75:
        return "SSE"
    elif 168.75 <= deg < 191.25:
        return "S"
    elif 191.25 <= deg < 213.75:
        return "SSW"
    elif 213.75 <= deg < 236.25:
        return "SW"
    elif 236.25 <= deg < 258.75:
        return "WSW"
    elif 258.75 <= deg < 281.25:
        return "W"
    elif 281.25 <= deg < 303.75:
        return "WNW"
    elif 303.75 <= deg < 326.25:
        return "NW"
    elif 326.25 <= deg < 348.75:
        return "NNW"
    else:
        return "N"


def get_pow(dis):
    w = my_round(dis)
    if 0.0 <= w <= 20:
        return 0
    elif 30 <= w <= 150:
        return 1
    elif 160 <= w <= 330:
        return 2
    elif 340 <= w <= 540:
        return 3
    elif 550 <= w <= 790:
        return 4
    elif 800 <= w <= 1070:
        return 5
    elif 1080 <= w <= 1380:
        return 6
    elif 1390 <= w <= 1710:
        return 7
    elif 1720 <= w <= 2070:
        return 8
    elif 2080 <= w <= 2440:
        return 9
    elif 2450 <= w <= 2840:
        return 10
    elif 2850 <= w <= 3260:
        return 11
    elif w >= 3270:
        return 12


deg, dis = map(int, input().split())
if get_pow((dis / 60)) == 0:
    print("C", get_pow((dis / 60)))
else:
    print(get_dir(deg / 10), get_pow((dis / 60)))
