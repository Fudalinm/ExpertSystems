:- dynamic
        xpozytywne/1,
        xnegatywne/1.

        znajdz_film(X) :- jest_to_film(X),
        format('~nPolecanym filmem moze byc ~w', X),
        nl, wyczysc_fakty.

        jest_to_film(madagaskar) :- jest_to(animacja),jest_to(familijny),jest_to(dla_dzieci).
        jest_to_film(szeregowiec_ryan) :- jest_to(dramat), jest_to(historyczny).
        jest_to_film(fight_club) :- jest_to(thriller), jest_to(historyczny).
        jest_to_film(nietykalni) :- jest_to(dramat), jest_to(komedia).
        jest_to_film(incepcja) :- jest_to(thriller), jest_to(sci_fi).
        jest_to_film(siedem) :- jest_to(kryminal), jest_to(thriler).
        jest_to_film(wyspa_tajemnic) :- jest_to(thriller), jest_to(dramat).
        jest_to_film(piekny_umysl) :- jest_to(dramat), jest_to(historyczny).
        jest_to_film(seks_misja) :- jest_to(komedia), jest_to(sci_fi).
        jest_to_film(efekt_motyla) :- jest_to(thriller), jest_to(sci_fi), pozytywne('Czy wierzysz w teorie spiskowe').
        jest_to_film(lsnienie) :- jest_to(horror).
        jest_to_film(django) :- jest_to(western), jest_to(komedia).
        jest_to_film(sherlock_holmes) :- jest_to(kryminal), jest_to(przygodowy).
        jest_to_film(interstellar) :- jest_to(sci_fi).
        jest_to_film(harry_potter) :- jest_to(familijny), jest_to(fantasy),jest_to(dla_dzieci),jest_to(przygodowy).
        jest_to_film(deadpool) :- jest_to(komedia),jest_to(akcja),jest_to(sci_fi).
        jest_to_film(zjawa) :- jest_to(dramat),jest_to(przygodowy),jest_to(western).
        jest_to_film(deadpool) :- jest_to(komedia),jest_to(akcja),jest_to(sci_fi).
        jest_to_film(teoria_wszystkiego) :- jest_to(biograficzny),jest_to(dramat),jest_to(edukacyjny).
        jest_to_film(snajper) :- jest_to(biograficzny),jest_to(dramat),jest_to(wojenny).
        jest_to_film(laibrynt_fauna) :- jest_to(dramat),jest_to(fantastyka).
        jest_to_film(alien) :- jest_to(horror),jest_to(sci_fi).
        jest_to_film(jak_wytresowac_smoka) :- jest_to(animacja),jest_to(familijny),jest_to(dla_dzieci).
        jest_to_film(zodiak) :- jest_to(dramat),jest_to(kryminal),jest_to(thriller).
        jest_to_film(gwiezdne_wojny) :- jest_to(przygodowy),jest_to(sci_fi).
        jest_to_film(czas_na_milosc) :- jest_to(komeida),jest_to(romantyczny).
        jest_to_film(forrest_gump) :- jest_to(komedia),  jest_to(dramat).
        jest_to_film(leon_zawodowiec) :- jest_to(dramat),jest_to(kryminal).
        jest_to_film(requiem_dla_snu) :- jest_to(dramat).
        jest_to_film(matrix) :- jest_to(akcja),jest_to(sci_fi).
        jest_to_film(gladiator) :- jest_to(dramat),jest_to(historyczny).
        jest_to_film(avatar) :- jest_to(sci_fi),jest_to(akcja).
        jest_to_film(shrek) :- jest_to(familijny),jest_to(komedia),jest_to(dla_dzieci),jest_to(animacja).
        jest_to_film(pianista) :- jest_to(historyczny),jest_to(dramat).
        jest_to_film(piraci_z_karaibow) :- jest_to(fantastyka),jest_to(przygodowy),jest_to(familjny).
        jest_to_film(kac_vegas) :- jest_to(komedia).
        jest_to_film(wladca_pierscieni) :- jest_to(fantastyka),jest_to(przygodowy).
        jest_to_film(batman) :- jest_to(sci_fi),jest_to(akcja),jest_to(thriller).
        jest_to_film(truman_show) :- jest_to(dramat),jest_to(komedia),jest_to(sci_fi).
        jest_to_film(krol_lew) :- jest_to(familijny),jest_to(dla_dzieci),jest_to(animacja), jest_to(kryminal).
        jest_to_film(prestiz) :- jest_to(dramat),jest_to(thriller).
        jest_to_film(wilk_z_wall_street) :- jest_to(edukacyjny),jest_to(komedia),jest_to(kryminal), jest_to(historyczny).
        jest_to_film(jestem_legenda) :- jest_to(horror),jest_to(sci_fi),jest_to(dramat).
        jest_to_film(wszystko_za_zycie) :- jest_to(historyczny),jest_to(dramat),jest_to(przygodowy).
        jest_to_film(braveheart) :- jest_to(dramat),jest_to(historyczny).
        jest_to_film(epoka_lodowcowa) :- jest_to(animacja),jest_to(komedia),jest_to(przygodowy), jest_to(familijny).
        jest_to_film(bogowie) :- jest_to(historyczny),jest_to(dramat),jest_to(komedia).
        jest_to_film(chlopaki_nie_placza) :- jest_to(komedia),jest_to(kryminal),jest_to(akcja).
        jest_to_film(whiplash) :- jest_to(dramat),jest_to(muzyczny).
        jest_to_film(amadeus) :- jest_to(historyczny),jest_to(edukacyjny),jest_to(muzyczny).
        jest_to_film(v_for_vendetta) :- jest_to(thriller),jest_to(sci_fi),jest_to(akcja).
        jest_to_film(300) :- jest_to(dramat),jest_to(edukacyjny),jest_to(historyczny).
        jest_to_film(diabel_ubiera_sie_u_prady) :- jest_to(dramat),jest_to(komedia).
        jest_to_film(kill__bill) :- jest_to(thriller),jest_to(akcja).
        jest_to_film(wywiad_z_wampirem) :- jest_to(dramat),jest_to(horror),jest_to(przygodowy).
        jest_to_film(kevin_sam_w_domu) :- jest_to(familijny),jest_to(dla_dzieci),jest_to(komedia).
        jest_to_film(igrzyska_smierci) :- jest_to(akcja),jest_to(sci_fi),jest_to(przygodowy).
        jest_to_film(iron_man) :- jest_to(akcja),jest_to(sci_fi),jest_to(komedia).
        jest_to_film(amelia) :- jest_to(komedia),jest_to(dramat),jest_to(romantyczne).
        jest_to_film(przekret) :- jest_to(komedia),jest_to(kryminal).
        jest_to_film(nienawistna_osemka) :- jest_to(western),jest_to(akcji),jest_to(przygodowy).
        %jest_to(polski):-pozytywne('czy masz ochote na polski film').
        jest_to(akcji):- negatywne(czy_ogladasz_z_dziecmi), pozytywne('czy lubisz gdy sie cos dzieje'), negatywne('czy lubisz sceny walki'), pozytywne('czy masz przekaske').


        jest_to(sci_fi) :- negatywne(czy_ogladasz_z_dziecmi), negatywne(czy_jestes_dzieckiem), pozytywne('czy masz przekaske').

        jest_to(familjny) :- pozytywne('czy ogladasz w wiele osob'), pozytywne(czy_ogladasz_z_dziecmi).

        jest_to(komedia) :- pozytywne('czy ogladasz w wiele osob'),  pozytywne('czy chcesz sie zrelaksowac').

        jest_to(dramat) :- negatywne('czy ogladasz w wiele osob').

        jest_to(dla_dzieci) :- pozytywne('czy jestes rodzicem'), pozytywne(czy_ogladasz_z_dziecmi), negatywne('czy lubisz przemoc').
        jest_to(dla_dzieci) :- pozytywne(czy_jestes_dzieckiem), negatywne('czy lubisz przemoc').


        jest_to(edukacyjny) :- negatywne('czy lubisz gdy sie cos dzieje'), pozytywne('czy film ma cie czegos nauczyc').

        jest_to(romantyczne) :- pozytywne('czy jestes kobieta'), negatywne('czy masz dobry humor'), pozytywne(' czy latwo cie wystraszyc').
        jest_to(romantyczne) :- pozytywne('czy ogladasz z dziewczyna'), negatywne('czy ogladasz w wiele osob'), pozytywne('czy ogladasz wieczorem'), pozytywne('czy masz dobry humor').

        jest_to(fantastyka) :- pozytywne('Czy grasz w gry'), pozytywne('czy ogladasz w wiele osob'), pozytywne('czy lubisz sceny walki').

        jest_to(historyczny) :- negatywne('czy ogladasz w wiele osob'), pozytywne('czy masz wyksztalcenie wyzsze'), negatywne(czy_ogladasz_z_dziecmi), pozytywne('czy film ma cie czegos nauczyc').

        jest_to(dokumentalny) :-  pozytywne('czy film ma cie czegos nauczyc').

        jest_to(katastroficzny) :- negatywne(czy_ogladasz_z_dziecmi), pozytywne('czy ogladasz wieczorem'), negatywne('czy latwo cie wystraszyc'), pozytywne('czy ogladasz z dziewczyna').

        jest_to(muzyczny) :- pozytywne('czy jestes kobieta'), pozytywne('Czy latwo sie wzruszasz').

        jest_to(przygodowy) :- pozytywne('czy chcesz sie zrelaksowac').

        jest_to(sportowy) :- pozytywne('czy uprawiasz sport'), negatywne('czy jestes kobieta').

        jest_to(animacja) :-  pozytywne('czy chcesz sie zrelaksowac').

        jest_to(thriller) :- negatywne(czy_ogladasz_z_dziecmi), negatywne(czy_jestes_dzieckiem), pozytywne('czy chcesz ogladac film dlugometrazowy'), pozytywne('czy lubisz gdy sie cos dzieje'), pozytywne('czy masz przekaske').

        jest_to(western) :- negatywne('czy jestes kobieta'), negatywne('czy ogladasz z dziewczyna'), pozytywne('czy lubisz stare filmy'), pozytywne('czy chcesz ogladac film dlugometrazowy').

        jest_to(horror) :- negatywne(czy_ogladasz_z_dziecmi), pozytywne('czy ogladasz wieczorem'), negatywne('czy latwo cie wystraszyc'), negatywne('czy ogladasz w wiele osob'), negatywny('czy chcesz sie zrelaksowac'), negatywne(czy_jestes_dzieckiem).
        jest_to(horror) :- pozytywne('czy ogladasz wieczorem'), pozytywne('czy latwo cie wystraszyc'), pozytywne('czy ogladasz z dziewczyna'), negatywne('czy ogladasz w wiele osob'), negatywne(czy_jestes_dzieckiem).

        jest_to(kryminal) :- pozytywne('czy lubisz watki kryminalne').




        pozytywne(X) :- xpozytywne(X), !.

        pozytywne(X) :- \+xnegatywne(X), !, pytaj(X).

        negatywne(X) :- xnegatywne(X), !.

        negatywne(X) :- \+xpozytywne(X),!, pytaj(X).



        pamietaj(X,tak) :- assertz(xpozytywne(X)),format('pamietaj tak ~w', [X]).
        pamietaj(X,nie) :- assertz(xnegatywne(X)),format('pamietaj nie').
