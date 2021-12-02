f = open('17.txt')
data = []
for i in f:
    data.append(int(i))

true_data = []
for i in data:
    if (i % 100) // 10 <= 4 and 3 <= (i % 1000) // 100 <= 7:
        true_data.append(i)
# print(true_data)
print(sorted(true_data))
print(len(true_data))
