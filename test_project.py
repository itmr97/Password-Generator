from project import generate_password
import string

def test_generate_password():

    assert generate_password(5, numbers=True, special_characters=False,lower=False,upper=False).isdigit()

def test_generate_password2():

    assert generate_password(45, numbers=True, special_characters=False,lower=True,upper=False).isalnum()
    assert generate_password(9, numbers=True, special_characters=False,lower=True,upper=True).isalnum()

def test_generate_password3():
     assert generate_password(20, numbers=False, special_characters=False,lower=True,upper=False).islower()
     assert generate_password(20, numbers=False, special_characters=False,lower=False,upper=True).isupper()
