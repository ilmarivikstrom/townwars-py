from abc import ABC, abstractmethod

import pygame as pg


class Component(ABC):
    @abstractmethod
    def handle_event(self, event: pg.event.Event) -> None:
        """Handle Pygame events like mouse clicks or key presses."""

    @abstractmethod
    def update(self) -> None:
        """Update component state (e.g., position, animations)."""

    @abstractmethod
    def draw(self, screen: pg.Surface) -> None:
        """Draw the component to the given surface."""
