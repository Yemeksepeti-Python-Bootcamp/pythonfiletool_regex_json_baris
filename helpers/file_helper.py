import json
from constants.messages import CustomMessages
from model.User import User

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

                    userList.append(user)
        except:
            print(CustomMessages.JSON_FILE_ERROR)

        return userList

    def isEmailuserlk(self, email, username):
        #TODO: controls will be added
        pass

    def isUsernamelk(self, username, name_surname):
        #TODO: controls will be added
        pass

        
       