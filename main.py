from __future__ import annotations
import os

# Фиксируем настройки графики Kivy для мобильного шлема
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics.opengl import glEnable, glDisable, GL_DEPTH_TEST
from kivy.graphics import RenderContext, Color, Rectangle

# Простейший шейдер для отрисовки 3D-графики в Pico 4
GLSL_SHADER = """
$HEADER$
void main(void) {
    gl_FragColor = vec4(1.0, 0.5, 0.0, 1.0); // Яркий оранжевый цвет куба
}
"""

class Cube3DWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Включаем специальный контекст визуализации для 3D
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.fs = GLSL_SHADER
        
        with self.canvas:
            Color(1.0, 0.5, 0.0, 1.0)
            # Базовая сетка под отрисовку нашего кубика
            self.rect = Rectangle(position=self.pos, size=self.size)
            
        self.bind(position=self._update_rect, size=self._update_rect)
        Clock.schedule_once(self.enable_depth, 0)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def enable_depth(self, dt):
        # Активируем аппаратный буфер глубины шлема Pico 4
        glEnable(GL_DEPTH_TEST)

class PicoVRApp(App):
    def build(self):
        return Cube3DWidget()

if __name__ == '__main__':
    PicoVRApp().run()
