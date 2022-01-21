from geopy.geocoders import Nominatim
from constants.messages import CustomMessages

class LocationHelper:

    def getLocation(self, latitude, longitude):
        """ This method takes the location information
            from the geopy package  and returns 
            the country name as a string

            param: <str> latitude, <str> longitude
            return: <str> country
        """
        try:
            geoLoc = Nominatim(user_agent="GetLoc")
            locname = geoLoc.reverse(f"{latitude}, {longitude}")
            country = str(locname.address).split()[-1]
            
            return country
            
        except:
            print(CustomMessages.LOCATION_ERROR)



