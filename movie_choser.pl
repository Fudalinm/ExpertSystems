:-include('baza_wiedzy.pl').
        pytaj(X) :- !, format('~w? (t/n)~n',[X]),
        read(Reply),
        pamietaj(X,Reply).



        wyczysc_fakty :- write('Przycisnij cos aby wyjsc'), nl,
        retractall(xpozytywne(_)),
        retractall(xnegatywne(_)),
        get_char(_).

        wykonaj :- set_stream(current_output, tty(true)), jest_to_film(X), !,
        format('~nPolecanym filmem moze byc ~w', X),
        nl, wyczysc_fakty.

        wykonaj :- set_stream(current_output, tty(true)), write('Nie jestem w stanie polecić żadnego filmu.'), nl,
        wyczysc_fakty.
