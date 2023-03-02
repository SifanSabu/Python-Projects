def bulletCalc():
    print("Fourth Times the Charm or Triple Tap?")
    print("Please Choose: [fttc] or [tt]")
    choice = str(input())
    if( choice == "fttc" ):
        fttc()
    elif( choice == "tt" ):
        tt()
    else:
        print("Please choose a valid perk.\n")
        bulletCalc()

def fttc():
    print("\nBase Magazine Size: ")
    baseMag = int(input())
    roundsLeft = baseMag
    totalFired = 0
    extraBullets = 0
    count = 0

    while roundsLeft >=0:
        if(roundsLeft == 0):
            break
        totalFired += 1
        roundsLeft -= 1
        count += 1
        
        if (count == 4):
            extraBullets += 2
            roundsLeft += 2
            print("Fourth Times the Charm procs on bullet: " +str(totalFired))
            count = 0

    print("Total Fired: " +str(totalFired) + " with " + str(extraBullets) + " extra bullets.\n")
    bulletCalc()

def tt():
    print("\nBase Magazine Size: ")
    baseMag = int(input())
    roundsLeft = baseMag
    totalFired = 0
    extraBullets = 0
    count = 0

    while roundsLeft >=0:
        if(roundsLeft == 0):
            break
        totalFired += 1
        roundsLeft -= 1
        count += 1
        
        if (count == 3):
            extraBullets += 1
            roundsLeft += 1
            print("Triple Tap procs on bullet: " +str(totalFired))
            count = 0

    print("Total Fired: " +str(totalFired) + " with " + str(extraBullets) + " extra bullets.\n")
    bulletCalc()


bulletCalc()
