from pyswip import *


if __name__ =="__main__":

    prolog = Prolog()
    prolog.consult("baza_wiedzy.pl")
    a = Variable()
    jest_to_film = Functor("jest_to_film", 1)
    jest_to_film_query = Query(jest_to_film(a))
    while jest_to_film_query.nextSolution():
        print(a.value)
    jest_to_film_query.closeQuery()




