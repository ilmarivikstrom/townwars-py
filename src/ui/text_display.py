import pygame as pg


class TextDisplay:
    def __init__(
        self,
        origin: tuple[int, int] | None = None,
        center: tuple[int, int] | None = None,
        font_size: int = 16,
        padding: int = 8,
        max_width: int | None = None,
        background_alpha: int = 180,
        text: str = "",
    ) -> None:
        if origin is None and center is None:
            raise ValueError("Either origin or center must be provided")
        if origin is not None and center is not None:
            raise ValueError("Only one of origin or center should be provided")

        self.origin = origin
        self.center = center
        self.font_size = font_size
        self.padding = padding
        self.max_width = max_width
        self.background_alpha = background_alpha

        self.font = pg.font.Font(pg.font.match_font("monospace"), font_size)

        self.text = text
        self.lines = []

        self.text_color = (255, 255, 255)
        self.background_color = (0, 0, 0, background_alpha)

        self.text_surface = None
        self.background_surface = None
        self.rect = pg.Rect(0, 0, 0, 0)

        self._update_surfaces()

    def set_text(self, text: str) -> None:
        self.text = text
        self._update_surfaces()

    def handle_event(self, event: pg.event.Event) -> None:
        pass

    def update(self) -> None:
        pass

    def _update_surfaces(self) -> None:
        if not self.text:
            self.text_surface = None
            self.background_surface = None
            if self.center is not None:
                self.rect = pg.Rect(self.center[0], self.center[1], 0, 0)
            else:
                self.rect = pg.Rect(self.origin[0], self.origin[1], 0, 0)
            return

        self.lines = self.text.split("\n")

        line_surfaces = []
        max_line_width = 0

        for line in self.lines:
            if line.strip():  # Non-empty lines
                line_surface = self.font.render(line, True, self.text_color)  # noqa: FBT003
                line_surfaces.append(line_surface)
                max_line_width = max(max_line_width, line_surface.get_width())
            else:
                # Empty lines
                empty_surface = pg.Surface((0, self.font.get_height()), pg.SRCALPHA)
                line_surfaces.append(empty_surface)

        if not line_surfaces:
            self.text_surface = None
            self.background_surface = None
            if self.center is not None:
                self.rect = pg.Rect(self.center[0], self.center[1], 0, 0)
            else:
                self.rect = pg.Rect(self.origin[0], self.origin[1], 0, 0)
            return

        total_height = len(line_surfaces) * self.font.get_height()

        self.text_surface = pg.Surface((max_line_width, total_height), pg.SRCALPHA)

        y_offset = 0
        for line_surface in line_surfaces:
            self.text_surface.blit(line_surface, (0, y_offset))
            y_offset += self.font.get_height()

        bg_width = max_line_width + (self.padding * 2)
        bg_height = total_height + (self.padding * 2)

        if self.max_width is not None:
            bg_width = min(bg_width, self.max_width)

        self.background_surface = pg.Surface((bg_width, bg_height), pg.SRCALPHA)

        background_rect = pg.Rect(0, 0, bg_width, bg_height)
        self.background_surface.fill(self.background_color, background_rect)

        # Update the rect with the new dimensions
        if self.center is not None:
            self.rect = pg.Rect(0, 0, bg_width, bg_height)
            self.rect.center = self.center
        else:
            self.rect = pg.Rect(self.origin[0], self.origin[1], bg_width, bg_height)

    def draw(self, screen: pg.Surface) -> None:
        if self.background_surface is None or self.text_surface is None:
            return

        screen.blit(self.background_surface, self.rect)

        text_x = self.rect.x + self.padding
        text_y = self.rect.y + self.padding
        screen.blit(self.text_surface, (text_x, text_y))

    def set_center(self, center: tuple[int, int]) -> None:
        self.rect.center = center
        self.center = center
        if self.origin is not None:
            self.origin = (self.rect.x, self.rect.y)

    def set_origin(self, origin: tuple[int, int]) -> None:
        self.origin = origin
        self.rect.x, self.rect.y = origin
        if self.center is not None:
            self.center = self.rect.center
