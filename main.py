from __future__ import annotations
import os

# Фиксируем стабильный мобильный графический бэкенд
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import RenderContext, Color, Rectangle, PushMatrix, PopMatrix, Translate
from kivy.graphics.opengl import glEnable, GL_DEPTH_TEST, glClearColor
from kivy.core.window import Window
from kivy.clock import Clock

class SpacePhysicsVRScene(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        
        self.win_w = Window.width
        self.win_h = Window.height
        
        # 1. Наш оранжевый космический кубик
        self.cube_x = self.win_w / 2
        self.cube_y = self.win_h / 2
        self.cube_size = 90
        
        # Переменные космической инерции
        self.is_grabbed = False
        self.velocity_x = 0  # Скорость полета по горизонтали
        self.velocity_y = 0  # Скорость полета по вертикали
        
        # Коэффициент космического трения (чем ближе к 1.0, тем дольше летит куб)
        self.friction = 0.96 
        
        # Для расчета скорости броска запоминаем прошлую точку руки
        self.last_touch_x = 0
        self.last_touch_y = 0
        
        Clock.schedule_interval(self.update_space_physics, 1.0 / 60.0)
        Clock.schedule_once(self.setup_gl, 0)

    def setup_gl(self, dt):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0) # Глубокий черный космос вокруг

    def draw_cube(self, x, y, w, h, r, g, b):
        with self.canvas:
            PushMatrix()
            Translate(x, y, 0)
            Color(r, g, b, 1.0)
            Rectangle(pos=(-w/2, -h/2), size=(w, h))
            PopMatrix()

    def update_space_physics(self, dt):
        self.canvas.clear()
        
        # Если куб летит сам (отпущен)
        if not self.is_grabbed:
            # Двигаем куб по инерции
            self.cube_x += self.velocity_x
            self.cube_y += self.velocity_y
            
            # Плавно гасим скорость трением космоса, чтобы он остановился по физике
            self.velocity_x *= self.friction
            self.velocity_y *= self.friction
            
            # Если подлетел к краю экрана — мягко отскакивает, как в невесомости
            if self.cube_x < self.cube_size/2 or self.cube_x > self.win_w - self.cube_size/2:
                self.velocity_x *= -0.8
            if self.cube_y < self.cube_size/2 or self.cube_y > self.win_h - self.cube_size/2:
                self.velocity_y *= -0.8
                
        # Рисуем наш оранжевый кубик посреди космоса
        self.draw_cube(self.cube_x, self.cube_y, self.cube_size, self.cube_size, 1.0, 0.5, 0.0)

    def on_touch_down(self, touch):
        # Хватаем кубик передним триггером контроллера
        if abs(touch.x - self.cube_x) < 120 and abs(touch.y - self.cube_y) < 120:
            self.is_grabbed = True
            self.velocity_x = 0
            self.velocity_y = 0
            self.last_touch_x = touch.x
            self.last_touch_y = touch.y
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self and self.is_grabbed:
            # Считаем, с какой скоростью и куда сейчас движется рука
            self.velocity_x = touch.x - self.last_touch_x
            self.velocity_y = touch.y - self.last_touch_y
            
            # Обновляем координаты куба вслед за рукой
            self.cube_x = touch.x
            self.cube_y = touch.y
            
            # Запоминаем текущую точку для следующего кадра
            self.last_touch_x = touch.x
            self.last_touch_y = touch.y
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.is_grabbed = False
            touch.ungrab(self)
            return True
        return super().on_touch_up(touch)

class PicoVRApp(App):
    def build(self):
        Window.fullscreen = True
        return SpacePhysicsVRScene()

if __name__ == '__main__':
    PicoVRApp().run()
