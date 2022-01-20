import json
from constants.messages import CustomMessages
from helpers.location_helper import LocationHelper
from helpers.regex_helper import RegexHelper
from model.user import User

class FileHelper:
    regexHelper = RegexHelper()
    locationHelper = LocationHelper()
    
    def scrapJsonFile(self, path):
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
                    user.birth_day = self.getBirthDay(data["profile"]["dob"])
                    user.birth_month = self.getBirthMonth(data["profile"]["dob"])
                    user.birth_year = self.getBirthYear(data["profile"]["dob"])
                    user.usernamelk = self.isUsernamelk(user.username, user.name_surname)
                    
                    userList.append(user)
        except:
            print(CustomMessages.JSON_FILE_ERROR)

        return userList


    def getBirthDay(self,date):
        day = self.regexHelper.parseBirthDay(date)
        return day
    
    def getBirthMonth(self,date):
        month = self.regexHelper.parseBirthMonth(date)
        return month

    def getBirthYear(self,date):
        year = self.regexHelper.parseBirthYear(date)
        return year

    def getCountry(self, latitude, longitude):
        country = self.locationHelper.getLocation(latitude, longitude)
        return country

    def isEmailuserlk(self, name_surname, username):
        pass
        
    def isUsernamelk(self, username, name_surname):
        name_surname = name_surname.lower().replace(" ","")
        name = self.regexHelper.parseUsername(username)

        return "1" if name == name_surname[:len(name)] else "0"


        
       