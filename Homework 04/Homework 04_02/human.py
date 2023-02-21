""" Module of human class"""


class Human:
    def __init__(self, name: str = 'Name', surname: str = 'Surname', age: int = 18, born: str = '2006',
                 cellphone: str = 'XXXXXXXXXX', email: str = 'mail@domain.com'):
        if not isinstance(age, int):
            raise TypeError()

    # maybe better if all attributes was 'protected' and using setters and getters methods instead to work with them?
        self.name = name
        self.surname = surname
        self.age = age
        self.born = born
        self.cellphone = cellphone
        self.email = email

    def __str__(self):
        return f'\nName: {self.name}' \
               f'\nsurname: {self.surname}' \
               f'\nBorn: {self.born} ' \
               f'\nCellphone: {self.cellphone}' \
               f'\nEmail: {self.email}'
