import json
from constants.messages import CustomMessages
from helpers.regex_helper import RegexHelper
from model.user import User

class FileHelper:
    
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
                    user.country = data["profile"]["address"].split()[-1]
                    user.birth_day = data["profile"]["dob"][:8]
                    user.birth_month = data["profile"]["dob"][5:7]
                    user.birth_year = data["profile"]["dob"][0:4]
                    user.usernamelk = self.isUsernamelk(user.username, user.name_surname)

                    userList.append(user)
        except:
            print(CustomMessages.JSON_FILE_ERROR)

        return userList


    def getBirthDay(self,date):
        pass
    def getCountry(self, latitude, longitude):
        #TODO: will be added service
        pass


    def isEmailuserlk(self, name_surname, username):
        pass
        


    def isUsernamelk(self, username, name_surname):
        regexHelper = RegexHelper()
        name_surname = name_surname.lower().replace(" ","")
        name = regexHelper.parseUsername(username)

        return "1" if name == name_surname[:len(name)] else "0"


        
       