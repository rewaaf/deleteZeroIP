# without . checking
print('The original IP is: 212.05.016.112 # first way')
ip = list('212.05.016.112')
for num in ip:
    if num == '0':
        ip.remove(num)
print('The modified IP is: ' + ''.join(ip))

# with . checking
print('The original IP is: 212.05.016.112 # second way')
ip = list('212.05.016.112')
for num in range(12): # 0-12 not 0-14 because delete 2 digits so the number is 12 not 14 and ip is static!
    if ip[num] == '.':
        newindx = num + 1
        if ip[newindx] == '0':
            del ip[newindx]
print('The modified IP is: ' + ''.join(ip))
