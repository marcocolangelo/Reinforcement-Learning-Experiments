# -*- coding: utf-8 -*-

"""
This file contains the static assets for the Monopoly game, including the board layout and property details.
"""

# Represents the 40 spaces on a standard Monopoly board
BOARD_SPACES = [
    {"name": "Go", "type": "go"},
    {"name": "Mediterranean Avenue", "type": "property", "price": 60, "rent": [2, 10, 30, 90, 160, 250], "group": "Brown", "house_cost": 50},
    {"name": "Community Chest", "type": "community_chest"},
    {"name": "Baltic Avenue", "type": "property", "price": 60, "rent": [4, 20, 60, 180, 320, 450], "group": "Brown", "house_cost": 50},
    {"name": "Income Tax", "type": "tax", "amount": 200},
    {"name": "Reading Railroad", "type": "railroad", "price": 200},
    {"name": "Oriental Avenue", "type": "property", "price": 100, "rent": [6, 30, 90, 270, 400, 550], "group": "Light Blue", "house_cost": 50},
    {"name": "Chance", "type": "chance"},
    {"name": "Vermont Avenue", "type": "property", "price": 100, "rent": [6, 30, 90, 270, 400, 550], "group": "Light Blue", "house_cost": 50},
    {"name": "Connecticut Avenue", "type": "property", "price": 120, "rent": [8, 40, 100, 300, 450, 600], "group": "Light Blue", "house_cost": 50},
    {"name": "Jail / Just Visiting", "type": "jail"},
    {"name": "St. Charles Place", "type": "property", "price": 140, "rent": [10, 50, 150, 450, 625, 750], "group": "Pink", "house_cost": 100},
    {"name": "Electric Company", "type": "utility", "price": 150},
    {"name": "States Avenue", "type": "property", "price": 140, "rent": [10, 50, 150, 450, 625, 750], "group": "Pink", "house_cost": 100},
    {"name": "Virginia Avenue", "type": "property", "price": 160, "rent": [12, 60, 180, 500, 700, 900], "group": "Pink", "house_cost": 100},
    {"name": "Pennsylvania Railroad", "type": "railroad", "price": 200},
    {"name": "St. James Place", "type": "property", "price": 180, "rent": [14, 70, 200, 550, 750, 950], "group": "Orange", "house_cost": 100},
    {"name": "Community Chest", "type": "community_chest"},
    {"name": "Tennessee Avenue", "type": "property", "price": 180, "rent": [14, 70, 200, 550, 750, 950], "group": "Orange", "house_cost": 100},
    {"name": "New York Avenue", "type": "property", "price": 200, "rent": [16, 80, 220, 600, 800, 1000], "group": "Orange", "house_cost": 100},
    {"name": "Free Parking", "type": "free_parking"},
    {"name": "Kentucky Avenue", "type": "property", "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "group": "Red", "house_cost": 150},
    {"name": "Chance", "type": "chance"},
    {"name": "Indiana Avenue", "type": "property", "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "group": "Red", "house_cost": 150},
    {"name": "Illinois Avenue", "type": "property", "price": 240, "rent": [20, 100, 300, 750, 925, 1100], "group": "Red", "house_cost": 150},
    {"name": "B. & O. Railroad", "type": "railroad", "price": 200},
    {"name": "Atlantic Avenue", "type": "property", "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "group": "Yellow", "house_cost": 150},
    {"name": "Ventnor Avenue", "type": "property", "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "group": "Yellow", "house_cost": 150},
    {"name": "Water Works", "type": "utility", "price": 150},
    {"name": "Marvin Gardens", "type": "property", "price": 280, "rent": [24, 120, 360, 850, 1025, 1200], "group": "Yellow", "house_cost": 150},
    {"name": "Go to Jail", "type": "go_to_jail"},
    {"name": "Pacific Avenue", "type": "property", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "group": "Green", "house_cost": 200},
    {"name": "North Carolina Avenue", "type": "property", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "group": "Green", "house_cost": 200},
    {"name": "Community Chest", "type": "community_chest"},
    {"name": "Pennsylvania Avenue", "type": "property", "price": 320, "rent": [28, 150, 450, 1000, 1200, 1400], "group": "Green", "house_cost": 200},
    {"name": "Short Line", "type": "railroad", "price": 200},
    {"name": "Chance", "type": "chance"},
    {"name": "Park Place", "type": "property", "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500], "group": "Dark Blue", "house_cost": 200},
    {"name": "Luxury Tax", "type": "tax", "amount": 100},
    {"name": "Boardwalk", "type": "property", "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000], "group": "Dark Blue", "house_cost": 200},
]

# Simplified list of Chance cards
CHANCE_CARDS = [
    {"description": "Advance to Go (Collect $200)", "action": "advance", "destination": "Go"},
    {"description": "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200", "action": "go_to_jail"},
    {"description": "Bank pays you dividend of $50", "action": "collect", "amount": 50},
    {"description": "Get Out of Jail Free", "action": "get_out_of_jail_free"},
    {"description": "Pay poor tax of $15", "action": "pay", "amount": 15},
    {"description": "Your building loan matures. Collect $150", "action": "collect", "amount": 150},
    {"description": "You have been elected Chairman of the Board. Pay each player $50", "action": "pay_each_player", "amount": 50},
    # Add more cards as needed
]

# Simplified list of Community Chest cards
COMMUNITY_CHEST_CARDS = [
    {"description": "Advance to Go (Collect $200)", "action": "advance", "destination": "Go"},
    {"description": "Bank error in your favor. Collect $200", "action": "collect", "amount": 200},
    {"description": "Doctor’s fee. Pay $50", "action": "pay", "amount": 50},
    {"description": "From sale of stock you get $50", "action": "collect", "amount": 50},
    {"description": "Get Out of Jail Free", "action": "get_out_of_jail_free"},
    {"description": "Go to Jail. Go directly to jail, do not pass Go, do not collect $200", "action": "go_to_jail"},
    {"description": "Holiday fund matures. Receive $100", "action": "collect", "amount": 100},
    {"description": "Income tax refund. Collect $20", "action": "collect", "amount": 20},
    {"description": "Life insurance matures. Collect $100", "action": "collect", "amount": 100},
    {"description": "Pay hospital fees of $100", "action": "pay", "amount": 100},
    {"description": "Pay school fees of $50", "action": "pay", "amount": 50},
    {"description": "You have won second prize in a beauty contest. Collect $10", "action": "collect", "amount": 10},
    {"description": "You inherit $100", "action": "collect", "amount": 100},
    # Add more cards as needed
]
