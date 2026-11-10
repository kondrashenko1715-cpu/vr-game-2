from __future__ import annotations
import os

# Фиксируем мобильный графический бэкенд
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class PicoCubeApp(App):
    def build(self):
        # Насильно заставляем окно растянуться под линзы шлема
        Window.fullscreen = True
        
        layout = BoxLayout(orientation='vertical')
        
        # Создаем яркую, гарантированно работающую кнопку-панель
        btn = Button(
            text='🚀 PICO 4 PYTHON VR READY! 🚀',
            font_size='32sp',
            background_color=(1.0, 0.5, 0.0, 1.0) # Наш фирменный оранжевый цвет!
        )
        
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    PicoCubeApp().run()
