# -*- coding: utf-8 -*-

import os
from stable_baselines3 import PPO
from monopoly_env import MonopolyEnv

def main():
    """
    Main function to train the PPO agent on the Monopoly environment.
    """
    # Create logs and models directories if they don't exist
    log_dir = "logs/"
    model_dir = "models/"
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)

    # Instantiate the Monopoly environment
    env = MonopolyEnv(num_players=2)
    env.reset()

    # Instantiate the PPO model
    # 'MlpPolicy' is used because the observation space is a flat vector.
    model = PPO('MlpPolicy', env, verbose=1)

    # Train the model
    # Start with a small number of timesteps to ensure everything is working.
    total_timesteps = 10000
    print(f"Starting training for {total_timesteps} timesteps...")

    model.learn(total_timesteps=total_timesteps)

    print("Training finished.")

    # Save the trained model
    model_path = os.path.join(model_dir, "ppo_monopoly")
    model.save(model_path)

    print(f"Model saved to {model_path}.zip")

    env.close()

if __name__ == '__main__':
    main()
