from __future__ import annotations
import os

# Фиксируем стабильный мобильный графический бэкенд
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import RenderContext, Color, Rectangle, PushMatrix, PopMatrix, Translate
from kivy.graphics.opengl import glEnable, GL_DEPTH_TEST
from kivy.core.window import Window

class Interactive3DCube(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        
        # Начальные координаты куба (космический центр экрана)
        self.cube_x = Window.width / 2
        self.cube_y = Window.height / 2
        
        # Флаг: схватили ли мы куб боковой кнопкой контроллера/руки
        self.is_grabbed = False
        
        # Отрисовываем графику
        self.render_scene()
        Clock = None # Заглушка, используем стандартное обновление canvas
        glEnable(GL_DEPTH_TEST)

    def render_scene(self):
        # Очищаем старую графику и рисуем куб в новых координатах руки
        self.canvas.clear()
        with self.canvas:
            PushMatrix()
            # Переносим куб в точку, где находится рука/курсор
            Translate(self.cube_x, self.cube_y, 0)
            Color(1.0, 0.5, 0.0, 1.0) # Наш оранжевый цвет
            Rectangle(pos=(-150, -150), size=(300, 300))
            PopMatrix()

    def on_touch_down(self, touch):
        # Если луч от контроллера/руки попал в область куба при нажатии боковой кнопки
        if abs(touch.x - self.cube_x) < 150 and abs(touch.y - self.cube_y) < 150:
            self.is_grabbed = True
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        # Если куб схвачен — он плавно двигается вслед за вашей рукой в VR-пространстве!
        if touch.grab_current is self and self.is_grabbed:
            self.cube_x = touch.x
            self.cube_y = touch.y
            self.render_scene() # Мгновенно перерисовываем куб в новой точке
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        # Когда отпускаем боковую кнопку — рука разжимается, куб остается на месте
        if touch.grab_current is self:
            self.is_grabbed = False
            touch.ungrab(self)
            return True
        return super().on_touch_up(touch)

class PicoVRApp(App):
    def build(self):
        Window.fullscreen = True
        return Interactive3DCube()

if __name__ == '__main__':
    PicoVRApp().run()
