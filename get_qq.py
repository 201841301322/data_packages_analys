import os
print "input this IP"
a=raw_input()
while 1:
        os.system("tcpdump host "+a+" -c 100 -w ./99.pcap")
        f = open('99.pcap','rb')
        n = 0;
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
        #print(w)
        stra=w.find('00000d')
        allnum=w[stra+5:stra+26]
        #print(allnum)
        if allnum[19]!= '3':
                if w[stra+5:stra+24:2][1:].isalpha():
                        print w[stra+5:stra+24:2][1:]
                        #print w[stra+5:stra+24:2][1:].isalpha
                        continue
                print w[stra+5:stra+24:2][1:]
                break
        else:
                if w[stra+5:stra+26:2][1:].isalpha():
                        print w[stra+5:stra+26:2][1:]
                        #print w[stra+5:stra+26:2][1:].isalpha
                        continue
                print w[stra+5:stra+26:2][1:]
                break
#print('\n\ntotal bytes: %d'%n)
f.close()
