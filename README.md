# Hotel Allocation Project

## Overview

This project aims to allocate customers to hotels based on their preferences, room availability, and pricing. The dataset includes information about 400 hotels, 4000 potential customers, and their preferences. The program implements four different allocation strategies and generates a report on the results.

## Datasets

- **hotels.xlsx**: Contains the number of vacant rooms and unit cost of each room for 400 hotels.
- **guests.xlsx**: Contains the discount fraction for 4000 potential customers.
- **preferences.xlsx**: Contains the order of hotel preference for each customer.

## Allocation Strategies

The program implements four different allocation strategies:

1. **Random Allocation**: Customers are randomly distributed to the rooms until the seats or customers are exhausted.
2. **Customer Preference Allocation**: Customers are served in order of reservation and allocated to hotels based on their preferences.
3. **Price-Based Allocation**: Hotels are distributed in order of price, starting with the cheapest hotel.
4. **Availability-Based Allocation**: Hotels are distributed in order of room availability, starting with the most spacious hotel.

## Metrics Calculated

The program generates a report that includes the following metrics for each strategy:

- Number of Customers Accommodated
- Number of Rooms Occupied
- Number of Different Hotels Occupied
- Total Revenue (Total earnings of each hotel)
- Average Customer Satisfaction

## Results

| Strategy                | Customers Accommodated | Rooms Occupied | Hotels Occupied | Total Revenue | Average Satisfaction |
|-------------------------|------------------------|----------------|------------------|---------------|----------------------|
| Random                  | 4000                   | 4000           | 400              | 641341.87     | 0.141225             |
| Customer Preference     | 3975                   | 3975           | 400              | 643597.53     | 0.892507             |
| Price-Based             | 4000                   | 4000           | 400              | 643525.05     | 1.000000             |
| Availability-Based      | 4000                   | 4000           | 400              | 643525.05     | 1.000000             |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Parsa-Hajian/HotelAllocation.git
