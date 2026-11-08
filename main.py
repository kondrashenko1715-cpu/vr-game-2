from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics.opengl import *
from kivy.graphics import Callback

class VRGameCube(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        with self.canvas:
            Callback(self.draw_vr_scene)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        self.angle += 1

    def draw_vr_scene(self, instr):
        # Используем встроенные в Kivy константы OpenGL ES 2
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        glTranslatef(0.0, 0.0, -3.0)
        glRotatef(self.angle, 1, 1, 0)

        size = 0.6
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.5, 0.0)
        glVertex3f(-size, -size, size); glVertex3f(size, -size, size)
        glVertex3f(size, size, size); glVertex3f(-size, size, size)
        glVertex3f(-size, -size, -size); glVertex3f(-size, size, -size)
        glVertex3f(size, size, -size); glVertex3f(size, -size, -size)
        glEnd()

class MainApp(App):
    def build(self):
        return VRGameCube()

if __name__ == '__main__':
    MainApp().run()
