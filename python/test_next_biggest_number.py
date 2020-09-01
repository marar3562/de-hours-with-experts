# Test file for next biggest number
num = 3399 # 3939
print([x for x in str(num)])


st = [x for x in str(num)]
a = int(''.join(sorted(st)))                #ascending order
d = int(''.join(sorted(st, reverse=True)))  #descending order
le = len(str(num))                          #length of number
re = list(reversed(str(num)))               #reverse of number

print(a)
print(d)
print(le)
print(re)

if num == d:
    #if descending will never find case where a higher # is found
    out = -1
elif num == a and st[-2:-1][0] != st[-1]:
    #if ascending in all the right order then swap last two #'s
    if le >= 3:
        a_l = st[0:(le-2)]
    else:
        a_l = []
    a_l.append(st[-1])
    a_l.append(st[-2:-1][0])
    out = int(''.join(a_l))
else:
    it = 0
    r_l = []
    m_l = []
    s_l = []
    c_l = []
    it2 = 0
    it3 = 0
    for x in re:
        if it == 0:
            p = x
            it = it + 1
            r_l.append(x)
        else:
            if x >= p:
                p = x
                it = it + 1
                r_l.append(x)
            elif p > x and it3 == 0:
                print(p)
                print(x)
                for y in r_l:
                    if y > x:
                        m_l.append(y)
                        
                print(r_l)
                for z in r_l:
                    if min(m_l) == z and it2 == 0:
                        s_l.append(x)
                        it2 = it2 + 1
                    else:
                        s_l.append(z)
                
                print(st[0:(le-it-1)])
                c_l = st[0:(le-it-1)]
                print(min(m_l))
                c_l.append(min(m_l))
                print(sorted(s_l))
                c_l.extend(sorted(s_l))
            
                out = int(''.join(c_l))
                it3 = it3 + 1
            else:
                it = it + 1

print(out)