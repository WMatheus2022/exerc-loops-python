def andaresHotel():
    print("Hotel tem 20 andares")
    andar = 20
    while(andar >= 1):
        if(andar != 13):
            print("Voce esta no andar: ", andar)
        andar -= 1
    else:
        print("voce percorreu todos os andares do Hotel")
    
andaresHotel()