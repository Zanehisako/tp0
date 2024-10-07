def Same(n,m):
    if n%2 == 0 and m%2 != 0:
       return True
    else:
        return False

print('Enter un chiffre:')
number = input()
single_numbers = list(map(int,number))
for i in range(len(single_numbers)-1):
    print(single_numbers[i])
    if single_numbers[i]<single_numbers[i+1] and Same(single_numbers[i],single_numbers[i+1])  :
       n = single_numbers [i] 
       single_numbers[i] = single_numbers[i+1]
       single_numbers[i+1] = n
    if single_numbers[i-1]<single_numbers[i] and i>0 and Same(single_numbers[i-1],single_numbers[i]):
       n = single_numbers [i] 
       single_numbers[i] = single_numbers[i-1]
       single_numbers[i-1] = n
print(single_numbers)
single_numbers = list(map(str,single_numbers))
single_numbers = ''.join(single_numbers)
int(single_numbers)
print(single_numbers);
