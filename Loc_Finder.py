from geopy.geocoders import Nominatim


#create GeoLocator Object with user Agent
geolocator = Nominatim(user_agent= "geoapiExercises")

#Get Continously location
while True:
    # Get City Name 
    place: str = input("Enter Your City: ")
    try:
        # GeoCode the Location
        location = geolocator.geocode(place)
        zip_code = location.address
        #Print Location Detail
        print(location)
    except AttributeError:
        print('There is Something Wrong...!')
        continue


