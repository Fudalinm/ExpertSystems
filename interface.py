from pyswip import Prolog, Functor, call, Query,Variable


if __name__ =="__main__":

    prolog = Prolog()
    prolog.consult("baza_wiedzy.pl")
    # list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
    q = prolog.query("jest_to_film(kevin_sam_w_domu)")
    X = Variable()
    print(sorted(prolog.query("jest_to_film(X)")))
