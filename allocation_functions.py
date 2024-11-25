import pandas as pd
import numpy as np


''' RANDOM ALLOCATION

Input: hotels, guests, preferences
Output: allocations DataFrame

1. Initialize allocations as an empty list
2. Copy hotels DataFrame to HOTEL
3. For each guest in guests:
     a. Filter HOTEL to get available hotels
     b. If no available hotels, exit the loop
     c. Randomly select one hotel
     d. Calculate discounted price for the guest
     e. Append allocation details to allocations
     f. Reduce the room count for the selected hotel
4. Return allocations as a DataFrame

'''

def random_allocation(hotels, guests, preferences):
    #Initialize allocations as an empty list
    allocations = []
    
    #Copy hotels DataFrame to HOTEL
    HOTEL = hotels.copy()
    
    #For each guest in guests
    for guestID in guests['guest']:
        
        #Filter HOTEL to get available hotels
        available_HOTELS = HOTEL[ HOTEL['rooms'] > 0 ]
        
        #If no available hotels, exit the loop
        if available_HOTELS.empty == True : 
            break
        
        #Randomly select one hotel
        selected_HOTEL = available_HOTELS.sample(1).iloc[0] 
        hotelID = selected_HOTEL['hotel']
        
        #Calculate discounted price for the guest
        discount = guests.loc[guests['guest'] == guestID, 'discount'].values[0]
        final_price = selected_HOTEL['price'] * (1 - discount)
        
        #Append allocation details to allocations
        allocations.append({
            'guest_id': guestID,
            'hotel_id': hotelID,
            'price_paid': final_price
        })
        
        #Reduce the room count for the selected hotel
        HOTEL.loc[HOTEL['hotel'] == hotelID, 'rooms'] -= 1

    return pd.DataFrame(allocations)


''' CUSTOMER PREFRENCE ALLOCATION

Input: hotels, guests, preferences
Output: allocations DataFrame

1. Initialize allocations as an empty list
2. Copy hotels DataFrame to HOTEL
3. For each guest in guests:
     a. Retrieve and sort guest’s hotel preferences by priority
     b. For each preferred hotel:
          i. Check if hotel has available rooms
          ii. If available:
                - Calculate discounted price
                - Append allocation details to allocations
                - Reduce the room count for the selected hotel
                - Break to the next guest
4. Return allocations as a DataFrame


'''
def preference_allocation(hotels, guests, preferences):
    #Initialize allocations as an empty list
    allocations = []
    
    #Copy hotels DataFrame to HOTEL
    HOTEL = hotels.copy()  
    
    #For each guest in guests:
    for guestID in guests['guest']:
        
        #Retrieve and sort guest’s hotel preferences by priority
        guest_preferences = preferences[preferences['guest'] == guestID].sort_values(by='priority')['hotel'].values
        
        #For each preferred hotel, Check if hotel has available rooms
        for hotelID in guest_preferences:
            selected_HOTEL = HOTEL[HOTEL['hotel'] == hotelID]
            
            #If available,Calculate discounted price
            if not selected_HOTEL.empty and selected_HOTEL.iloc[0]['rooms'] > 0:
                discount = guests.loc[guests['guest'] == guestID, 'discount'].values[0]
                final_price = selected_HOTEL.iloc[0]['price'] * (1 - discount)
                
                #Append allocation details to allocations
                allocations.append({
                    'guest_id': guestID,
                    'hotel_id': hotelID,
                    'price_paid': final_price
                })
                #Reduce the room count for the selected hotel
                HOTEL.loc[HOTEL['hotel'] == hotelID, 'rooms'] -= 1
                #Break to the next guest
                break 

    return pd.DataFrame(allocations)



'''  Price-Based Allocation

Input: hotels, guests, preferences
Output: allocations DataFrame

1. Initialize allocations as an empty list
2. Copy and sort hotels DataFrame by price (ascending)
3. For each guest in guests:
     a. Retrieve and sort guest’s hotel preferences by priority
     b. For each preferred hotel:
          i. Check if hotel has available rooms
          ii. If available:
                - Calculate discounted price
                - Append allocation details to allocations
                - Reduce the room count for the selected hotel
                - Break to the next guest
4. Return allocations as a DataFrame
'''

def price_allocation(hotels, guests, preferences):
    #Initialize allocations as an empty list
    allocations = []
    
    #Copy and sort hotels DataFrame by price (ascending)
    HOTEL = hotels.copy()
    sorted_HOTELS = HOTEL.sort_values(by='price')
    
    #For each guest in guests:
    for guestID in guests['guest']:
        
        #Retrieve and sort guest’s hotel preferences by priority
        guest_preferences = preferences[preferences['guest'] == guestID].sort_values(by='priority')['hotel'].values
        
        #For each preferred hotel:
        for hotelID in guest_preferences:
            selected_HOTEL = sorted_HOTELS[sorted_HOTELS['hotel'] == hotelID]
            
            #Check if hotel has available rooms
            #If available:
            if not selected_HOTEL.empty and selected_HOTEL.iloc[0]['rooms'] > 0:
                
                #Calculate discounted price
                discount = guests.loc[guests['guest'] == guestID, 'discount'].values[0]
                final_price = selected_HOTEL.iloc[0]['price'] * (1 - discount)
                
                #Append allocation details to allocations
                allocations.append({
                    'guest_id': guestID,
                    'hotel_id': hotelID,
                    'price_paid': final_price
                })
                
                #Reduce the room count for the selected hotel
                HOTEL.loc[HOTEL['hotel'] == hotelID, 'rooms'] -= 1
                
                #Break to the next guest
                break  

    return pd.DataFrame(allocations)

''' Availability-Based Allocation

Input: hotels, guests, preferences
Output: allocations DataFrame

1. Initialize allocations as an empty list
2. Copy and sort hotels DataFrame by rooms (descending)
3. For each guest in guests:
     a. Retrieve and sort guest’s hotel preferences by priority
     b. For each preferred hotel:
          i. Check if hotel has available rooms
          ii. If available:
                - Calculate discounted price
                - Append allocation details to allocations
                - Reduce the room count for the selected hotel
                - Break to the next guest
4. Return allocations as a DataFrame
'''

def availability_allocation(hotels, guests, preferences):
    #Initialize allocations as an empty list
    allocations = []
    
    #Copy and sort hotels DataFrame by rooms (descending)
    HOTEL = hotels.copy()  
    sorted_HOTELS = HOTEL.sort_values(by='rooms', ascending=False)
    
    #For each guest in guests:
    for guestID in guests['guest']:
        
        #Retrieve and sort guest’s hotel preferences by priority
        guest_preferences = preferences[preferences['guest'] == guestID].sort_values(by='priority')['hotel'].values
        
        #For each preferred hotel:
        for hotelID in guest_preferences:
            selected_HOTEL = sorted_HOTELS[sorted_HOTELS['hotel'] == hotelID]
            
            #Check if hotel has available rooms
            #If available:
            if not selected_HOTEL.empty and selected_HOTEL.iloc[0]['rooms'] > 0:
                
                #Calculate discounted price
                discount = guests.loc[guests['guest'] == guestID, 'discount'].values[0]
                final_price = selected_HOTEL.iloc[0]['price'] * (1 - discount)
                
                #Append allocation details to allocations
                allocations.append({
                    'guest_id': guestID,
                    'hotel_id': hotelID,
                    'price_paid': final_price
                })
                
                #Reduce the room count for the selected hotel
                HOTEL.loc[HOTEL['hotel'] == hotelID, 'rooms'] -= 1
                
                #Break to the next guest
                break  

    return pd.DataFrame(allocations)

def calculate_metrics(allocation_df, hotels, preferences):
    # 1. Number of Customers Accommodated
    customers_accommodated = len(allocation_df)
    
    # 2. Number of Rooms Occupied
    rooms_occupied = customers_accommodated  # Each guest occupies one room
    
    # 3. Number of Different Hotels Occupied
    hotels_occupied = allocation_df['hotel_id'].nunique()
    
    # 4. Total Revenue
    total_revenue = allocation_df['price_paid'].sum()
    
    # 5. Average Satisfaction
    satisfaction_scores = []
    for _, row in allocation_df.iterrows():
        guest_id = row['guest_id']
        hotel_id = row['hotel_id']
        rank = preferences[
            (preferences['guest'] == guest_id) & (preferences['hotel'] == hotel_id)
        ]['priority'].values
        if len(rank) > 0:  # If hotel is in guest's preferences
            satisfaction_scores.append(1 / rank[0])  # Satisfaction = 1 / priority rank
    avg_satisfaction = sum(satisfaction_scores) / len(satisfaction_scores) if satisfaction_scores else 0
    
    # Return metrics as a dictionary
    return {
        "Customers Accommodated": customers_accommodated,
        "Rooms Occupied": rooms_occupied,
        "Hotels Occupied": hotels_occupied,
        "Total Revenue": total_revenue,
        "Average Satisfaction": avg_satisfaction
    }
