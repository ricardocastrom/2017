def princces(lista):
    tamano=lista[0]
    print (tamano)
    contador=0
    lista=lista[1:]
    posicionM=[]
    posicionP=[]
    split2=tamano
    listaTrabajo=[]
    while(contador<3):
        
        numero=0
        print(lista[contador])
        x=(lista[contador]).split(' ', split2)
        print(x)
        if (x== ['', '']):
                
            contador2=contador2+1
        else:
            listaTrabajo.append(x)
              
        contador=contador+1

    contador=0
    print(listaTrabajo)
    while(contador<3):
        contador2=0
        while (contador2<tamano):
            if((listaTrabajo[contador][contador2])=="m"):
                posicionM=[contador,contador2]
            elif(listaTrabajo[contador][contador2]=="p"):
                posicionP=[contador,contador2]    
            contador2=contador2+1
        contador=contador+1
    print(posicionM,posicionP)
    tamano=abs(posicionM[0]-posicionP[0])
    while(tamano!=0):
        if(posicionM[0]>posicionP[0]):
            posicionM[0]=posicionM[0]-1
            print('Up')
            tamano=abs(posicionM[0]-posicionP[0])
        elif (posicionM[0]<posicionP[0]):
            posicionM[0]=posicionM[0]+1
            print('Down')
            tamano=abs(posicionM[0]-posicionP[0])

    tamano=abs(posicionM[1]-posicionP[1])
    while(tamano!=0):
        if(posicionM[1]>posicionP[1]):
            posicionM[1]=posicionM[1]-1
            print('left')
            tamano=abs(posicionM[1]-posicionP[1])
        elif (posicionM[1]<posicionP[1]):
            posicionM[1]=posicionM[1]+1
            print('right')
            tamano=abs(posicionM[1]-posicionP[1])
                
    
        
    
        contador=contador+1
    
    
