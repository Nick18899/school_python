f = open('24.txt')
data = f.readlines()
data = data[0]
splited_list = data.split('QW')
len_of_splited=[]
for i in splited_list:
    if len(i)>0:
        len_of_splited.append(len(i))
print(max(len_of_splited))