# -*- coding: utf-8 -*-

import random
from monopoly_assets import BOARD_SPACES, CHANCE_CARDS, COMMUNITY_CHEST_CARDS

class MonopolyGame:
    """
    Manages the state and logic of a game of Monopoly.
    """
    def __init__(self, num_players=2):
        """
        Initializes a new game of Monopoly.

        Args:
            num_players (int): The number of players in the game.
        """
        if not 2 <= num_players <= 4:
            raise ValueError("Number of players must be between 2 and 4.")

        self.num_players = num_players
        self.board = BOARD_SPACES

        # Initialize players
        self.players = self._initialize_players()

        # Game state
        self.current_player_index = 0
        self.game_over = False

        # Deck of cards
        self.chance_cards = list(CHANCE_CARDS)
        self.community_chest_cards = list(COMMUNITY_CHEST_CARDS)
        random.shuffle(self.chance_cards)
        random.shuffle(self.community_chest_cards)

        # Property ownership
        self.properties = self._initialize_properties()

    def _initialize_players(self):
        """Creates the player objects for the game."""
        players = []
        for i in range(self.num_players):
            players.append({
                "id": i,
                "position": 0,
                "money": 1500,
                "properties": set(),
                "in_jail": False,
                "jail_turns": 0,
                "get_out_of_jail_cards": 0,
                "is_bankrupt": False,
            })
        return players

    def _initialize_properties(self):
        """Initializes the ownership status of all properties."""
        properties = {}
        for i, space in enumerate(self.board):
            if space["type"] in ["property", "railroad", "utility"]:
                properties[i] = {
                    "owner": None,
                    "houses": 0,
                    "is_mortgaged": False,
                }
        return properties

    def roll_dice(self):
        """
        Rolls two six-sided dice.

        Returns:
            tuple: A tuple containing the result of the two dice and a boolean indicating if it was a double.
        """
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        is_double = (die1 == die2)
        return die1, die2, is_double

    def get_current_player(self):
        """Returns the player object for the current turn."""
        return self.players[self.current_player_index]

    def next_turn(self):
        """Advances the turn to the next active player."""
        while True:
            self.current_player_index = (self.current_player_index + 1) % self.num_players
            if not self.players[self.current_player_index]["is_bankrupt"]:
                break

    def move_player(self, player, roll_amount):
        """Moves a player and handles passing Go."""
        old_position = player["position"]
        new_position = (old_position + roll_amount) % len(self.board)
        player["position"] = new_position

        # Handle passing Go
        if new_position < old_position:
            player["money"] += 200
            print(f"Player {player['id']} passed Go and collected $200.")

        print(f"Player {player['id']} moved to {self.board[new_position]['name']}.")
        return new_position

    def handle_landed_on_space(self, player, space_index):
        """Handles the logic for a player landing on a specific space."""
        space = self.board[space_index]
        space_type = space["type"]

        print(f"Player {player['id']} landed on {space['name']} (type: {space_type}).")

        if space_type == "property" or space_type == "railroad" or space_type == "utility":
            self._handle_property_space(player, space_index)
        elif space_type == "chance":
            self._handle_chance_card(player)
        elif space_type == "community_chest":
            self._handle_community_chest_card(player)
        elif space_type == "tax":
            self._handle_tax_space(player, space)
        elif space_type == "go_to_jail":
            self._go_to_jail(player)
        else:
            # For spaces like "Go", "Jail (Just Visiting)", "Free Parking"
            print(f"No action required for Player {player['id']} on {space['name']}.")

    def _handle_property_space(self, player, space_index):
        """Logic for landing on a property, railroad, or utility."""
        property_info = self.properties[space_index]
        owner_id = property_info["owner"]

        if owner_id is None:
            # Opportunity to buy. For the RL agent, this will be an action.
            # Here, we'll just print for now.
            space = self.board[space_index]
            print(f"Space is unowned. Player {player['id']} can buy {space['name']} for ${space['price']}.")
        elif owner_id != player["id"]:
            # Pay rent
            owner = self.players[owner_id]
            rent = self._calculate_rent(space_index)
            self._pay_rent(player, owner, rent)
        else:
            # Player owns it
            print("Player already owns this property.")

    def buy_property(self, player, space_index):
        """Allows a player to buy an unowned property."""
        space = self.board[space_index]
        property_info = self.properties[space_index]

        if property_info["owner"] is not None:
            print("Error: Property is already owned.")
            return False

        price = space["price"]
        if player["money"] >= price:
            player["money"] -= price
            property_info["owner"] = player["id"]
            player["properties"].add(space_index)
            print(f"Player {player['id']} bought {space['name']} for ${price}.")
            return True
        else:
            print(f"Player {player['id']} does not have enough money to buy {space['name']}.")
            return False

    def _calculate_rent(self, space_index):
        """
        Calculates the rent for a given space.
        This is a simplified version. A full implementation would be more complex.
        """
        space = self.board[space_index]
        property_info = self.properties[space_index]
        owner_id = property_info["owner"]
        owner = self.players[owner_id]

        if space["type"] == "property":
            # Simplified: returns base rent without considering houses or monopolies
            return space["rent"][0]
        elif space["type"] == "railroad":
            owned_railroads = sum(1 for prop_idx in owner["properties"] if self.board[prop_idx]["type"] == "railroad")
            return 25 * (2 ** (owned_railroads - 1))
        elif space["type"] == "utility":
            # Simplified: returns a fixed amount, not based on dice roll
            return 10

        return 0

    def _pay_rent(self, payer, owner, rent_amount):
        """Handles the transaction of one player paying rent to another."""
        if payer["money"] >= rent_amount:
            payer["money"] -= rent_amount
            owner["money"] += rent_amount
            print(f"Player {payer['id']} paid ${rent_amount} in rent to Player {owner['id']}.")
        else:
            # Handle bankruptcy
            owner["money"] += payer["money"]
            payer["money"] = 0
            payer["is_bankrupt"] = True
            print(f"Player {payer['id']} could not pay ${rent_amount} and went bankrupt!")
            # Transfer properties in a real game

    def _handle_chance_card(self, player):
        """Draws and executes a Chance card."""
        card = self.chance_cards.pop(0)
        self.chance_cards.append(card) # Return card to bottom of the deck
        print(f"Player {player['id']} drew a Chance card: {card['description']}")
        # Card action logic to be implemented

    def _handle_community_chest_card(self, player):
        """Draws and executes a Community Chest card."""
        card = self.community_chest_cards.pop(0)
        self.community_chest_cards.append(card) # Return card to bottom of the deck
        print(f"Player {player['id']} drew a Community Chest card: {card['description']}")
        # Card action logic to be implemented

    def _handle_tax_space(self, player, space):
        """Handles paying a tax."""
        tax_amount = space["amount"]
        player["money"] -= tax_amount
        print(f"Player {player['id']} paid ${tax_amount} in tax.")

    def _go_to_jail(self, player):
        """Sends a player to jail."""
        player["position"] = self.board.index(next(s for s in self.board if s['type'] == 'jail'))
        player["in_jail"] = True
        player["jail_turns"] = 0
        print(f"Player {player['id']} has been sent to Jail!")

    def is_game_over(self):
        """Checks if the game has ended (i.e., only one player is not bankrupt)."""
        active_players = sum(1 for p in self.players if not p["is_bankrupt"])
        return active_players <= 1

# Example usage:
if __name__ == '__main__':
    game = MonopolyGame(num_players=2)
    player = game.get_current_player()
    print(f"Starting game with {game.num_players} players.")
    print(f"Player {player['id']}'s turn. Money: ${player['money']}")

    # Simulate a full turn
    d1, d2, is_double = game.roll_dice()
    roll = d1 + d2
    print(f"Player {player['id']} rolled a {d1} and a {d2} (Total: {roll}).")

    new_position = game.move_player(player, roll)
    game.handle_landed_on_space(player, new_position)

    print(f"Player {player['id']} ends turn. Money: ${player['money']}")

    game.next_turn()
    player = game.get_current_player()
    print(f"\nNext turn: Player {player['id']}.")
