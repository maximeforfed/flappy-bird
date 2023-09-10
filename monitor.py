import array


import Pipes

TPipes = []


def ColisionMonitor():
    pass


def GenerateurDePipe():

    # supresion pipe unutile

    for i in range(0, len(TPipes) -1) :
        positionPipes = TPipes[i].position

        if positionPipes < -400 :
            TPipes.pop(i)


    lentT = len(TPipes)
    for n in range(lentT, 5):

        if len(TPipes) == 0:
            TPipes.append(Pipes.PipesAleatoire(100))
        else:
            TPipes.append(Pipes.PipesAleatoire(TPipes[-1].position +400))




