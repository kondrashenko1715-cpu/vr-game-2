from __future__ import annotations
import os

# Фиксируем стабильный мобильный графический бэкенд
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import RenderContext, Color, Mesh, PushMatrix, PopMatrix, Translate, Rotate
from kivy.graphics.opengl import glEnable, GL_DEPTH_TEST, glClearColor
from kivy.core.window import Window
from kivy.clock import Clock

class PhysicsVRScene(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        
        # Размеры экрана
        self.win_w = Window.width
        self.win_h = Window.height
        
        # 1. Параметры пола (на уровне ног)
        self.floor_y = 50
        
        # 2. Параметры БОЛЬШОГО коричневого куба (стола)
        self.table_x = self.win_w / 2
        self.table_y = self.floor_y + 100  # Стоит на полу
        self.table_w = 400  # Ширина стола
        self.table_h = 200  # Высота стола
        
        # 3. Параметры МАЛЕНЬКОГО оранжевого куба
        self.cube_x = self.win_w / 2
        self.cube_y = 500  # Начинает высоко в воздухе
        self.cube_size = 80  # Маленький размер
        
        # Физические переменные
        self.is_grabbed = False
        self.velocity_y = 0  # Скорость падения
        self.gravity = -0.8  # Сила притяжения
        
        # Общие 3D-вершины для кубов (центрированные относительно их осей)
        self.vertices = [
            # Передняя грань
            -0.5, -0.5,  0.5, 0, 0,   0.5, -0.5,  0.5, 1, 0,   0.5,  0.5,  0.5, 1, 1,  -0.5,  0.5,  0.5, 0, 1,
            # Задняя грань
            -0.5, -0.5, -0.5, 0, 0,  -0.5,  0.5, -0.5, 1, 0,   0.5,  0.5, -0.5, 1, 1,   0.5, -0.5, -0.5, 0, 1,
        ]
        self.indices = 
        
        # Запускаем игровой цикл физики (60 кадров в секунду)
        Clock.schedule_interval(self.update_physics, 1.0 / 60.0)
        Clock.schedule_once(self.enable_vr_environment, 0)

    def enable_vr_environment(self, dt):
        glEnable(GL_DEPTH_TEST)
        # Насильно перекрашиваем фон в глубокий черный космос!
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def draw_cube(self, x, y, size_w, size_h, size_z, r, g, b, angle_rot):
        PushMatrix()
        Translate(x, y, 0)
        Rotate(angle=angle_rot, axis=(1, 1, 0))
        # Масштабируем базовые вершины под нужный размер куба/стола
        Translate(0, 0, 0)
        Color(r, g, b, 1.0)
        
        # Создаем вершины с учетом масштаба
        scaled_vertices = []
        for i in range(0, len(self.vertices), 5):
            scaled_vertices.extend([self.vertices[i]*size_w, self.vertices[i+1]*size_h, self.vertices[i+2]*size_z, self.vertices[i+3], self.vertices[i+4]])
            
        Mesh(
            vertices=scaled_vertices,
            indices=self.indices,
            fmt=[(b'vPosition', 3, b'float'), (b'vTexCoords0', 2, b'float')],
            mode='triangles'
        )
        PopMatrix()

    def render_scene(self):
        self.canvas.clear()
        with self.canvas:
            # 1. Рисуем бесконечный черный пол (линия-платформа на уровне ног)
            PushMatrix()
            Color(0.2, 0.2, 0.2, 1.0) # Темно-серый ориентир пола
            Mesh(
                vertices=[0, self.floor_y, 0, 0, 0,  self.win_w, self.floor_y, 0, 1, 0,  self.win_w, self.floor_y-10, 0, 1, 1,  0, self.floor_y-10, 0, 0, 1],
                indices=[0, 1, 2, 2, 3, 0],
                fmt=[(b'vPosition', 3, b'float'), (b'vTexCoords0', 2, b'float')],
                mode='triangles'
            )
            PopMatrix()
            
            # 2. Рисуем БОЛЬШОЙ КОРИЧНЕВЫЙ КУБ (Стол со стабильной коллизией)
            # Цвет: Коричневый (R:0.5, G:0.3, B:0.1)
            self.draw_cube(self.table_x, self.table_y, self.table_w, self.table_h, 300, 0.5, 0.3, 0.1, 15)
            
            # 3. Рисуем МАЛЕНЬКИЙ ОРАНЖЕВЫЙ КУБ (Физический объект)
            # Цвет: Оранжевый (R:1.0, G:0.5, B:0.0)
            self.draw_cube(self.cube_x, self.cube_y, self.cube_size, self.cube_size, self.cube_size, 35, 1.0, 0.5, 0.0)

    def update_physics(self, dt):
        if not self.is_grabbed:
            # Применяем гравитацию, если кубик отпущен
            self.velocity_y += self.gravity
            self.cube_y += self.velocity_y
            
            # КОЛЛИЗИЯ СО СТОЛОМ (Проверяем падение на коричневый куб)
            table_top = self.table_y + (self.table_h / 2) + (self.cube_size / 2)
            table_left = self.table_x - (self.table_w / 2)
            table_right = self.table_x + (self.table_w / 2)
            
            if table_left < self.cube_x < table_right:
                if self.cube_y <= table_top and self.cube_y + abs(self.velocity_y) >= table_top - 20:
                    self.cube_y = table_top
                    self.velocity_y = 0  # Останавливаем падение
            
            # КОЛЛИЗИЯ С ПОЛОМ (Если пролетел мимо стола — падает на пол на уровне ног)
            floor_top = self.floor_y + (self.cube_size / 2)
            if self.cube_y < floor_top:
                self.cube_y = floor_top
                self.velocity_y = 0  # Встает на пол
                
        self.render_scene()

    def on_touch_down(self, touch):
        # Хватаем маленький оранжевый кубик передней кнопкой контроллера
        if abs(touch.x - self.cube_x) < 100 and abs(touch.y - self.cube_y) < 100:
            self.is_grabbed = True
            self.velocity_y = 0
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        # Двигаем кубик вслед за лучом руки
        if touch.grab_current is self and self.is_grabbed:
            self.cube_x = touch.x
            self.cube_y = touch.y
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        # Отпускаем переднюю кнопку — активируется гравитация и кубик летит вниз!
        if touch.grab_current is self:
            self.is_grabbed = False
            touch.ungrab(self)
            return True
        return super().on_touch_up(touch)

class PicoVRApp(App):
    def build(self):
        Window.fullscreen = True
        return PhysicsVRScene()

if __name__ == '__main__':
    PicoVRApp().run()
