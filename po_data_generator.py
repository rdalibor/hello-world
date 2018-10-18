import random



#x = input('Enter a number please: ')

#print(d)

#data = [2,5,7]

#print data



file = open("po_cap_mem_po_data.txt", "w")
for x in range(0, 100):
    d = random.randint(0,2**20-1)
    e = format(d, '05x')
    file.write(str(e))
    file.write("\n")
file.close()
