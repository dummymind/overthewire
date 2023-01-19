
f=open("natas20","w")

for i in range(1,641):
    t=str(i)+'-admin'
    print(t.encode("utf-8").hex())
    f.write(t.encode("utf-8").hex()+'\n')

f.close()
