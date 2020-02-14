with open('input.txt', 'r', encoding='utf-8') as f:
    read_data = list(f)

m = int( read_data[-1].strip() )

result_list = []
for index in range( 0, len(read_data)-1 ):
    i, s = read_data[index].strip().split(':')
    if m % int(i) == 0:
        result_list.append( (int(i), str(s)) )
    
result_list = sorted( result_list, key=lambda x:x[0] )    
result_str = ''
if len(result_list) != 0: 
    for d in result_list:
        result_str += d[1]
else:
    result_str = m

print(result_str)
