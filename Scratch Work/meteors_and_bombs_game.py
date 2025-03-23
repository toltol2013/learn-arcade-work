"""
This adapts the previous static coin collector game by the player shooting bullets to destroy the coins
The main changes to the code are as follows:
1. we create a 3rd sprite list to handle the bullets
2. the mouse movement function is changed so the player can only move left/right
3. a new mouse click function creates a bullet when the mouse is clicked, positions it, and adds it to the
   bullet sprite list
4. the window class update function has a new loop added - this loops through the bullet list and checks if
   the bullet has hit a coin, if so the bullet and coin are removed and the score increased. Also, if the
   bullet has moved off the top of the screen the bullet is removed.
"""


import random
import arcade
import time

METEORIT_SCALING = 1
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.3
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 30
METEORIT_COUNT = 3
BOMB_COUNT = 8
BOMB_SCALING = 1


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5

class CreateShip(arcade.Sprite):
    def update(self):
        pass

class Coin(arcade.Sprite):
    def update(self):
        self.center_y -= 0.5
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT

class CreateSprite(arcade.Sprite):
    def update(self):
        self.center_y -= 1
        if self.center_y < 40:
            self.center_y = SCREEN_HEIGHT - 40


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        # Variables that will hold sprite lists
        self.start_time = None
        self.big_explosion = None
        self.big_explosion_list = None
        self.small_explosion_list = None
        self.small_explosion = None
        self.bomb_list = None
        self.small_meteorit_list = None
        self.medium_meteorit_list = None
        self.big_meteorit_list = None
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.medium_meteorit = None
        self.big_meteorit = None
        self.small_meteorit = None
        self.bomb = None
        
        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.lives = 5

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)
        self.laser_sound = arcade.load_sound("laser.wav")
        self.boom_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.big_explosion_list = arcade.SpriteList()
        self.small_explosion_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.small_meteorit_list = arcade.SpriteList()
        self.medium_meteorit_list = arcade.SpriteList()
        self.big_meteorit_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the score
        self.score = 0
        self.lives = 5
        # Set up the player

        # Image from builtin resources
        for i in range(METEORIT_COUNT):
            self.big_meteorit = CreateSprite("big_meteor.png", METEORIT_SCALING)
            self.big_meteorit.center_x = random.randint(40, SCREEN_WIDTH - 40)
            self.big_meteorit.center_y = random.randint(300, SCREEN_HEIGHT)
            self.big_meteorit_list.append(self.big_meteorit)
            
        for i in range(BOMB_COUNT):
            self.bomb = CreateSprite("bomb.png", BOMB_SCALING)
            self.bomb.center_x = random.randint(40, SCREEN_WIDTH)
            self.bomb.center_y = random.randint(400, SCREEN_HEIGHT)
            self.bomb_list.append(self.bomb)

        self.player_sprite = CreateShip("playerShip2_blue.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from builtin resources
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randint(30, SCREEN_WIDTH - 30)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.small_explosion_list.draw()
        self.big_explosion_list.draw()
        self.bomb_list.draw()
        self.small_meteorit_list.draw()
        self.medium_meteorit_list.draw()
        self.big_meteorit_list.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 20)
        arcade.draw_text(f"lives: {self.lives}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x


    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)
        arcade.play_sound(self.laser_sound)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90
        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        bullet.change_y = BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.player_sprite.update()
        self.small_explosion_list.update()
        self.big_explosion_list.update()
        self.bomb_list.update()
        self.small_meteorit_list.update()
        self.medium_meteorit_list.update()
        self.big_meteorit_list.update()
        self.coin_list.update()
        self.bullet_list.update()



        for meteor in self.big_meteorit_list:
            if meteor.center_y < 42:
                self.score -= 3

        for meteor2 in self.medium_meteorit_list:
            if meteor2.center_y < 42:
                self.score -= 2

        for meteor3 in self.small_meteorit_list:
            if meteor3.center_y < 42:
                self.score -= 1

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            hit_list2 = arcade.check_for_collision_with_list(bullet, self.big_meteorit_list)
            hit_list3 = arcade.check_for_collision_with_list(bullet, self.medium_meteorit_list)
            hit_list4 = arcade.check_for_collision_with_list(bullet, self.small_meteorit_list)
            hit_list5 = arcade.check_for_collision_with_list(bullet, self.bomb_list)
            hit_list6 = arcade.check_for_collision_with_list(self.player_sprite, self.bomb_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.boom_sound)
                coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

                coin.center_x = random.randint(30, SCREEN_WIDTH - 30)
                coin.center_y = SCREEN_HEIGHT
                self.coin_list.append(coin)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

            if len(hit_list2) > 0:
                self.score += 1
                for meteor in hit_list2:
                    meteor.remove_from_sprite_lists()
                    self.medium_meteorit = CreateSprite("medium_meteor.png", 1)
                    self.medium_meteorit.center_x = meteor.center_x
                    self.medium_meteorit.center_y = meteor.center_y
                    self.medium_meteorit_list.append(self.medium_meteorit)
                    bullet.remove_from_sprite_lists()

            if len(hit_list3) > 0:
                self.score += 2
                for meteor1 in hit_list3:
                    self.small_meteorit = CreateSprite("small_meteor.png", METEORIT_SCALING)
                    self.small_meteorit.center_x = meteor1.center_x
                    self.small_meteorit.center_y = meteor1.center_y
                    self.small_meteorit_list.append(self.small_meteorit)
                    meteor1.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()

            if len(hit_list4) > 0:
                self.score += 3
                for meteor2 in hit_list4:
                    meteor2.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()
                    self.big_meteorit = CreateSprite("big_meteor.png", METEORIT_SCALING)
                    self.big_meteorit.center_x = random.randint(40, SCREEN_WIDTH - 40)
                    self.big_meteorit.center_y = SCREEN_HEIGHT
                    self.big_meteorit_list.append(self.big_meteorit)

            if len(hit_list5) > 0:
                self.score += 1
                for bomb in hit_list5:
                    bomb.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()
                    self.small_explosion = arcade.Sprite("explosion2.png", 1)
                    self.small_explosion.center_x = bomb.center_x
                    self.small_explosion.center_y = bomb.center_y
                    self.small_explosion.creation_time = time.time()
                    self.small_explosion_list.append(self.small_explosion)

            if len(hit_list6) > 0:
                print(f"Collision détectée avec {len(hit_list6)} bombes")
                for bomb in hit_list6:
                    bomb.remove_from_sprite_lists()
                    self.lives -= 1
                    self.small_explosion = arcade.Sprite("explosion2.png", 1)
                    self.small_explosion.center_x = bomb.center_x
                    self.small_explosion.center_y = bomb.center_y
                    self.small_explosion.creation_time = time.time()
                    self.small_explosion_list.append(self.small_explosion)
                    print("Explosion")

        for explosion in self.small_explosion_list:
            if time.time() - explosion.creation_time > 5:
                explosion.remove_from_sprite_lists()
def main():
    CreateSprite()
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
