from __future__ import annotations
import os

# Включаем стабильный мобильный графический бэкенд
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.graphics import RenderContext, Color, Mesh
from kivy.graphics.opengl import glEnable, GL_DEPTH_TEST
from kivy.core.window import Window

class My3DCubeWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        
        # Точные координаты вершин оранжевого 3D-куба (X, Y, Z, U, V)
        vertices = [
            -0.5, -0.5,  0.5, 0, 0,
             0.5, -0.5,  0.5, 1, 0,
             0.5,  0.5,  0.5, 1, 1,
            -0.5,  0.5,  0.5, 0, 1,
            -0.5, -0.5, -0.5, 0, 0,
            -0.5,  0.5, -0.5, 1, 0,
             0.5,  0.5, -0.5, 1, 1,
             0.5, -0.5, -0.5, 0, 1,
        ]
        
        # ИСПРАВЛЕНО: Прописали четкие индексы соединения точек в треугольники, чтобы избежать вылета!
        indices = [0, 1, 2, 2, 3, 0,  4, 5, 6, 6, 7, 4]
        
        with self.canvas:
            Color(1.0, 0.5, 0.0, 1.0) # Наш фирменный оранжевый цвет!
            self.mesh = Mesh(
                vertices=vertices,
                indices=indices,
                fmt=[(b'vPosition', 3, b'float'), (b'vTexCoords0', 2, b'float')],
                mode='triangles'
            )
            
        Clock.schedule_once(self.enable_depth_buffer, 0)

    def enable_depth_buffer(self, dt):
        glEnable(GL_DEPTH_TEST)

class PicoVRApp(App):
    def build(self):
        Window.fullscreen = True
        root = BoxLayout()
        root.add_widget(My3DCubeWidget())
        return root

if __name__ == '__main__':
    PicoVRApp().run()
