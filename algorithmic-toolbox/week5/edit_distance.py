# Uses python3
def edit_distance(s, t):
    sl = len(s)
    tl = len(t)
    #return editDistDP(s, t, sl, tl)
    table = [[0 for x in range(tl + 1)] for x in range(sl + 1)] 

    for si in range(sl + 1):
        for ti in range(tl + 1):
            if si == 0:
                table[si][ti] = ti
            elif ti == 0:
                table[si][ti] = si
            elif s[si - 1] == t[ti - 1]:
                table[si][ti] = table[si - 1][ti - 1]
            else:
                table[si][ti] = 1 + min(
                    table[si - 1][ti],
                    table[si - 1][ti - 1],
                    table[si][ti - 1]
                )
    return table[sl][tl]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
