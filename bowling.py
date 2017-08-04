def score(game):
    result = 0
    frame = 1
    first_throw = True

    for throw in range(len(game)):
        if game[throw] == '/':
            result += 10 - get_value(game[throw-1])
        else:
            result += get_value(game[throw])

        if game[throw].lower() in ("x/") and frame < 10:
            result += get_value(game[throw+1])
            if game[throw].lower() == 'x':
                if game[throw+2] == '/':
                    result += 10 - get_value(game[throw+1])
                else:
                    result += get_value(game[throw+2])

        if not first_throw or game[throw].lower() == 'x':
            first_throw = True
            frame += 1
        else:
            first_throw = False

    return result


def get_value(char):
    if char in ("-123456789"):
        return ("-123456789").index(char)
    elif char.lower() in ("x/"):
        return 10
    else:
        raise ValueError
