import re

class RegexHelper:
    
    def parseUsername(self, username):
        pattern = re.compile(r"[A-Za-z]+")
        match = pattern.search(username)

        return match.group()