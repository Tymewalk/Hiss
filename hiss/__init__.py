import pygame

class Sprite():
    def __init__(self, name):
        self.name = name
        self.costumes = []

    def addCostume(self, costumePath):
        costume = pygame.image.load(costumePath)
        self.costumes.append(costume)
