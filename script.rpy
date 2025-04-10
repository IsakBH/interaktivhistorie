define t = Character("Trollius the Malevolent", color="#ff0000")
define e = Character("Isus Kristonius", color="#2C7ED4")
define p = Character("Du", color="#FFD700")

image isus happy = "images/isus_happy.png"
image isus serious = "images/isus_serious.png"
image isus determined = "images/isus_determined.png"
image isus victorious = "images/isus_victorious.png"
image victory_isus = "images/victory_isus.png"

image trollius happy = "images/trollius_happy.png"
image trollius angry = "images/trollius_angry.png"
image trollius scheming = "images/trollius_scheming.png"
image trollius victorious = "images/trollius_victorious.png"
image victory_trollius = "images/victory_trollius.png"


label start:

    scene bg room

    show isus happy at Transform(yalign=0.1)
    e "Det var en gang en utvikler som het Isak. En natt kjedet han seg veldig og hadde lyst til å lage et tekstbehandlingsprogram. Han satt ut på eventyret som nå er vel kjent som Ord på Nett, som du som leser dette også bør bruke ;)"

    e "Ord på Nett ble raskt en 'hit' rundt om i hele verden og er nå den største konkurrenten til både Google Docs og Microsoft Word. Den vise profeten Isus Kristonius skal snakke om dette vidunderlige produktet på rådhusplassen i morgen."

    scene bg town_square
    show isus serious at Transform(yalign=0.1)

    e "Mine venner! Vi har samlet oss her i dag for å hylle fri tekstredigering uten proprietære lenker som binder oss til onde selskaper!"

    show trollius angry at Transform(xalign=1.0, yalign=0.1)

    t "Hah! Dere naive sjeler! Dere tror at et gratis og åpent tekstverktøy kan eksistere uten å bøye seg for makten til de store teknologiselskapene? Jeg, Trollius den Ondskapsfulle, vil gjøre slutt på dette nonsenset!"

    e "Trollius! Din tid med ondskap er over! Ord på Nett er bygget på kjærlighet, frihet og et ønske om at alle skal kunne skrive uten hindringer!"

    t "Vi får se med det! Se på denne koden jeg har skrevet!"

    t "Med denne onde PHP-injeksjonen skal jeg ødelegge databasen deres og gjøre alle dokumentene uleste!"

    p "Dette ser ut til å bli en kamp mellom godt og ondt... men hvilken side skal jeg velge?"

    menu:
        "Støtt Isus Kristonius og forsvare åpen kildekode":
            jump support_isus
        "Støtt Trollius den Ondskapsfulle og hjelpe til med å ødelegge Ord på Nett":
            jump support_trollius

label support_isus:

    show isus determined at Transform(yalign=0.1)

    p "Jeg kan ikke la Trollius vinne! Frihet i tekstbehandling er for viktig!"

    e "Jeg visste du ville gjøre det rette! Men hvordan skal vi stoppe ham?"

    menu:
        "Bruk kraften av lynrask bugfixing":
            jump bugfixing
        "Kall på open-source samfunnet for hjelp":
            jump open_source_help
        "Implementer en hellig rollback-funksjon":
            jump rollback_function

label bugfixing:

    e "Med mine hellige fingre skal jeg fjerne all ondsinnet kode!"

    "Isus Kristonius skriver kode raskere enn noen har sett før. Alle feilene i systemet blir rettet på sekunder."

    t "Nei! Hvordan er dette mulig?!"

    e "Ingen bug står imot kraften av fri kildekode!"

    jump victory_isus

label open_source_help:

    e "Vi må stå sammen! Jeg kaller på alle bidragsytere av fri programvare!"

    "Plutselig dukker tusenvis av utviklere opp, klare til å reversere skaden Trollius har gjort."

    t "Nei! Ikke fellesskapet! Min eneste svakhet!"

    jump victory_isus

label rollback_function:

    e "Ingen problem! Jeg aktiverer rollback-systemet!"

    "Isus trykker på en knapp, og hele databasen blir rullet tilbake til en tidligere versjon før Trollius rakk å gjøre skade."

    t "Hva!? NEI! Dette er juks!"

    jump victory_isus

label victory_isus:

    hide trollius
    show isus victorious at Transform(yalign=0.1)

    e "Enda en dag er reddet, og Ord på Nett vil fortsette å være fritt for alle!"

    p "Friheten vant! Jeg vil fortsette å bruke Ord på Nett og spre budskapet!"

    return

label support_trollius:

    show trollius scheming at Transform(xalign=1.0, yalign=0.1)

    p "Hmmm... Kanskje Trollius har et poeng? Kanskje jeg burde stå på hans side?"

    t "Endelig noen med fornuft! Sammen skal vi ødelegge dette tullete fritekst-prosjektet!"

    "Men hvordan skal vi gjøre det?"

    menu:
        "DDoS-angrep mot serverne":
            jump ddos_attack
        "Ondskapens lisensavtale":
            jump evil_license
        "Kode et proprietært virus":
            jump evil_virus

label ddos_attack:

    "Du og Trollius starter et massivt DDoS-angrep mot Ord på Nett."

    e "Nei! Brukerne kan ikke logge inn!"

    t "Mwahaha! Nå må de bruke Google Docs i stedet!"

    jump victory_trollius

label evil_license:

    "Trollius sniker inn en ondsinnet lisensavtale i kildekoden."

    e "Hva er dette?! Brukere må betale en månedlig avgift for å bruke lagringsfunksjonen?!"

    t "Mwahaha! Snart vil ingen bruke det gratis!"

    jump victory_trollius

label evil_virus:

    "Du koder et virus som infiltrerer alle dokumenter og gjør dem uleselige."

    e "Nei! Alle filene er nå fylt med reklame for Microsoft Word!"

    t "Hahaha! Ord på Nett er ødelagt!"

    jump victory_trollius

label victory_trollius:

    show trollius victorious at Transform(xalign=1.0, yalign=0.1)

    t "Mwahaha! La dette være en lærepenge for alle som tror på fri programvare!"

    return
