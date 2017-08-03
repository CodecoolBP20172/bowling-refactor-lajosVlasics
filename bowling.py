def score(game):
    result = 0
    frame = 1
    first_throw = True
    for throw in range(len(game)):
        if game[throw] == '/':
            result += 10 - last_throw_score
        else:
            result += get_value(game[throw])
        if frame < 10 and get_value(game[throw]) == 10:
            if game[throw] == '/':
                result += get_value(game[throw+1])
            elif game[throw] == 'X' or game[throw] == 'x':
                result += get_value(game[throw+1])
                if game[throw+2] == '/':
                    result += 10 - get_value(game[throw+1])
                else:
                    result += get_value(game[throw+2])
        last_throw_score = get_value(game[throw])
        if not first_throw:
            frame += 1
        if first_throw:
            first_throw = False
        else:
            first_throw = True
        if game[throw] == 'X' or game[throw] == 'x':
            first_throw = True
            frame += 1
    return result


def get_value(char):
    if char in ("123456789"):
        return int(char)
    elif char.lower() in ("x/"):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
