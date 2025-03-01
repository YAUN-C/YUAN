def jiemi():
    d1=datertime.datetime.now()
    p=int(varin.get())
    for i in range(0,p+1):
        if i==p:
            d2=datetime.datetime.now()
            d=d2-d1
            #输入框
            varout.set(str(d.seconds)+:"s"+str(d.micrseconds/1000)+"ms")
        