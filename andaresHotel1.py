def andaresHotel():
    print("Hotel tem 20 andares")
    andar = 0
    for andar in range(1,21,1):
        if(andar != 13):
            print("voce esta no andar:", andar)
    else:
        print("voce percorreu todos os andares do Hotel")
andaresHotel()