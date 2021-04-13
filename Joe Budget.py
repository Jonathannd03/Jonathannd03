print('\tWillkommen in Joe_Budget \n\tIhr persönlicher spesenberater'.upper())
print('\tWollen Sie die von uns vorgesclagenen Regelugen nutzen oder '
      '\n\tIhre eigene Regelung hinzufügen?'.upper())
auswahl =input('\n\tGeben Sie 1 für die Joe-Budget Regelungen und '
      '\n\t2 um Ihre eigenen hinzufügen: '.upper())
if auswahl == '1' or auswahl == 'Eins' or auswahl == 'eins' or auswahl == 'EINS':
    print('\tDie erste Regelung besteht aus einer 50-30-20 Gehaltsverteilung'.upper())
    print('\t50% Bedürfnisse, 30% Wünsche und 20% Einsparungen'.upper())
    print('\tDie zweite Regelung besteht aus einer 50-20-30 Gehaltsverteilung'.upper())
    print('\t50% Bedürfnisse, 20% Wünsche und 30% Einsparungen'.upper())
    gehalt = 1
    ergebnis = 0

    regelung =input('\tWählen Sie eine Regelung aus: ')
    if regelung == 'erste' or regelung == '1' or regelung == 'Erste' or regelung == 'ERSTE':
        print('\tSie haben die 50-30-20 Reglung ausgewählt')
        def joe_budget(gehalt):

            if gehalt > 0:
                ergebnis= (gehalt * 50) /100
                print('\tEntsprechend Ihrem Nettogehalt haben Sie', ergebnis,
                      'Euro oder 50% Ihres Gehaltes, um Ihren gesamten Bedarf für diesen Monat zu decken.')
                if gehalt > 0:
                    ergebnis= (gehalt * 30) /100
                    print('\tEntsprechend Ihrem Nettogehalt haben Sie', ergebnis,
                      'Euro oder 30% Ihres Gehaltes, um Ihren Wünschen für diesen Monat zu decken.')
                    if gehalt > 0:
                        ergebnis = (gehalt * 20) / 100
                        print('\tEntsprechend Ihrem Nettogehalt müssen Sie ', ergebnis,
                              'Euro oder 20% Ihres Gehaltes für Ihre Ersparnisse einbehalten oder investieren.')
                        print('\tdanke für Ihr Vertrauen in Joe-Budget wir wünschen Ihnen einen gesegneten Monat :)'.upper())
        print(joe_budget(float(input('\tGeben Sie Ihr monatliches Gehalt ein(Netto Betrag): '))))
    elif regelung == 'zweite' or regelung == 'Zwiete' or regelung == '2' or regelung == 'ZWEITE':
        print('\tSie haben die 50-20-30 Regelung ausgewählt')
        def joe_budget(gehalt):

            if gehalt > 0:
                ergebnis= (gehalt * 50) /100
                print('\tEntsprechend Ihrem Nettogehalt haben Sie', ergebnis ,
                      'Euro oder 50% Ihres Gehaltes, um Ihren gesamten Bedarf für diesen Monat zu decken.')
                if gehalt > 0:
                    ergebnis= (gehalt * 20) /100
                    print('\tEntsprechend Ihrem Nettogehalt haben Sie', ergebnis,
                      'Euro oder 30% Ihres Gehaltes, um Ihren Wünschen für diesen Monat zu decken.')
                    if gehalt > 0:
                        ergebnis = (gehalt * 30) / 100
                        print('\tEntsprechend Ihrem Nettogehalt müssen Sie ', ergebnis,
                              'Euro oder 30% Ihres Gehaltes für Ihre Ersparnisse einbehalten oder investieren.')
                        print('\tdanke für Ihr Vertrauen in Joe-Budget wir wünschen Ihnen einen gesegneten Monat :)'.upper())
        print(joe_budget(float(input('\tGeben Sie Ihr monatliches Gehalt ein(Netto Betrag): '))))

    else:
        print('\tSie haben eine Falsche Regelung ausgewählt')
        print('\tdanke für Ihr Vertrauen in Joe-Budget wir wünschen Ihnen einen gesegneten Monat :)'.upper())
elif auswahl == '2' or auswahl == 'Zwei' or auswahl == 'ZWEI' or auswahl == 'zwei':
    print('\tHier Können Sie Ihre eingene Regelung hinzufügen'.upper())
    gehlt = 0
    ergb = 0
    total = 0
    rest = 0
    while total !=100:
        bedürfnisse_prozent = int(
            input('\tWelcher Prozentsatz Ihres Gehalts sollte für die Bedürfnisse verwendet werden: '.upper()))
        wünsche_prozent = int(
            input('\tWelcher Prozentsatz Ihres Gehalts sollte für die Wünsche verwendet werden: '.upper()))
        einsparungen_prozent = int(input('\tWelcher Prozentsatz Ihres Gehalts sollte eingespart werden: '.upper()))
        total = bedürfnisse_prozent + wünsche_prozent + einsparungen_prozent
        if total != 100:
            print('\tIhr gemeisamer Prozentsatz soll nicht höher als 100 sein'
                  '\n\tLaut Ihre Eingabe ist ihre gemeisamer  Prozentsatz  '.upper(), total, '%')
        else:
            def benuzter_budget(gehlt):
                if gehlt > 0:
                    ergb = (gehlt * bedürfnisse_prozent) / 100
                    print('\tEntsprechend Ihrem Nettogehalt haben Sie', ergb,
                          'Euro oder', bedürfnisse_prozent,
                          end='' ' %Ihres Gehaltes, um Ihren gesamten Bedarf für diesen Monat zu decken.')
                    if gehlt > 0:
                        ergb = (gehlt * wünsche_prozent) / 100
                        print('\n\tEntsprechend Ihrem Nettogehalt haben Sie', ergb,
                              'Euro oder', wünsche_prozent, end=''
                                                                '% Ihres Gehaltes, um Ihren gesamten Bedarf für diesen Monat zu decken.')
                        if gehlt > 0:
                            ergb = (gehlt * einsparungen_prozent) / 100
                            print('\n\tEntsprechend Ihrem Nettogehalt haben Sie', ergb,
                                  'Euro oder', einsparungen_prozent, end=''
                                                                         '% Ihres Gehaltes, um Ihren gesamten Bedarf für diesen Monat zu decken.')
                            print(
                                '\n\tdanke für Ihr Vertrauen in Joe-Budget wir wünschen Ihnen einen gesegneten Monat :)'.upper())


    print(benuzter_budget(float(input('\n\tGeben Sie Ihr monatliches Gehalt ein(Netto Betrag): '.upper()))))
else:
    print('\tSie haben einen falschen Ziffer eigegeben'
          '\n\tGeben Sie 1 für die Joe-budget regelungen oder 2 um ihre eigenen hinzufügen'
          '\n\tdanke für Ihr Vertrauen in Joe-Budget wir wünschen Ihnen einen gesegneten Monat :)'.upper())





