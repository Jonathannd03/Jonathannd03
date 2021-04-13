versicherungart = input("Geben Sie die Versicherungsart ein: ")
arzneinmittelart = input("Geben Sie die Arzneinmittelárt ein: ")

def rezept_verwaltung(versicherungsart, arzneinmittelart):
    if versicherungart == "gesetzlich" and arzneinmittelart == "verschreibungsplichtiges":
        print("Rosa")

    elif versicherungart == "gesetzlich" and arzneinmittelart == "nicht verschreibungsplichtiges":
        print("Grün")

    elif versicherungart == "privat" and arzneinmittelart == "verschreibungsplichtiges" or "vp"\
            or "nicht verschreibungsplichtiges" or "nvp":
        print("blau")

    elif versicherungart == "gesetzlich" or "g" or "privat" or "p" and \
            arzneinmittelart == "verschreibungsplichtiges" or "nvp" or "betäubungsmittel":
        print("Gelb")

rezept_verwaltung(versicherungart,arzneinmittelart))