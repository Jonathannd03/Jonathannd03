class User():
    def __init__(self, vorname, nachname, alter, staatangehörigkeit, status, geschlecht):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.staatangehörigkeit = staatangehörigkeit
        self.status = status
        self.geschlecht = geschlecht
        self.login_attempts = 0


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

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.vorname, 'hat versuch, sich', self.login_attempts, 'mal anzumelden.')
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        print('Die Anmeldeversuche sind zurückgesetzt worden', self.login_attempts)
        return self.login_attempts

user1 = User('Jonathan', 'Ndinga', '24', 'Kongolesich', 'single', 'M')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()



user2 = User('Hannah', 'Konyietny', '26', 'Deutsche', 'verlobt', 'W')
user2.describe_user()
user2.greet_user()

user3 = User('Patient', 'Musafiri', '27', 'Kongolesich', 'verlobt', 'M')
user3.describe_user()
user3.greet_user()

user4 = User('Gloria', 'Green', '23', 'ugandan', 'verheiratet', 'W')
user4.describe_user()
user4.greet_user()
