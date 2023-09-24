def xo(s):
    # Check if there is an equal number of x's and o's
    s = s.lower()
    if s.count('x') == s.count('o'):
        return True
    # if there no x or o return true
    elif s.count('x') == 0 and s.count('o') == 0:
        return True
    else:
        return False

xo("dfhsklxoxxo")