# Reinforcement Learning Monopoly Agent

This project provides a complete framework for training a Reinforcement Learning (RL) agent to play the game of Monopoly. It uses the PPO (Proximal Policy Optimization) algorithm from `stable-baselines3`. The project also includes a simple graphical interface built with `pygame` to visualize the trained agent's gameplay.

## Features

-   **Monopoly Game Engine:** A core engine that implements the rules of Monopoly.
-   **Custom Gym Environment:** A `gymnasium.Env` compatible environment that allows RL agents to interact with the game.
-   **PPO Agent Training:** A script to train a PPO agent to learn how to play.
-   **Pygame GUI:** A simple graphical interface to watch the agent play and test its behavior.

## Project Structure

```
.
├── models/
│   └── ppo_monopoly.zip  # Saved model after training
├── notebooks/
│   └── ...
├── src/
│   ├── monopoly_assets.py      # Static data (board layout, cards)
│   ├── monopoly_game.py        # Core game logic class
│   ├── monopoly_env.py         # Gymnasium environment wrapper
│   ├── monopoly_gui.py         # Pygame GUI class for visualization
│   ├── train.py                # Script to train the agent
│   └── play.py                 # Script to watch the agent play
└── requirements.txt            # Python dependencies
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    > **Note:** The dependencies include PyTorch. If you have limited disk space, the installation might fail. The dependencies are configured to install a CPU-only version of PyTorch to be lightweight.

## How to Use

### 1. Train the Agent

To start training the agent, run the `train.py` script:

```bash
python src/train.py
```

This script will:
-   Instantiate the Monopoly environment.
-   Create a PPO agent.
-   Train the agent for a set number of timesteps (currently 10,000 for a quick test).
-   Save the trained model as `models/ppo_monopoly.zip`.

For effective training, you may want to increase the `total_timesteps` in `train.py` to a much larger number (e.g., 1,000,000 or more).

### 2. Watch the Agent Play

Once a model has been saved, you can watch it play using the Pygame interface by running the `play.py` script:

```bash
python src/play.py
```

This will open a window showing the Monopoly board, and the agent will begin to play. The speed can be adjusted by changing the `clock.tick()` value in `play.py`.

---
### (Italiano)

# Agente di Reinforcement Learning per il Monopoli

Questo progetto fornisce un framework completo per addestrare un agente di Reinforcement Learning (RL) a giocare al gioco del Monopoli. Utilizza l'algoritmo PPO (Proximal Policy Optimization) di `stable-baselines3`. Il progetto include anche una semplice interfaccia grafica creata con `pygame` per visualizzare il gameplay dell'agente addestrato.

## Funzionalità

-   **Motore di Gioco del Monopoli:** Un motore di base che implementa le regole del Monopoli.
-   **Ambiente Gym Personalizzato:** Un ambiente compatibile con `gymnasium.Env` che permette agli agenti RL di interagire con il gioco.
-   **Addestramento dell'Agente PPO:** Uno script per addestrare un agente PPO a imparare a giocare.
-   **GUI con Pygame:** Una semplice interfaccia grafica per guardare l'agente giocare e testare il suo comportamento.

## Struttura del Progetto

```
.
├── models/
│   └── ppo_monopoly.zip  # Modello salvato dopo l'addestramento
├── notebooks/
│   └── ...
├── src/
│   ├── monopoly_assets.py      # Dati statici (tabellone, carte)
│   ├── monopoly_game.py        # Classe con la logica di gioco
│   ├── monopoly_env.py         # Wrapper ambiente Gymnasium
│   ├── monopoly_gui.py         # Classe per la GUI con Pygame
│   ├── train.py                # Script per addestrare l'agente
│   └── play.py                 # Script per guardare l'agente giocare
└── requirements.txt            # Dipendenze Python
```

## Installazione

1.  **Clona la repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Installa le dipendenze:**
    Si consiglia di utilizzare un ambiente virtuale.
    ```bash
    python -m venv venv
    source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    > **Nota:** Le dipendenze includono PyTorch. Se lo spazio su disco è limitato, l'installazione potrebbe fallire. Le dipendenze sono configurate per installare una versione di PyTorch solo per CPU per essere più leggera.

## Come Usare

### 1. Addestrare l'Agente

Per avviare l'addestramento dell'agente, esegui lo script `train.py`:

```bash
python src/train.py
```

Questo script si occuperà di:
-   Istanziare l'ambiente del Monopoli.
-   Creare un agente PPO.
-   Addestrare l'agente per un numero prefissato di timesteps (attualmente 10.000 per un test rapido).
-   Salvare il modello addestrato come `models/ppo_monopoly.zip`.

Per un addestramento efficace, potresti voler aumentare il `total_timesteps` in `train.py` a un numero molto più grande (es. 1.000.000 o più).

### 2. Guardare l'Agente Giocare

Una volta che un modello è stato salvato, puoi guardarlo giocare tramite l'interfaccia Pygame eseguendo lo script `play.py`:

```bash
python src/play.py
```

Questo aprirà una finestra che mostra il tabellone del Monopoli e l'agente inizierà a giocare. La velocità può essere regolata modificando il valore `clock.tick()` in `play.py`.
