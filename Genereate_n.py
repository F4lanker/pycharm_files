def generate_num (n:int, m:int, prefix=None):
    '''Generate all numbers with leadig zeros in N-metric system(N<=10) length M'''
    prefix = prefix or []
    if m==0:
        print(prefix)
        return
    for digit in range (n):
        prefix.append(digit)
        generate_num(n, m-1, prefix)
        prefix.pop()
generate_num(4,3)