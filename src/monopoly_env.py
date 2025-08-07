# -*- coding: utf-8 -*-

import gymnasium as gym
from gymnasium import spaces
import numpy as np
from monopoly_game import MonopolyGame

class MonopolyEnv(gym.Env):
    """A custom Gymnasium environment for the game of Monopoly."""
    metadata = {'render.modes': ['human']}

    def __init__(self, num_players=2):
        super(MonopolyEnv, self).__init__()

        self.game = MonopolyGame(num_players=num_players)
        self.num_players = num_players

        # Define the action space
        # Action 0: Roll and move (the primary action for a turn)
        # Action 1: Buy property (if available and affordable)
        # Action 2: Do nothing / End turn
        self.action_space = spaces.Discrete(3)

        # Define the observation space
        # It's a simplified representation of the game state:
        # - Player 0's position
        # - Player 0's money (normalized)
        # - Player 0's bankruptcy status
        # - Ownership status for each of the 40 properties (-1 if not ownable, 0 if unowned, player_id if owned)
        # We'll need a more comprehensive observation space later on.
        self.observation_space = spaces.Box(low=-1, high=1500, shape=(40 + 3,), dtype=np.float32)

    def _get_obs(self):
        """Constructs the observation vector from the current game state."""
        player = self.game.get_current_player()

        # Player-specific info
        pos = player['position']
        money = player['money']
        is_bankrupt = 1 if player['is_bankrupt'] else 0

        # Property ownership info
        ownership = np.full(40, -1.0) # -1 for non-properties
        for i, prop_details in self.game.properties.items():
            owner = prop_details['owner']
            ownership[i] = owner if owner is not None else 0

        obs = np.concatenate(([pos, money, is_bankrupt], ownership)).astype(np.float32)
        return obs

    def reset(self, seed=None, options=None):
        """Resets the environment to an initial state."""
        super().reset(seed=seed)
        self.game = MonopolyGame(num_players=self.num_players)
        return self._get_obs(), {}

    def step(self, action):
        """Executes one time step within the environment."""
        player = self.game.get_current_player()
        reward = 0
        terminated = False

        # --- Action Handling ---
        if action == 0: # Roll and move
            d1, d2, is_double = self.game.roll_dice()
            roll = d1 + d2
            old_money = player['money']

            new_pos = self.game.move_player(player, roll)
            self.game.handle_landed_on_space(player, new_pos)

            # Simple reward: change in money
            reward = player['money'] - old_money

        elif action == 1: # Buy property
            space_index = player['position']
            space = self.game.board[space_index]

            if space['type'] in ['property', 'railroad', 'utility'] and self.game.properties[space_index]['owner'] is None:
                if self.game.buy_property(player, space_index):
                    reward = 10 # Reward for acquiring property
                else:
                    reward = -5 # Penalty for trying to buy something unaffordable
            else:
                reward = -1 # Penalty for invalid action

        elif action == 2: # Do nothing / End turn
            self.game.next_turn()
            reward = 0 # No reward for just ending the turn

        # --- Check for game over ---
        if self.game.is_game_over():
            terminated = True
            # Assign a large reward for winning, and penalty for losing.
            if not player['is_bankrupt']:
                reward += 1000 # Winner's bonus
            else:
                reward -= 500 # Loser's penalty

        obs = self._get_obs()
        info = {}
        # For simplicity, we set truncated to False. A real implementation might use it for time limits.
        truncated = False

        return obs, reward, terminated, truncated, info

    def render(self, mode='human'):
        """Renders the environment to the console."""
        if mode == 'human':
            player = self.game.get_current_player()
            print("-" * 30)
            print(f"Current Player: {player['id']}")
            print(f"Position: {player['position']} ({self.game.board[player['position']]['name']})")
            print(f"Money: ${player['money']}")
            print(f"Properties Owned: {player['properties']}")
            print(f"In Jail: {'Yes' if player['in_jail'] else 'No'}")
            print("-" * 30)

    def close(self):
        """Cleans up the environment."""
        pass

if __name__ == '__main__':
    from stable_baselines3.common.env_checker import check_env

    env = MonopolyEnv()
    # It will check your custom environment and output additional warnings if needed
    try:
        check_env(env)
        print("Environment check passed!")
    except Exception as e:
        print("Environment check failed!")
        print(e)

    # Test the environment loop
    obs, _ = env.reset()
    env.render()
    for i in range(10):
        action = env.action_space.sample() # take a random action
        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        if terminated or truncated:
            print("Episode finished!")
            obs, _ = env.reset()
            env.render()
    env.close()
