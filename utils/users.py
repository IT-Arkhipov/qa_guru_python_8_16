from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    date: str
    checked_date: str
    subject: str
    hobby: str
    file_name: str
    address: str
    state: str
    city: str


user = User(
    first_name='FirstName',
    last_name='LastName',
    email='mymail@test.ru',
    gender='Male',
    phone='9170770905',
    date='11 Oct 2023',
    checked_date='11 October,2023',
    subject='Maths',
    hobby='Sports',
    file_name='sample.jpg',
    address='My address',
    state='NCR',
    city='Delhi'
)
