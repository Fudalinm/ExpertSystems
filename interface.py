from pyswip import *

def read():
    x = str(input())
    return x
def py_read(pytanie, odp):
    print(pytanie," ? (tak/nie)")
    inp = read()
    while inp not in ["tak", "nie"]:
        print("odpowiedz musi być (tak/nie)")
        inp = read()
    odp.unify(inp)
    return True
    # PL_cons_functor_v()
    # prolog.query("pamietaj("+ str(X) +"," + inp+")").close()
    # prolog.query("pamietaj(X,"+inp+")").close()


py_read.arity = 2
if __name__ =="__main__":

    prolog = Prolog()
    registerForeign(py_read)
    prolog.consult("baza_wiedzy.pl")
    # to też działa :D
    # for result in prolog.query("jest_to_film(X)"):
    #     # r = result["X"]
    #     # print(r)
    #     pass
    X = Variable()

    jest_to_film = Functor("znajdz_film",1)
    q = Query(jest_to_film(X))
    while q.nextSolution():
        print("Hello,", X.value)
    q.closeQuery()




