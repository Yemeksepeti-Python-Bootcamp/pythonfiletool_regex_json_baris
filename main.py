from constants.messages import CustomMessages
from model.user import User
from helpers.file_helper import FileHelper
from helpers.database_helper import DatabaseHelper

def main(file = None, db = None):
    
    if (file is not None) and (db is not None): # checks the parameters are given or not

        jsonFileTool = FileHelper() # jsonfileTool for scraping the JSON file
        databaseHelper = DatabaseHelper(db) # for creating the database 

        userInfoList = jsonFileTool.scrapJsonFile(file) # scraps the json file and returns all information as a list
        databaseHelper.createTable() # for creating the database table

        for user_info in userInfoList: # insert the all user data from userInfoList to the database table
            databaseHelper.insertData(user_info)
    else:
        print(CustomMessages.PARAMETER_ERROR) # if the parameters are not given raise exception


if __name__ == "__main__":

    file = "dataregex.json"
    db = "dataregex.db"

    main(file,db) # calss the main function
