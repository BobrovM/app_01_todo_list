#1
filenames=['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")
ips=['100.122.133.105', '100.122.133.111']
num=int(input("Enter index: "))
print(ips[num])