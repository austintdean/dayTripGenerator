# (5 points): As a developer, I want to make at least three commits with descriptive messages.
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation,
# and entertainments in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of
# transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all
# of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember,
# each function should do just one thing!
import random 

locations = ['Chicago', 'San Diego', 'London', 'Quebec', 'Barcelona']
restaurants = ['Gibsons Bar & Steakhouse', '2','3','4','5']
transports = ['1','2','3','4','5']
entertainment = ['1','2','3','4','5']



def location_select(location_list):
    select_location = random.choice(location_list)
    return select_location 

        
    

final_location = location_select(locations)


def restaurant_select (restaurant_list):
    select_restaurant = random.choice(restaurant_list)
    return select_restaurant

final_restaurant = restaurant_select(restaurants) 

def transports_select (transport_list):
    select_transport = random.choice(transport_list)
    return select_transport

final_transport = transports_select(transports)

    
def entertainment_select (entertainment_list):
    select_entertainment = random.choice(entertainment_list)
    return select_entertainment

final_entertainment = entertainment_select(entertainment) 





    



   
