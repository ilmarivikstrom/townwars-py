import pygame as pg

from src.colors import BASE, PEACH, RGB, TEXT
from src.component import Component


class Button(Component):
    def __init__(
        self,
        on_click: callable,
        center: tuple[int, int],
        text: str,
        font_size: int = 16,
        padding: int = 12,
    ) -> None:
        self.on_click = on_click
        self.center = center
        self.font_size = font_size
        self.text = text
        self.padding = padding

        self.original_text_color: RGB = TEXT
        self.original_background_color: RGB = BASE
        self.hover_text_color: RGB = BASE
        self.hover_background_color: RGB = PEACH

        self.is_hovered = False
        self.font = pg.font.Font(pg.font.match_font("monospace"), font_size)
        self.text_surface = None
        self.background_surface = None

        self._update_surfaces()

    def handle_event(self, event: pg.event.Event) -> None:
        if event.type == pg.MOUSEMOTION:
            self.is_hovered = self._get_rect().collidepoint(event.pos)
            self._update_surfaces()
        if event.type == pg.MOUSEBUTTONDOWN and self.is_hovered and self.on_click:
            self.on_click()

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        if self.background_surface is None or self.text_surface is None:
            return

        # Calculate positions so origin is at the center
        bg_width = self.background_surface.get_width()
        bg_height = self.background_surface.get_height()
        bg_x = self.center[0] - bg_width // 2
        bg_y = self.center[1] - bg_height // 2

        screen.blit(self.background_surface, (bg_x, bg_y))

        # Calculate text position relative to the background's top-left corner
        text_x = bg_x + self.padding
        text_y = bg_y + self.padding
        screen.blit(self.text_surface, (text_x, text_y))

    def _set_text(self, text: str) -> None:
        self.text = text
        self._update_surfaces()

    def _update_surfaces(self) -> None:
        if not self.text:
            self.text_surface = None
            self.background_surface = None
            return

        if self.is_hovered:
            current_color = self.hover_text_color
            current_background_color = self.hover_background_color
        else:
            current_color = self.original_text_color
            current_background_color = self.original_background_color
        # Render text directly to text_surface
        self.text_surface = self.font.render(self.text, True, current_color)  # noqa: FBT003

        # Get dimensions from the rendered text
        line_width = self.text_surface.get_width()
        line_height = self.text_surface.get_height()

        # Create background surface with padding
        bg_width = line_width + (self.padding * 2)
        bg_height = line_height + (self.padding * 2)

        self.background_surface = pg.Surface((bg_width, bg_height), pg.SRCALPHA)

        # Draw rounded rectangle
        rect = pg.Rect(0, 0, bg_width, bg_height)
        pg.draw.rect(
            self.background_surface,
            current_background_color,
            rect,
            border_radius=3,
        )

        # Add white outline when hovered
        if self.is_hovered:
            pg.draw.rect(
                self.background_surface,
                (150, 150, 150),
                rect,
                width=1,
                border_radius=3,
            )

    def _get_rect(self) -> pg.Rect:
        if self.background_surface is None:
            return pg.Rect(self.center[0], self.center[1], 0, 0)

        bg_width = self.background_surface.get_width()
        bg_height = self.background_surface.get_height()
        bg_x = self.center[0] - bg_width // 2
        bg_y = self.center[1] - bg_height // 2

        return pg.Rect(
            bg_x,
            bg_y,
            bg_width,
            bg_height,
        )
