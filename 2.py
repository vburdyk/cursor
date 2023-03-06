class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return str(list(self.__dict__))


profile = Profile("Vasya", "Lolam", "0666005868", "Zolochiv", "vasya@gmail.com", "14/01/2004", 18, "male")
print(profile)

