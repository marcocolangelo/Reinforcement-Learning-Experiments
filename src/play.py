# -*- coding: utf-8 -*-

import pygame
from stable_baselines3 import PPO
from monopoly_env import MonopolyEnv
from monopoly_gui import MonopolyGUI

def main():
    """
    Main function to load a trained agent and watch it play Monopoly with a GUI.
    """
    # --- Load Model ---
    model_path = "models/ppo_monopoly.zip"
    try:
        model = PPO.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model not found at {model_path}.")
        print("Please run train.py to train and save a model first.")
        return

    # --- Initialize Environment and GUI ---
    env = MonopolyEnv(num_players=2)
    gui = MonopolyGUI(env.game)
    clock = pygame.time.Clock()

    obs, _ = env.reset()
    gui.update() # Initial render

    # --- Game Loop ---
    running = True
    terminated = False
    action_names = {0: "Roll", 1: "Buy", 2: "End Turn"}

    while running:
        # Handle Pygame events
        running = gui.handle_events()
        if not running:
            break

        if not terminated:
            # Get action from the agent
            action, _states = model.predict(obs, deterministic=True)

            # Announce the action
            current_player_id = env.game.current_player_index
            print(f"Player {current_player_id} attempts action: {action_names.get(action, 'Unknown')}")

            # Perform the action in the environment
            obs, reward, terminated, truncated, info = env.step(action)

            # Update the GUI
            gui.update()
            print("GUI Updated.")

            if terminated or truncated:
                print("Game Over!")

        # Control the game speed
        # e.g., 5 frames per second to make it easily watchable
        clock.tick(5)

    gui.close()
    env.close()

if __name__ == '__main__':
    main()
