def arithmetic_arranger(_list, ans=False):
    oper = ["+", "-"]
    length = len(_list)
    error_check = 0
    v = [i.split() for i in _list]
    p = [' '*(len(t[1]+' '+t[2]) - len(t[0]))+t[0] if len(t[0]) < len(t[2]) else '  '+ t[0] for t in v]
    c = [t[1]+' ' +' '*(len(t[0]) - len(t[2])) + t[2] if len(t[0]) > len(t[2]) else t[1]+' '+t[2] for t in v]
    l = ['-'*len(i) for i in c]
    if len(_list) > 5:
        print("Error: Too many problems")
    else:
        while length != 0:
            for _str in _list:
                str_i = _str.split(" ")
                for k in str_i:
                    if not(str_i[0].isnumeric()) or not(str_i[2].isnumeric()):
                        print("Error: Numbers must contain only digits.")
                        error_check += 1
                        break
                    elif str_i[1] not in oper:
                        print("Error: Operator must be '+' or '-'.")
                        error_check += 1
                        break
                    elif len(str_i[0]) > 4 or len(str_i[2])> 4:
                        print("Numbers cannot be more than four digits.")
                        error_check += 1
                        break
            length -= 1
            if error_check > 0:
                break
        if error_check == 0:
            if ans != True:
                print(*p, sep='    ')
                print(*c, sep='    ')
                print(*l, sep='    ')
            else:
                v = [i.split() for i in _list]
                p = [' '*(len(t[1]+' '+t[2]) - len(t[0]))+t[0] if len(t[0]) < len(t[2]) else '  '+ t[0] for t in v ]
                c = [t[1]+' ' +' '*(len(t[0]) - len(t[2])) + t[2] if len(t[0]) > len(t[2]) else t[1]+' '+t[2] for t in v]
                l = ['-'*len(i) for i in c]
                a = [str(eval(_list[i] )).rjust(len(l[i])) for i in range(len(l))]
                print(*p, sep='    ')
                print(*c, sep='    ')
                print(*l, sep='    ')
                print(*a, sep='    ') 

arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"])
print( )
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# ==============================================================================================================================================














  