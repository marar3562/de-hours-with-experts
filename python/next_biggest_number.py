#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    #
    st = [x for x in str(num)]                  #list of number
    a = int(''.join(sorted(st)))                #ascending order
    d = int(''.join(sorted(st, reverse=True)))  #descending order
    le = len(str(num))                          #length of number
    re = list(reversed(str(num)))               #reverse of number
    
    if num == d:
        #if descending will never find case where a higher # is found
        out = -1
    elif num == a and st[-2:-1][0] != st[-1]:
        #if ascending in all the right order then swap last two #'s 
        ## caveat here is if the last two are the same numbers this will not work
        if le >= 3:
            a_l = st[0:(le-2)]
        else:
            a_l = []
        a_l.append(st[-1])
        a_l.append(st[-2:-1][0])
        out = int(''.join(a_l))
    else:
        # all other scenarios
        it = 0
        r_l = []
        m_l = []
        s_l = []
        c_l = []
        it2 = 0
        it3 = 0
        for x in re:
            # process backwards
            if it == 0:
                p = x
                it = it + 1
                r_l.append(x)
            else:
                # find where the values decrease from right to left
                if x >= p:
                    p = x
                    it = it + 1
                    r_l.append(x)
                elif p > x and it3 == 0:
                    # finding value where the decrease occurs ("d")
                    for y in r_l:
                        # find smallest value of remaining values ("m") that is greater than "d"
                        if y > x:
                            m_l.append(y)
                    
                    # replace "r" with "d", which becomes list "s"
                    for z in r_l:
                        if min(m_l) == z and it2 == 0:
                            s_l.append(x)
                            it2 = it2 + 1
                        else:
                            s_l.append(z)
                    
                    c_l = st[0:(le-it-1)]   # values before "d" stay
                    c_l.append(min(m_l))    # "m"
                    c_l.extend(sorted(s_l)) # arrange list "s" in ascending order
                
                    out = int(''.join(c_l))
                    it3 = it3 + 1
                else:
                    break
    
    return out

if __name__ == "__main__":
    main()

