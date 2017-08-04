def score(game):
    result = 0
    frame = 1
    first_throw = True

    for ball in range(len(game)):
        if game[ball] == '/':
            result += 10 - last_throw_score
        else:
            result += get_value(game[ball])

        if frame < 10 and get_value(game[ball]) == 10:
            if game[ball] == '/':
                result += get_value(game[ball+1])
            elif game[ball] == 'X' or game[ball] == 'x':
                result += get_value(game[ball+1])
                if game[ball+2] == '/':
                    result += 10 - get_value(game[ball+1])
                else:
                    result += get_value(game[ball+2])

        last_throw_score = get_value(game[ball])
        
        if first_throw:
            first_throw = False
        else:
            first_throw = True
            frame += 1

        if game[ball].lower() == 'x':
            first_throw = True
            frame += 1
    
    return result


def get_value(char):
    if char in ("-123456789"):
        return ("-123456789").index(char)
    elif char.lower() in ("x/"):
        return 10
    else:
        raise ValueError
