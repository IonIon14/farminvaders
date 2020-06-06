import pygame
import pyglet
from pyglet.window import key
from pyglet.window import mouse
import pyglet.graphics as gl
import main

pygame.init()

animation=pyglet.image.load_animation("game_gif.gif")
anime_sprite=pyglet.sprite.Sprite(animation)
mute_volume=pyglet.image.load_animation('audio_off_volume.gif')
w=800
h=560
window=pyglet.window.Window(width=w,height=h,caption="Farm Invaders",resizable=None)
icon=pyglet.image.load('ufo.png')
window.set_icon(icon)
r,g,b,alpha=0.5,0.5,0.8,0.5
pyglet.gl.glClearColor(r,g,b,alpha)
music=pyglet.media.load('song.wav')
silence=pyglet.media.load('silence.wav')
player=pyglet.media.Player()



Intro_text=pyglet.text.Label('Farm Invaders',font_name='Retro Gaming',font_size=50,x=window.width//2,y=window.height-100,anchor_y='center',anchor_x='center',color=(210,30,20,150))
volume_text=pyglet.text.Label("Volume",font_name='Retro Gaming',font_size=25,x=660,y=360,anchor_x='center',anchor_y='center',color=(210,30,20,150))
volume_25=pyglet.graphics.vertex_list(4, 'v2f', 'c3B',)
continue_button=pyglet.text.Label('Press Space to continue',font_name='Retro Gaming',font_size=20,x=window.width//2,y=window.height-450,anchor_y='center',anchor_x='center',color=(210,30,20,150))
quit_button=pyglet.text.Label('Press Escape to quit',font_name='Retro Gaming',font_size=20,x=window.width//2,y=window.height-500,anchor_y='center',anchor_x='center',color=(210,30,20,150))

@window.event


def on_draw():
    window.clear()
    anime_sprite.draw()
    Intro_text.draw()
    volume_text.draw()
    continue_button.draw()
    quit_button.draw()

@window.event

def on_key_press(key,modifier):
    if key == pyglet.window.key.SPACE:
        print('Spacebar was pressed!')
        pyglet.app.EventLoop().exit()
        if __name__=='__main__':
            window.close()
            main.gameplay()
    else:
        if key==pyglet.window.key.ESCAPE:
            pyglet.app.EventLoop().exit()
            window.close()

@window.event
def on_mouse_press(x,y,buttons,modifiers):
    if buttons ==mouse.LEFT:
        print("Left Mouse is pressed\n")
        print("Coordinates:",x,y)
        if (x>=590 or x<=x+26) and (y>=130 or y<=x+26):
            print("Mute button is pressed")
            player.pause()
    else:
        if buttons ==mouse.RIGHT:
            print("Right Mouse is pressed\n")
            print("Coordinates:",x,y)

music.play()

pyglet.app.run()








