import os
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
print("抖音:"+str(w.count("646f7579696e",0,len(w)))+"\n")
print("快手:"+str(w.count("736d696c65",0,len(w)))+"\n")
print("微信:"+str(w.count("77656978696",0,len(w)))+"\n")
print("微博:"+str(w.count("776569626f",0,len(w)))+"\n")
print("网易云:"+str(w.count("6d7573696303",0,len(w)))+"\n")
print("酷安:"+str(w.count("636f6f6c61706b",0,len(w)))+"\n")
print("夸克:"+str(w.count("71756172",0,len(w)))+"\n")
print("飞猪旅行:"+str(w.count("747269702e74616f62616f",0,len(w)))+"\n")
print("王者荣耀:"+str(w.count("000b000b4013",0,len(w)))+"\n")
print("知乎:"+str(w.count("7a68696875",0,len(w)))+"\n")
print("拼多多:"+str(w.count("70696e64756f64756f2e636f6d",0,len(w)))+"\n")
print("支付宝/蚂蚁财富:"+str(w.count("616c697061792e636f6d",0,len(w)))+"\n")
print("腾讯自选股:"+str(w.count("74656e63656e742e706f7274666f6c696f",0,len(w)))+"\n")
print("百度网盘:"+str(w.count("70616e2e62616964752e636f6d",0,len(w)))+"\n")
print("优学院:"+str(w.count("756c6561726e696e672e636e",0,len(w)))+"\n")
print("QQ:"+str(w.count("33672e71712e636f6d",0,len(w)))+"\n")
print("运动世界校园:"+str(w.count("697964736a2e636f6d",0,len(w)))+"\n")


f.close()
