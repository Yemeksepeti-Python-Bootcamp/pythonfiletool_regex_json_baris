import json
from constants.messages import CustomMessages
from helpers.location_helper import LocationHelper
from helpers.regex_helper import RegexHelper
from model.user import User

class FileHelper:
    regexHelper = RegexHelper()
    locationHelper = LocationHelper()
    
    def scrapJsonFile(self, path):
        """ This method scraps the json file
            and returns the all info as a List

            param: <str> path
            return: <list> userList
        """
        userList = list()
        try:
            with open(path) as jsonFile:
                allJsonDatas = json.load(jsonFile)

                for data in allJsonDatas:
                    user = User()

                    user.email = data["email"]
                    user.username = data["username"]
                    user.name_surname = data["profile"]["name"]

                    user.country = self.getCountry(data["profile"]["location"]["lat"], data["profile"]["location"]["long"])

                    user.birth_day = self.getBirthInfo(data["profile"]["dob"])["day"]
                    user.birth_month = self.getBirthInfo(data["profile"]["dob"])["month"]
                    user.birth_year = self.getBirthInfo(data["profile"]["dob"])["year"]

                    user.usernamelk = self.isUserNamelk(user.username, user.name_surname)
                    user.emailuserlk = self.isEmailUserlk(user.email, user.username)

                    userList.append(user)
        except:
            print(CustomMessages.JSON_FILE_ERROR)

        return userList

    def getBirthInfo(self,date):
        """ This method takes the parsing information
            from the regex method and returns it

            param: <str> date
            return: <str> birthDate
        """
        birthDate = self.regexHelper.parseBirthDate(date)
        return birthDate

    def isEmailUserlk(self, email, username):
        """ This method takes the parsing information
            from the regex method and checks the whether
            the user's email does contain the user's username.
            If yes returns 1, otherwise return 0 as a string

            param: <str> email, <str> username
            return: <str> 1 or 0
        """
        username = self.regexHelper.parseUsername(username)
        email_info = self.regexHelper.parseEmail(email)

        return "1" if username in email_info.values() else "0"
        
    def isUserNamelk(self, username, name_surname):
        """ This method takes the parsing information
            from the regex method and checks the whether
            the user's name and surname does contain the user's 
            username. If yes returns 1, otherwise return 0 as a string

            param: <str> username, <str> name_surname
            return: <str> 1 or 0
        """
        name_surname = name_surname.lower().split()
        name = self.regexHelper.parseUsername(username)

        return "1" if name in name_surname else "0"

    def getCountry(self, latitude, longitude):
        """ This method takes the location information
            from the getLocation method and and returns 
            the country name as a string

            param: <str> latitude, <str> longitude
            return: <str> country
        """
        country = self.locationHelper.getLocation(latitude, longitude)
        return country


        
       