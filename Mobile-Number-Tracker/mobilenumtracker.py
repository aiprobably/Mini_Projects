#Importing all the neccessary Modules
import phonenumbers
from phonenumbers import geocoder,timezone,carrier
from opencage.geocoder import OpenCageGeocode
import folium
​
#API key for the Map
Key='80ad334ec5784c32913ff5a423a1255d'
​
#Taking input of phone number from the user
number=input("Enter a phone number")
phone_number= phonenumbers.parse(number)
​
#Validating the phone number
valid=phonenumbers.is_valid_number(phone_number)
possible=phonenumbers.is_possible_number(phone_number)
​
#Finding the Phone Number's Carrier,Location and timezone
if ((valid and possible)== True):
    Carrier=carrier.name_for_number(phone_number,'en')
    Region= geocoder.description_for_number(phone_number,'en')
    timeZone = timezone.time_zones_for_number(phone_number)
​
    print(Carrier)
    print(Region)
    print(timeZone)
    
    #Finding the latitude and longitude of the phone number
    #using the API key
    geocoder = OpenCageGeocode(Key)
    query= str(Region)
    
    Result= geocoder.geocode(query)
    lat = Result[0]['geometry']['lat']
    lng= Result[0]['geometry']['lng']
    print("The latitude and longitude are:",'[',lat,',',lng,']')
​
    #Locating the latitude and longitude on a map
    myMap=folium.Map(location=[lat,lng], zoom_start=5)
    folium.Marker([lat,lng],popup=Region).add_to(myMap)
​
    #Saving the map to a HTML Page
    myMap.save('yourLocation.html')
​
else: 
    print("Try again with a valid number")
