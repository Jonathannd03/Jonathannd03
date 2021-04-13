import build_profiles as bp

user_profile = bp.build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)

print('\n')

user_profile1 = bp.build_profile('Jonathan', 'Ndinga', Straße='Oberlöricker', Hausnummer='321', PLZ='40547')
print(user_profile1)