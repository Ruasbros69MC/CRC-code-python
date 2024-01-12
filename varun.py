def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
data = "101011"
key = "11011"
l_key = len(key)
append_data=data + '0'*(l_key-1)
lenght=len(key)
temp=append_data[0:lenght]
while lenght<len(append_data):
    if temp[0]=='1':
        temp=xor(key,temp)+append_data[lenght]
    else:
        temp=xor('0'*lenght,temp)+append_data[lenght]  
    lenght+=1
if temp[0]=='1':
    temp=xor(key,temp)
else:
    temp=xor('0'*lenght,temp)
word=temp
print(word)
codeword = data+word
print("Remainder : ", word)
print("Data + word:",codeword)

    