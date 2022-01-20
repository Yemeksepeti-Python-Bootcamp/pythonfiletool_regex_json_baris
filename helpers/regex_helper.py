import re

class RegexHelper:

    def parseEmail(self, email):
        """ Parses email and extract name and surname """

        pattern =  re.compile(r"([a-zA-Z]+)[\.-_]*([a-zA-Z]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
        match = pattern.search(email)
        name_from_email = match.group(1)
        surname_from_email = match.group(2)

        return [name_from_email, surname_from_email]

    def parseUsername(self, username):
        pattern = re.compile(r"[A-Za-z]+")
        match = pattern.search(username)

        return match.group()

    def parseBirthDate(self, date):
        birthDate = dict()
        pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
        match = pattern.search(date)

        birthDate["year"] = match.group(1)
        birthDate["month"] = match.group(2)
        birthDate["day"] = match.group(3)

        return birthDate

    
    # def parseBirthYear(self, date):
    #     pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
    #     match = pattern.search(date)

    #     return match.group(1)
    
    # def parseBirthMonth(self, date):
    #     pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
    #     match = pattern.search(date)

    #     return match.group(2)
    
    # def parseBirthDay(self, date):
    #     pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
    #     match = pattern.search(date)

    #     return match.group(3)
