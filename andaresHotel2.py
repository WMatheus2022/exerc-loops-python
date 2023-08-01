def andaresHotel():
    print("Hotel tem 20 andares")
    andar = 21
    for andar in range(20,0,-1):
        if(andar != 13):
            print("voce esta no andar:", andar)
    else:
        print("Voce percorreu todos os andares do Hotel")
        
andaresHotel()