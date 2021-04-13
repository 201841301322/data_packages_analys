import os
f = open('ff.pcap','rb')
n = 0
s = f.read(1)
w=''
while s:
        byte = ord(s)
        n = n+1
                #print('%d'%byte)
                #print('%02x'%(byte),end='')
                #print(type(q))
                #print(byte)
        v='%02x'%(byte)
                #print(type(v))
        w=w+v
                #if n%16==0:
                #        print('')
        s = f.read(1)
                #w=w+q

endip=w.find('01bb')
stra=w.find('c0a8')
print(w[endip-16:endip])
print(endip)
if stra>=endip-15:
        print(w[endip-16:endip-8])
elif stra<endip-15:
        print(w[endip-8:endip])
#print(w[148:156])#+w[156:164])
        #allnum=w[stra+5:stra+26]
        #print(allnum)
#print('\n\ntotal bytes: %d'%n)
f.close()
