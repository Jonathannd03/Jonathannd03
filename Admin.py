class User():
    def __init__(self, vorname, nachname, alter, staatangehörigkeit, status, geschlecht):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.staatangehörigkeit = staatangehörigkeit
        self.status = status
        self.geschlecht = geschlecht


    def describe_user(self):
        print('\nVorname: ', self.vorname)
        print('Nachname: ', self.nachname)
        print('Alter: ', str(self.alter), 'Jahre alt')
        print('Staatangehörigkeit: ', self.staatangehörigkeit)
        print('Status: ', self.status)
        print('Geschlecht: ', self.geschlecht)

    def greet_user(self):
        if self.geschlecht == 'M':
            print('\nHerzlich Willkommen','\nWir freuen uns '
                                    'Herr', self.vorname, self.nachname, 'begrüßen zu dürfen')
        else:
            print('\nHerzlich Willkommen', '\nWir freuen uns '
                                           'Frau', self.vorname, self.nachname, 'begrüßen zu dürfen')

class Admin(User):
    def __init__(self, vorname, nachname, alter, staatangehörigkeit, status, geschlecht):
        User.__init__(self, vorname, nachname, alter, staatangehörigkeit, status, geschlecht)
        self.privileges = ['er kann Beitrag einfügen', 'er kann Beitrag löschen', 'er kann dir sperren']

    def show_privileges(self):
        print('\nDies sind die Admin-Rechte von', self.vorname, 'als Admin:')
        for privilege in self.privileges:
            print(privilege)

admin = Admin('Jonathan', 'Ndinga', '24', 'Kongolesich', 'single', 'M')

print(admin.show_privileges())