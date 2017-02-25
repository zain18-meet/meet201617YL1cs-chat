def add_break_line(s):

    '''
    Add a '\r' every 17 charachters
    '''
    for  in s:
        
        s = s[0:17] +'\r' + s[17:]
        return s


result = add_break_line('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print(result)
