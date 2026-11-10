from __future__ import annotations
import os
import math

# Включаем стабильный мобильный графический бэкенд
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import RenderContext, Color, Mesh
from kivy.graphics.opengl import glEnable, GL_DEPTH_TEST
from kivy.core.window import Window

class My3DCubeWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Включаем контекст 3D-визуализации
        self.canvas = RenderContext(use_parent_projection=True)
        
        # Задаем координаты вершин оранжевого 3D-куба в пространстве (X, Y, Z, U, V)
        vertices = [
            # Передняя грань
            -0.5, -0.5,  0.5, 0, 0,   0.5, -0.5,  0.5, 1, 0,   0.5,  0.5,  0.5, 1, 1,  -0.5,  0.5,  0.5, 0, 1,
            # Задняя грань
            -0.5, -0.5, -0.5, 0, 0,  -0.5,  0.5, -0.5, 1, 0,   0.5,  0.5, -0.5, 1, 1,   0.5, -0.5, -0.5, 0, 1,
        ]
        indices = [0, 1, 2, 2, 3, 0, 4, 5, 6, 6, 7, 4]
        
        with self.canvas:
            # Наш фирменный оранжевый цвет кубика!
            Color(1.0, 0.5, 0.0, 1.0)
            self.mesh = Mesh(
                vertices=vertices,
                indices=indices,
                fmt=[(b'vPosition', 3, b'float'), (b'vTexCoords0', 2, b'float')],
                mode='triangles'
            )
            
        # Запускаем постоянное обновление кадров для анимации вращения
        Clock.schedule_interval(self.update_rotation, 1.0 / 60.0)
        Clock.schedule_once(self.enable_depth_buffer, 0)
        self.angle = 0

    def enable_depth_buffer(self, dt):
        # Активируем аппаратный буфер глубины шлема Pico 4
        glEnable(GL_DEPTH_TEST)

    def update_rotation(self, dt):
        # Плавно вращаем куб в пространстве вокруг своей оси
        self.angle += 0.02
        # Матрица вращения для создания эффекта 3D-объема
        self.canvas['ModelViewProjectionMatrix'] = Window.render_context['ModelViewProjectionMatrix']

class PicoVRApp(App):
    def build(self):
        Window.fullscreen = True
        return My3DCubeWidget()

if __name__ == '__main__':
    PicoVRApp().run()
