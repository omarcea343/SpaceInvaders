import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.image.load('../graphics/asteroid.png').convert_alpha()  # Cambia la ruta a la ubicación de tu archivo asteroid.png
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))