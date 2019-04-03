# Testovacie scenáre pre predmet ITS (OpenCart platforma)  <br> Tomáš Sasák  - 2018/2019
Testovacia sada obsahuje 5 feature súborov. Každý súbor popisuje jeden element, OpenCart e-shopu. Zoznam súborov .feature:
* Admin
* Cart
* Offer
* Overall
* User

## Sada Admin
Sada testuje vlastnosti administratorského panelu, vlastnosti sú následujúce:
* Prihlasovanie do admin účtu
* Odhlasovanie z admin účtu
* Zobrazenie všetkých registrovaných zákazníkov
* Zobrazenie všetkých objednávok

## Sada Cart
Sada testuje vlastnosti nákupného košíku, testované vlastnosti sú následujúce:
* Uživatel pridáva položky do prázdneho košíku
* Uživatel pridáva položky do neprázdneho košíku
* Uživatel pridáva položky do košíku z okamžitej ponuky, na hlavnej stránke

## Sada Offer
Sada testuje vlastnosti ponuky sortimentu (zoznam), testované vlastnosti sú nasledujúce:
* Zobrazenie zoznamu sortimentu, danej kategórie

## Sada Overall
Sada testuje všeobecné vlastnosti e-shopu, testované vlastnosti sú nasledujúce:
* Prístup na stránku a plné načítanie e-shopu
* Zmena meny, v ktorej sú dané ceny
* Vytvorenie objednávky

## Sada User
Sada testuje vlastnosti uživatela e-shopu, testované vlastnosti sú nasledujúce:
* Správna registrácia uživateľa
* Nesprávna registrácia uživateľa (neplatné údaje)
* Nesprávna registrácia uživateľa (nesúhlas s privacy policy)
* Správne prihlásenie do zákaznického účtu
* Nesprávne prihlásenie do zákaznického účtu (neplatné údaje)
* Správna zmena hesla
* Nesprávna zmena hesla (moc krátke heslo)