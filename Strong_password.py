# checking a password strong or not
import re

def password(inputs):

    Check_eight_characeterLong = re.compile(r'[\d\s\w\D\S\W]{8,}')
    Upper_case_letter = re.compile(r'[A-Z]+')
    Lower_case_Letter = re.compile(r'[a-z]+')
    One_complex_term = re.compile(r'[\d]+')

    # or the expression can be r'(?={8,})(?=.*\d)(?=.*\d)'

    if not Check_eight_characeterLong.search(inputs) : # or condition == False means if we get less then 8 we get our condition trye infact result will be false

        return False

    elif not Upper_case_letter.search(inputs):
        return False
    elif not Lower_case_Letter.search(inputs):
        return False
    elif not One_complex_term.search(inputs):
        return False

    return True

Type_password = input() #A&dsas9$_%6..
print(''+str(password(Type_password)))
