print()
inp = input()


S = set()


for i in inp:
    try:

        if not int(i) in S:
            S.add(int(i))


        else:
            n=''
            while True:
                if n == '':
                    n = i

                if n in inp:
                    n += i
                else:
                    break
            S.add(n)

    except ValueError:
        pass
print(S)