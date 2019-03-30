# Configuration file for the Scooter class
import pygame
pygame.init()

CONFIG = {
	"FILENAME": "SCOOTER.png",
	"CONTROLS": {
		"LEFT": pygame.K_LEFT,
		"RIGHT": pygame.K_RIGHT,
		"UP": pygame.K_UP
		},
	"TURN_DEGREES": 2,
	"SPEED": 3.5,
	"ACCELERATION_FACTOR": 0.02,
	"BRAKE_FACTOR": 0.05
	}
