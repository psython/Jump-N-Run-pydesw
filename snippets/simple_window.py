#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simple_window.py
#  
#  Copyright 2016 psython
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class NewGame(object):
    
    def __init__(self, width, height, framerate, background):
        pygame.init()
        self.width = width
        self. height = height
        self.framerate = framerate
        self.background = background
        self.game_over = False
        self.main_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                
    def update_frame(self):
        self.main_window.fill(self.background)
        pygame.display.flip()
        
    def quit_game(self):
        pygame.quit()
    
    def looping(self):
        while not self.game_over:
            self.clock.tick(self.framerate)
            self.get_events()
            self.update_frame()
        self.quit_game()
        
def main(args):
    new_game = NewGame(1024, 768, 60, GREEN)
    new_game.looping()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
