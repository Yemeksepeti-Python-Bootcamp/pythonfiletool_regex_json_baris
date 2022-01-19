import re

from numpy import mat

class RegexHelper:
    
    def parseUsername(self, username):
        pattern = re.compile(r"[A-Za-z]+")
        match = pattern.search(username)

        return match.group()
    
    def parseBirthYear(self, date):
        pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
        match = pattern.search(date)

        return match.group(1)
    
    def parseBirthMonth(self, date):
        pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
        match = pattern.search(date)

        return match.group(2)
    
    def parseBirthDay(self, date):
        pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
        match = pattern.search(date)

        return match.group(3)
