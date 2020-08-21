import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle,Line,RoundedRectangle
from functools import partial
from kivy.uix.label import Label
##########################################################################################
class make_circle(FloatLayout):
    def __init__(self,btn,val, **kwargs):
        super(make_circle, self).__init__(**kwargs)
        print((btn.size))
        with btn.canvas.after:
            btn.line = Line(circle=(btn.center_x, btn.center_y, btn.size[1]/3), width=2)
            
class make_cross(FloatLayout):
    def __init__(self,btn,val, **kwargs):
        super(make_cross, self).__init__(**kwargs)
        print((btn.size))
        with btn.canvas.after:
            Color(1., 0, 0, 1)
            btn.line = Line(points=[btn.center_x - btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x + btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=5)
            btn.line = Line(points=[btn.center_x + btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x - btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=5)

class make_circle2(FloatLayout):
    def __init__(self,btn, main_self, **kwargs):
        super(make_circle2, self).__init__(**kwargs)
        print((main_self.size_hint))
        print((main_self.pos_hint))
        with btn.canvas.after:
            btn.line = Line(circle=(main_self.size[0], main_self.size[1], btn.size[1]/3), width=2)
            
class make_cross2(FloatLayout):
    def __init__(self,btn, main_self, **kwargs):
        super(make_cross2, self).__init__(**kwargs)
        print((btn.size))
        with btn.canvas.after:
            Color(1., 0, 0, 1)
            btn.line = Line(points=[btn.center_x - btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x + btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=5)
            btn.line = Line(points=[btn.center_x + btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x - btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=5)
    

class lyt(FloatLayout):
    def __init__(self, **kwargs):
        super(lyt, self).__init__(**kwargs)
        
        with self.canvas.before:
#            Color(1, 1, 0, 0.1) # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size,
                               pos=self.pos)
            self.rect.source = 'main_lyt.jpg'
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        self.f1 = FloatLayout(size_hint=(self.size_hint[0]*0.6,self.size_hint[1]*0.6), 
                         pos_hint={'center_x':self.center_x/100, 'center_y':self.center_y/83})
        self.add_widget(self.f1)
        
        with self.f1.canvas.before:
            Color(1,1,1,1) # green; colors range from 0-1 instead of 0-255
            self.f1.rect1 = RoundedRectangle(size=self.f1.size,
                               pos=self.f1.pos)
        
        self.f1.bind(pos=self.update_rect1, size=self.update_rect1)
        
#        with self.f1.canvas.after:
#            self.f1.line = Line(circle=(200, 200, 25), width=2)
        
#        print(b.pos_hint)
#       ###########################################################################################
#        self.b1 = Button(text=str(0),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0, 'y': 0.67}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b1)
##        
#        self.b2 = Button(text=str(1),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0.33333333, 'y': 0.67}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b2)
#        
#        self.b3 = Button(text=str(2),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0.6666666666666, 'y': 0.67}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b3)
##        #########################################################################################
#        self.b4 = Button(text=str(3),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0, 'y': 0.335}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b4)
#        
#        self.b5 = Button(text=str(4),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0.33333333, 'y': 0.335}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b5)
#        
#        self.b6 = Button(text=str(5),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0.6666666666666, 'y': 0.335}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b6)
##        ###########################################################################################
#        self.b7 = Button(text=str(6),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0, 'y': 0}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b7)
#        
#        self.b8 = Button(text=str(7),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0.33333333, 'y': 0}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b8)
#        
#        self.b9 = Button(text=str(8),size_hint=(0.33333333333, 0.333333333333),
#                pos_hint={'x': 0.6666666666666, 'y': 0}, background_color =(1,1,1,1), color=[0,0,0,1])
#        self.f1.add_widget(self.b9)
###        #########################################################################################
#        self.b1.bind(on_press = partial(make_cross, self.b1))
#        self.b2.bind(on_press = partial(make_circle, self.b2))
#        self.b3.bind(on_press = partial(make_circle, self.b3))
#        self.b4.bind(on_press = partial(make_circle, self.b4))
#        self.b5.bind(on_press = partial(make_circle, self.b5))
#        self.b6.bind(on_press = partial(make_circle, self.b6))
#        self.b7.bind(on_press = partial(make_circle, self.b7))
#        self.b8.bind(on_press = partial(make_circle, self.b8))
#        self.b9.bind(on_press = partial(make_cross, self.b9))
        #############################################################################################
        self.f2 = FloatLayout(size_hint=(self.size_hint[0]*0.2, self.size_hint[1]*0.2),
                              pos_hint={'x':self.x + self.size_hint[0]*0.05, 'y':self.y+ self.size_hint[1]*0.05})
        self.add_widget(self.f2)
        
        with self.f2.canvas.before:
            Color(1,1,1,0.5) # green; colors range from 0-1 instead of 0-255
            self.f2.rect1 = RoundedRectangle(size=self.f2.size,
                               pos=self.f2.pos)
        
        self.f2.bind(pos=self.update_rect1, size=self.update_rect1)
        
        self.l1 = Label(text='Computer')
        self.l1.pos_hint={'x':self.f2.x, 'y':self.f2.y+0.3}
        self.f2.add_widget(self.l1)
        
        make_circle2(self.f2, self)
        ###############################################################################################
        #############################################################################################
        self.f3 = FloatLayout(size_hint=(self.size_hint[0]*0.2, self.size_hint[1]*0.2),
                              pos_hint={'x':self.x + self.size_hint[0]*0.75, 'y':self.y+ self.size_hint[1]*0.05})
        self.add_widget(self.f3)
        
        with self.f3.canvas.before:
            Color(0,0,1,1) # green; colors range from 0-1 instead of 0-255
            self.f3.rect1 = RoundedRectangle(size=self.f3.size,
                               pos=self.f3.pos)
        
        self.f3.bind(pos=self.update_rect1, size=self.update_rect1)
        
        self.l2 = Label(text='Player')
        self.l2.pos_hint={'x':self.f3.x, 'y':self.f3.y+0.3}
        self.f3.add_widget(self.l2)
        ###############################################################################################
    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
    
    def update_rect1(self, instance, value):
        instance.rect1.pos = instance.pos
        instance.rect1.size = instance.size#  
          

class main(App):
    def build(self):
        return lyt()

if __name__ == '__main__':
    main().run()
