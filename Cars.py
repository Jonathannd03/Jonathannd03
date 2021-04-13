def auto_herstellung(hersteller,auto_modelle,**infos):
    print('\nInfos zum folgenden Auto:')
    cars = {}
    cars['hersteller_name'] = hersteller
    cars['modelle_name'] = auto_modelle
    for key, value in infos.items():
        cars[key] = value
    return cars

car = auto_herstellung('subaru','Outback', farbe='blau', tow_package=True)
print(car)