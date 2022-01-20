from geopy.geocoders import Nominatim
 
# # calling the nominatim tool
# geoLoc = Nominatim(user_agent="GetLoc")
 
# # passing the coordinates
# locname = geoLoc.reverse("26.7674446, 81.109758")
 
# # printing the address/location name
# print(locname.address)

class LocationService:
    
    def getLocation(self):
        geoLocation = Nominatim(user_agent="GetLoc")
        locname = geoLocation.reverse("42.7674446, 10.109758")
        country = locname.address().split()[:-1]
 
# printing the address/location name
        print(country)

