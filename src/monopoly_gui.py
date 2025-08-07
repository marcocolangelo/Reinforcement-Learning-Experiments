# -*- coding: utf-8 -*-

import pygame
from monopoly_assets import BOARD_SPACES

# --- Constants ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BOARD_SIZE = 600
INFO_PANEL_WIDTH = SCREEN_WIDTH - BOARD_SIZE
CELL_SIZE = BOARD_SIZE // 11

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOARD_COLOR = (205, 230, 208)
PLAYER_COLORS = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
GROUP_COLORS = {
    "Brown": (139, 69, 19),
    "Light Blue": (173, 216, 230),
    "Pink": (255, 105, 180),
    "Orange": (255, 165, 0),
    "Red": (255, 0, 0),
    "Yellow": (255, 255, 0),
    "Green": (0, 128, 0),
    "Dark Blue": (0, 0, 139),
    "Railroad": (50, 50, 50),
    "Utility": (150, 150, 150),
}

class MonopolyGUI:
    """
    Handles the graphical rendering of the Monopoly game using Pygame.
    """

    def __init__(self, game):
        pygame.init()
        self.game = game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Monopoly RL Agent")
        self.font = pygame.font.SysFont(None, 24)
        self.small_font = pygame.font.SysFont(None, 18)
        self._board_layout = self._create_board_layout()

    def _create_board_layout(self):
        """Creates the coordinates for each space on the board."""
        layout = {}
        # Bottom row (right to left)
        for i in range(11):
            layout[i] = (BOARD_SIZE - (i + 1) * CELL_SIZE, BOARD_SIZE - CELL_SIZE)
        # Left column (bottom to top)
        for i in range(11, 21):
            layout[i] = (0, BOARD_SIZE - (i - 9) * CELL_SIZE)
        # Top row (left to right)
        for i in range(21, 31):
            layout[i] = ((i - 20) * CELL_SIZE, 0)
        # Right column (top to bottom)
        for i in range(31, 40):
            layout[i] = (BOARD_SIZE - CELL_SIZE, (i - 30) * CELL_SIZE)
        return layout

    def _draw_board(self):
        """Draws the static parts of the board."""
        self.screen.fill(BOARD_COLOR)

        # Draw cells
        for i, space_info in enumerate(BOARD_SPACES):
            x, y = self._board_layout[i]
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, BLACK, rect, 1)

            # Draw color bar for properties
            if space_info.get("group") in GROUP_COLORS:
                color = GROUP_COLORS[space_info["group"]]
                color_rect = pygame.Rect(x + 1, y + 1, CELL_SIZE - 2, CELL_SIZE // 4)
                pygame.draw.rect(self.screen, color, color_rect)

            # Draw name
            name_text = self.small_font.render(space_info["name"], True, BLACK)
            self.screen.blit(name_text, (x + 5, y + CELL_SIZE // 3))

    def _draw_player_tokens(self):
        """Draws the player tokens on the board."""
        for player in self.game.players:
            if not player["is_bankrupt"]:
                pos = player["position"]
                base_x, base_y = self._board_layout[pos]

                # Offset tokens so they don't overlap completely
                offset_x = (player["id"] % 2) * (CELL_SIZE // 4) + 10
                offset_y = (player["id"] // 2) * (CELL_SIZE // 4) + 10

                color = PLAYER_COLORS[player["id"]]
                pygame.draw.circle(self.screen, color, (base_x + offset_x, base_y + offset_y), 8)

    def _draw_ownership(self):
        """Indicates property ownership on the board."""
        for i, prop_details in self.game.properties.items():
            if prop_details["owner"] is not None:
                owner_id = prop_details["owner"]
                color = PLAYER_COLORS[owner_id]
                x, y = self._board_layout[i]
                pygame.draw.circle(self.screen, color, (x + CELL_SIZE - 10, y + 10), 5)

    def _draw_info_panel(self):
        """Draws the side panel with player and game information."""
        panel_x = BOARD_SIZE
        pygame.draw.rect(self.screen, WHITE, (panel_x, 0, INFO_PANEL_WIDTH, SCREEN_HEIGHT))

        y_offset = 20
        # Game info
        turn_text = self.font.render(f"Current Turn: Player {self.game.current_player_index}", True, BLACK)
        self.screen.blit(turn_text, (panel_x + 20, y_offset))
        y_offset += 40

        # Player info
        for player in self.game.players:
            color = PLAYER_COLORS[player["id"]]
            player_header = self.font.render(f"Player {player['id']}", True, color)
            self.screen.blit(player_header, (panel_x + 20, y_offset))
            y_offset += 25

            money_text = self.small_font.render(f"Money: ${player['money']}", True, BLACK)
            self.screen.blit(money_text, (panel_x + 30, y_offset))
            y_offset += 20

            status = "Bankrupt" if player["is_bankrupt"] else "Active"
            status_text = self.small_font.render(f"Status: {status}", True, BLACK)
            self.screen.blit(status_text, (panel_x + 30, y_offset))
            y_offset += 30

    def update(self):
        """Updates the entire display."""
        self._draw_board()
        self._draw_player_tokens()
        self._draw_ownership()
        self._draw_info_panel()
        pygame.display.flip()

    def handle_events(self):
        """Handles Pygame events like closing the window."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def close(self):
        """Closes the Pygame window."""
        pygame.quit()
