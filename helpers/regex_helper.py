import re

class RegexHelper:

    def parseEmail(self, email):
        """ This method parses email and extract name and surname 
            according the given pattern and returns all info into
            dictionary.

            param: <str> email
            return: <dict> email_info
        """
        email_info = dict()
        
        pattern =  re.compile(r"([a-zA-Z]+)[\.-_]*([a-zA-Z]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
        match = pattern.search(email)

        email_info["name"] = match.group(1)
        email_info["surname"] = match.group(2)

        return email_info

    def parseUsername(self, username):
        """ This method parses surname and extract name 
            according the given pattern and returns 
            a string.

            param: <str> username
            return: <str> match
        """
        pattern = re.compile(r"[A-Za-z]+")
        match = pattern.search(username).group()

        return match

    def parseBirthDate(self, date):
        """ This method parses surname and extract name 
            according the given pattern and returns 
            a string.

            param: <str> username
            return: <str> match
        """
        birthDate = dict()
        pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
        match = pattern.search(date)

        birthDate["year"] = match.group(1)
        birthDate["month"] = match.group(2)
        birthDate["day"] = match.group(3)

        return birthDate
