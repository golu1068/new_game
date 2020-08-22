import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle,Line,RoundedRectangle
from functools import partial
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '500')
#from kivy.core.window import Window
#Window.size = (300, 100)
###########################################################################################
class make_circle(FloatLayout):
    def __init__(self,btn, **kwargs):
        super(make_circle, self).__init__(**kwargs)
        with btn.canvas.after:
            btn.line = Line(circle=(btn.center_x, btn.center_y, btn.size[1]/3), width=2)
            
        btn.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, instance, value):
        instance.line.circle = (instance.center_x, instance.center_y, instance.size[1]/3)
#        instance.line.width = instance.width
            
class make_cross(FloatLayout):
    def __init__(self,btn, **kwargs):
        super(make_cross, self).__init__(**kwargs)
        with btn.canvas.after:
            Color(1., 0, 0, 1)
            btn.line1 = Line(points=[btn.center_x - btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x + btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=2)
            btn.line2 = Line(points=[btn.center_x + btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x - btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=2)
    
        btn.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, instance, value):
        instance.line1.points = [instance.center_x - instance.size[0]/3, instance.center_y + instance.size[1]/3, instance.center_x + instance.size[0]/3, 
                                    instance.center_y - instance.size[1]/3]
        instance.line2.points = [instance.center_x + instance.size[0]/3, instance.center_y + instance.size[1]/3, instance.center_x - instance.size[0]/3, 
                                    instance.center_y - instance.size[1]/3]
#        instance.line.size = instance.size
    
def button_click(f2, f3, btn):
    btn.disabled = True
    if (f3.canvas.before.children[0].rgba == [0,1,0,0.5]):
        draw = 1
        make_cross(btn)
        f2.canvas.before.children[0].rgba = [0,1,0,0.5]
        f3.canvas.before.children[0].rgba = [1,1,1,0.5]
    else:
        draw = 0
        make_circle(btn)
        f3.canvas.before.children[0].rgba = [0,1,0,0.5]
        f2.canvas.before.children[0].rgba = [1,1,1,0.5]

class lyt(FloatLayout):
    def __init__(self, **kwargs):
        super(lyt, self).__init__(**kwargs)
        
        with self.canvas.before:
#            Color(1, 1, 0, 0.1) # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size,
                               pos=self.pos)
            self.rect.source = 'main_lyt.jpg'
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        ################################################################################
        self.f1 = FloatLayout()
#        self.f1 = FloatLayout(size_hint=(self.size_hint[0]*0.6,self.size_hint[1]*0.6), 
#                         pos_hint={'center_x':self.center_x/100, 'center_y':self.center_y/83})
        self.add_widget(self.f1)
        
        with self.f1.canvas.before:
            Color(1,1,1,1) # green; colors range from 0-1 instead of 0-255
            self.f1.rect1 = RoundedRectangle(size=self.f1.size,
                               pos=self.f1.pos)
        
        self.f1.bind(pos=self.update_rect1, size=self.update_rect1)
        ############################################################################################
        with self.f1.canvas.before:
            Color(1, 0, 0, 1)
            self.f1.line1 = Line(points=[], width=5)
            self.f1.line2 = Line(points=[], width=5)
            self.f1.line3 = Line(points=[], width=5)
            self.f1.line4 = Line(points=[], width=5)
        
        self.f1.bind(pos=self.update_rect2, size=self.update_rect2)
#        self.f1.bind(pos=self.update_rect2, size=partial(self.update_rect2, 'ljvn'))
#       ###########################################################################################
        self.b1 = Button(text=str(0),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.05, 'y': 0.71}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b1)
        
        self.b2 = Button(text=str(1),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.36, 'y': 0.71}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b2)
        
        self.b3 = Button(text=str(2),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.67, 'y': 0.71}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b3)
##        #########################################################################################
        self.b4 = Button(text=str(3),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.05, 'y': 0.556}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b4)
        
        self.b5 = Button(text=str(4),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.36, 'y': 0.556}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b5)
        
        self.b6 = Button(text=str(5),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.67, 'y': 0.556}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b6)
#        ###########################################################################################
        self.b7 = Button(text=str(6),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.05, 'y': 0.4}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b7)
        
        self.b8 = Button(text=str(7),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.36, 'y': 0.4}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b8)
        
        self.b9 = Button(text=str(8),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.67, 'y': 0.4}, background_color =(1,1,1,1), color=[0,0,0,1])
        self.f1.add_widget(self.b9)
##########################################################################################################################
        self.f2 = FloatLayout()
        self.add_widget(self.f2)

        with self.f2.canvas.before:
            Color(1,1,1,0.5) # green; colors range from 0-1 instead of 0-255
            self.f2.rect5 = RoundedRectangle(size=self.f2.size,
                               pos=self.f2.pos)
            self.f2.l1 =  Label(text="Computer", font_size=13, color=(0, 0, 0, 1))
            Color(1,0,0,0.5)
            self.f2.line5 = Line(circle=(self.f2.size[0]+20, self.f2.size[1]-20, self.f2.size[1]/3), width=2)
        
        self.f2.bind(pos=self.update_rect5, size=self.update_rect5)
        
        ###############################################################################################
        self.f3 = FloatLayout()
        self.add_widget(self.f3)

        with self.f3.canvas.before:
            Color(0,1,0,.5) # green; colors range from 0-1 instead of 0-255
            self.f3.rect6 = RoundedRectangle(size=self.f3.size,
                               pos=self.f3.pos)
            self.f3.l2 =  Label(text="Player", font_size=13, color=(0, 0, 0, 1))
            Color(1,0,0,0.5)
            self.f3.line6 = Line(points=[self.f3.center_x - self.f3.size[0]/4, self.f3.center_y + self.f3.size[1]/4, 
                                         self.f3.center_x + self.f3.size[0]/4, self.f3.center_y - self.f3.size[1]/4], width=2)
            self.f3.line7 = Line(points=[self.f3.center_x + self.f3.size[0]/4, self.f3.center_y + self.f3.size[1]/4, 
                                         self.f3.center_x - self.f3.size[0]/4, self.f3.center_y - self.f3.size[1]/4], width=2)
        
        self.f3.bind(pos=self.update_rect6, size=self.update_rect6)
        #############################################################################################
#       #########################################################################################
##        self.b1.bind(on_press = partial(make_cross, self.b1))
##        self.b2.bind(on_press = partial(make_circle, self.b2))
##        self.b3.bind(on_press = partial(make_circle, self.b3))
##        self.b4.bind(on_press = partial(make_circle, self.b4))
##        self.b5.bind(on_press = partial(make_circle, self.b5))
##        self.b6.bind(on_press = partial(make_circle, self.b6))
##        self.b7.bind(on_press = partial(make_circle, self.b7))
##        self.b8.bind(on_press = partial(make_circle, self.b8))
##        self.b9.bind(on_press = partial(make_cross, self.b9))
#        
        self.b1.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b2.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b3.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b4.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b5.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b6.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b7.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b8.bind(on_press = partial(button_click, self.f2, self.f3))
        self.b9.bind(on_press = partial(button_click, self.f2, self.f3))
        #############################################################################################
    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
    
    def update_rect1(self, instance, value):
#        print(instance)
#        print(instance.rect1.pos)
#        print(instance.rect1.size)
        instance.rect1.pos = (instance.size[0]*0.05 ,instance.size[1]*0.4 )
        instance.rect1.size = (instance.size[0]*0.9 ,instance.size[1]*0.45)
    
    def update_rect2(self, instance, value):
#        print(instance)
#        print(instance.rect1.pos)
#        print(instance.rect1.size)
        instance.line1.points = [instance.rect1.pos[0]+instance.rect1.size[0]/3, instance.rect1.pos[1]+instance.rect1.size[1]/1,
                                 instance.rect1.pos[0]+instance.rect1.size[0]/3, instance.rect1.pos[1]] 
    
        instance.line2.points = [instance.rect1.pos[0]+instance.rect1.size[0]*(2/3), instance.rect1.pos[1]+instance.rect1.size[1]/1,
                                 instance.rect1.pos[0]+instance.rect1.size[0]*(2/3), instance.rect1.pos[1]] 

        instance.line3.points = [instance.rect1.pos[0], instance.rect1.pos[1]+instance.rect1.size[1]*(2/3),
                                 instance.rect1.pos[0]+instance.rect1.size[0], instance.rect1.pos[1]+instance.rect1.size[1]*(2/3)]
        
        instance.line4.points = [instance.rect1.pos[0], instance.rect1.pos[1]+instance.rect1.size[1]*(1/3),
                                 instance.rect1.pos[0]+instance.rect1.size[0], instance.rect1.pos[1]+instance.rect1.size[1]*(1/3)]    
    
    def update_rect5(self, instance, value):
        instance.rect5.pos = (self.pos[0]+self.size[0]*0.1,self.pos[1]+self.size[1]*0.1)
        instance.rect5.size = (self.size[0]*0.3, self.size[1]/2*0.3)
        instance.l1.pos = (self.pos[0]+self.size[0]*0.05, self.pos[1]+self.size[1]*0.125)
        instance.line5.circle = (self.pos[0]+self.size[0]*0.25, self.pos[1]+self.size[1]*0.155, instance.rect5.size[0]/3.5)
        
    def update_rect6(self, instance, value):
        instance.rect6.pos = (self.pos[0]+self.size[0]*0.6,self.pos[1]+self.size[1]*0.1)
        instance.rect6.size = (self.size[0]*0.3, self.size[1]/2*0.3)
#        instance.l2.pos = (self.pos[0]+self.size[0]*0.55, self.pos[1]+self.size[1]*0.125)
        instance.l2.pos = (instance.rect6.pos[0]-instance.rect6.size[0]*0.15, instance.rect6.pos[1]+instance.rect6.size[1]*0.21)
        instance.line6.points = [instance.rect6.pos[0]+instance.rect6.size[0]*0.2, instance.rect6.pos[1]+instance.rect6.size[1]*0.13,
                                 instance.rect6.pos[0]+instance.rect6.size[0]*0.73, instance.rect6.pos[1]+instance.rect6.size[1]*0.65]
        instance.line7.points = [instance.rect6.pos[0]+instance.rect6.size[0]*0.18, instance.rect6.pos[1]+instance.rect6.size[1]*0.65,
                                 instance.rect6.pos[0]+instance.rect6.size[0]*0.73, instance.rect6.pos[1]+instance.rect6.size[1]*0.18]
        


class main(App):
    def build(self):
        return lyt()

if __name__ == '__main__':
    main().run()
