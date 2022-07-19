#for w połączeniu z break

list=[-10,-5,0,5,10,15]

for x in list:
    if x>=0: #jedzie od lewej do prawej, jeśli bym dała if x<=0, nic nie wypisze bo od razu na "-10" urywa/breakuje
        break
    print(x,end=" ")
