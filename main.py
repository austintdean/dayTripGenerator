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
restaurants = ['Gibsons Bar & Steakhouse', 'Eddle Vs Prime Seafood','Bob Bob Ricard Soho','Cichon Dingue Champlain','RAO restaurant']
transports = ['car','train','boat','helicopter','taxi']
entertainment = ['watch a play','hike a mountain','see Big Ben','run with the bulls','dance at the ball']


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



def message_one(name):
    final_location = location_select(locations)
    print(f'Welcome {name} to Day Trip Generator! Would you like to travel to {final_location}? ')
    user_input = input('y/n')
    if user_input == 'y':
        print('Sounds like a plan! Lets get that down for you!')
        message_two(name)
        
    
    else:
        print(f'That is too bad! Lets try again.')            
        message_one(name)


    
def message_two(name):
    print(f'Wonderful, {name}! You have chosen to travel to {final_location}. Would you like to eat at {final_restaurant}? ')
    final_restaurant = restaurant_select(restaurants) 
    user_input = input('y/n')
    if user_input == 'y':
        print('Great!')
        message_three(name)
        return 
    
    else:
        print(f'That is too bad! Lets try again.')            
        message_two(name)

def message_three(name):

    print(f'Thanks, {name}! You have chosen ti travel to {final_location} and eat at {final_restaurant}? Would you like to transport yourself using {final_transport}?')
    final_transport = transports_select(transports)
    user_input = input('y/n')
    if user_input == 'y':
        print('Great!')
        message_four(name)
        return 
    
    else:
        print(f'That is too bad! Lets try again.')            
        message_three(name)

        
        
        
        
def message_four(name):
    print(f'Thanks, {name}! You have chosen to travel to {final_location}, eat at {final_restaurant} and transport yourself using {final_transport}; would you like to {final_entertainment}? ')
    final_entertainment = entertainment_select(entertainment)  
    user_input = input('y/n')
    if user_input == 'y':
        print('Great!')
        message_final(name)
        return 
    
    else:
        print(f'That is too bad! Lets try again.')            
        message_four(name)


def message_final(name):
    print(f'Thanks, {name}! You have chosen {final_location}, will eat at {final_restaurant}, travel using {final_transport}, and would like to {final_entertainment}? Does this trip sound fun for you?')
    user_input = input('y/n')
    if user_input == 'y':
        print('Great! We hope that you enjoy your trip! Thanks for using Day Trip Generator!')
      
    
    else:
        print(f'That is too bad! Lets try again from the beginning.')            
        message_one(name)



message_one('Mark')
   
