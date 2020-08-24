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
import time
import threading
#from kivymd.toast import toast
from my_toast import toast
from kivymd.app import MDApp
#from kivy.core.window import Window
#Window.size = (300, 100)
###########################################################################################
###   0 for ZERO    and   S
corner_points={};
data={'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2}
#possibilities = {'1':[1,2,3], '2':[1,4,7], '3':[1,5,9], '4':[2,5,8], '5':[3,6,9], '6':[3,5,7], '7':[4,5,6], '8':[7,8,9]}
possibilities = {'1':[[1,2,3],'h'], '2':[[1,4,7],'v'], '3':[[1,5,9],'s1'], '4':[[2,5,8], 'v'], '5':[[3,6,9],'v'], '6':[[3,5,7],'s2'],
                 '7':[[4,5,6],'h'], '8':[[7,8,9],'h']}
btn_self={};reset=0;btn_count=0;
#######################################################################################
class make_circle(FloatLayout):
    def __init__(self,btn, **kwargs):
        super(make_circle, self).__init__(**kwargs)
        global corner_points
        corner_points[str(btn.text)] = [btn.center_x - btn.size[0]/3, btn.center_y + btn.size[1]/3]
        with btn.canvas.after:
            Color(1., 0, 0, 0.7)
            btn.line = Line(circle=(btn.center_x, btn.center_y, btn.size[1]/3), width=3)
            
        btn.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, instance, value):
        instance.line.circle = (instance.center_x, instance.center_y, instance.size[1]/3)
#        instance.line.width = instance.width
            
class make_cross(FloatLayout):
    def __init__(self,btn, *args, **kwargs):
        super(make_cross, self).__init__(**kwargs)
        global corner_points
        corner_points[str(btn.text)] = [btn.center_x - btn.size[0]/3, btn.center_y + btn.size[1]/3]
        with btn.canvas.after:
            Color(0., 0, 1, 0.7)
            btn.line1 = Line(points=[btn.center_x - btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x + btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=3)
            btn.line2 = Line(points=[btn.center_x + btn.size[0]/3, btn.center_y + btn.size[1]/3, btn.center_x - btn.size[0]/3, 
                                    btn.center_y - btn.size[1]/3], width=3)
    
        btn.bind(pos=self.update_rect, size=self.update_rect)      
       
    
    def update_rect(self, instance, value):
        instance.line1.points = [instance.center_x - instance.size[0]/3, instance.center_y + instance.size[1]/3, instance.center_x + instance.size[0]/3, 
                                    instance.center_y - instance.size[1]/3]
        instance.line2.points = [instance.center_x + instance.size[0]/3, instance.center_y + instance.size[1]/3, instance.center_x - instance.size[0]/3, 
                                    instance.center_y - instance.size[1]/3]
#        instance.line.size = instance.size

def result_logic(btn, data, f1):
    global possibilities
    all_zero=[];all_one=[];re={};
#    print(data)
    for i in range(1,len(data)+1):
        if (data[str(i)] == 0):
            all_zero.append(i)
        elif (data[str(i)] == 1):
            all_one.append(i)
    if (len(all_one) > 2 or len(all_zero) > 2):
        for j in range(1,9):
                if (all(x in all_one for x in possibilities[str(j)][0]) == True):
                    re['1'] = possibilities[str(j)]
                    with f1.canvas.after:
                        Color(255/255,147/255,4/255,1)
                        btn_1 = list(re.values())[0][0]
                        btn_1 = btn_self[str(btn_1[0])]
                        btn_2 = list(re.values())[0][0]
                        btn_2 = btn_self[str(btn_2[2])]
                        #############################################################################
                        line_type = list(re.values())[0][1]
                        if (line_type == 'v'):
                            point = [btn_1.center_x , btn_1.center_y + btn_1.size[1]/2, 
                                     btn_2.center_x , btn_2.center_y - btn_1.size[1]/2]
                        elif (line_type == 'h'):
                            point = [btn_1.center_x - btn_1.size[0]/2 , btn_1.center_y, 
                                     btn_2.center_x + btn_1.size[1]/2 , btn_2.center_y]
                        elif (line_type == 's1'):
                            point = [btn_1.center_x - btn_1.size[0]/3, btn_1.center_y + btn_1.size[1]/3,
                                     btn_2.center_x + btn_2.size[0]/3, btn_2.center_y - btn_2.size[1]/3]
                        elif (line_type == 's2'):
                            point = [btn_1.center_x + btn_1.size[0]/3, btn_1.center_y + btn_1.size[1]/3,
                                     btn_2.center_x - btn_2.size[0]/3, btn_2.center_y - btn_2.size[1]/3]
                        ############################################################################
                        f1.line1 = Line(points=point, width=10)
                        f1.canvas.ask_update()
                        #################################################################################
                        toast(text='Player won this round', duration=1.5, icon='emoticon-lol')
                        #######################################################################################
                    return re
                elif (all(x in all_zero for x in possibilities[str(j)][0]) == True):
                    re['0'] = possibilities[str(j)]
                    with f1.canvas.after:
                        Color(255/255,147/255,4/255,1)
                        btn_1 = list(re.values())[0][0]
                        btn_1 = btn_self[str(btn_1[0])]
                        btn_2 = list(re.values())[0][0]
                        btn_2 = btn_self[str(btn_2[2])]
                        #############################################################################
                        line_type = list(re.values())[0][1]
                        if (line_type == 'v'):
                            point = [btn_1.center_x , btn_1.center_y + btn_1.size[1]/2, 
                                     btn_2.center_x , btn_2.center_y - btn_1.size[1]/2]
                        elif (line_type == 'h'):
                            point = [btn_1.center_x - btn_1.size[0]/2 , btn_1.center_y, 
                                     btn_2.center_x + btn_1.size[1]/2 , btn_2.center_y]
                        elif (line_type == 's1'):
                            point = [btn_1.center_x - btn_1.size[0]/3, btn_1.center_y + btn_1.size[1]/3,
                                     btn_2.center_x + btn_2.size[0]/3, btn_2.center_y - btn_2.size[1]/3]
                        elif (line_type == 's2'):
                            point = [btn_1.center_x + btn_1.size[0]/3, btn_1.center_y + btn_1.size[1]/3,
                                     btn_2.center_x - btn_2.size[0]/3, btn_2.center_y - btn_2.size[1]/3]
                        ############################################################################
                        f1.line1 = Line(points=point, width=10)
                        #################################################################################
                        toast(text='Computer won this round', duration=1.5, icon='emoticon-sad')
                        #######################################################################################
                    return re
    return 0
def dis_btn(btn_self, f1):
    for i in range(1, len(btn_self)+1):
        btn_self[str(i)].canvas.after.children.clear()
        f1.canvas.after.children.clear()
        btn_self[str(i)].disabled = True
#        btn_self[str(i)].canvas.after.children.clear()

def go_to_reset(btn_self, f1):
    global reset
    time.sleep(1)
    for i in range(1, len(btn_self)+1):
        btn_self[str(i)].canvas.after.children.clear()
        f1.canvas.after.children.clear()
        btn_self[str(i)].disabled = False

def button_click(f2, f3, f1, btn):
    global corner_points, data, btn_self, reset, btn_count
    btn.disabled = True
    btn_count += 1
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
    #############################################################################
    data[str(btn.text)] = draw
    if (btn_count > 4 and btn_count < 9):
        re = result_logic(btn, data, f1)
        print(re)
        if (re != 0):
            #############################################################################################
            t1 = threading.Thread(target=go_to_reset, args=(btn_self, f1, ))
            t1.start()
            data={'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2}
            btn_count=0
            
    elif (btn_count == 9):
        #############################################################################################
        t1 = threading.Thread(target=go_to_reset, args=(btn_self, f1, ))
        t1.start()
        data={'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2}
        btn_count=0
        toast(text='This round is a draw', duration=1.5, icon='emoticon-happy')
        #######################################################################################
            
            
#        if (re != 0):
#            print(re.values())
#            with btn.canvas.after:
#                Color(255/255,147/255,4/255,1)
##                point_list = list(corner_points)
#                btn_1 = list(re.values())[0][0]
#                btn_1 = btn_self[str(btn_1)]
#                btn_2 = list(re.values())[0][2]
#                btn_2 = btn_self[str(btn_2)]
#                point = [btn_1.center_x, btn_1.center_y, btn_2.center_x, btn_2.center_y]
#                btn.line1 = Line(points=point, width=10)
    ##################################################################################
#    print(dir(btn))
#    ((btn.canvas.after.children.clear()))    ##3 TO clear the line

    ###############################################################################
#    if (len(corner_points) == 2):
#        with btn.canvas.after:
#            Color(0,0,1,1)
#            point_list = list(corner_points) 
#            point = corner_points[point_list[0]] + corner_points[point_list[1]]
#            btn.line1 = Line(points=point, width=3)
    ##############################################################################
#    dis_btn(btn_self)
class lyt(FloatLayout):
    def __init__(self, **kwargs):
        super(lyt, self).__init__(**kwargs)
        global btn_self
        with self.canvas.before:
#            Color(255/255,147/255,4/255,1) # green; colors range from 0-1 instead of 0-255
            Color(0.8,0.8,0.8,1)
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
            Color(1,1,1,0) # green; colors range from 0-1 instead of 0-255
            self.f1.rect1 = RoundedRectangle(size=self.f1.size,
                               pos=self.f1.pos)
        
        self.f1.bind(pos=self.update_rect1, size=self.update_rect1)
        ############################################################################################
        with self.f1.canvas.before:
            Color(51/255, 25/255, 0, 1)
            self.f1.line1 = Line(points=[], width=5)
            self.f1.line2 = Line(points=[], width=5)
            self.f1.line3 = Line(points=[], width=5)
            self.f1.line4 = Line(points=[], width=5)
        
        self.f1.bind(pos=self.update_rect2, size=self.update_rect2)
#        self.f1.bind(pos=self.update_rect2, size=partial(self.update_rect2, 'ljvn'))
#       ###########################################################################################
        self.b1 = Button(text=str(1),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.05, 'y': 0.71}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b1)
        
        self.b2 = Button(text=str(2),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.36, 'y': 0.71}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b2)
        
        self.b3 = Button(text=str(3),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.67, 'y': 0.71}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b3)
##        #########################################################################################
        self.b4 = Button(text=str(4),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.05, 'y': 0.556}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b4)
        
        self.b5 = Button(text=str(5),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.36, 'y': 0.556}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b5)
        
        self.b6 = Button(text=str(6),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.67, 'y': 0.556}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b6)
#        ###########################################################################################
        self.b7 = Button(text=str(7),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.05, 'y': 0.4}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b7)
        
        self.b8 = Button(text=str(8),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.36, 'y': 0.4}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b8)
        
        self.b9 = Button(text=str(9),size_hint=(0.28, 0.14),
                pos_hint={'x': 0.67, 'y': 0.4}, background_color =(1,1,1,0), color=[0,0,0,1])
        self.f1.add_widget(self.b9)
##########################################################################################################################
        self.f2 = FloatLayout()
        self.add_widget(self.f2)

        with self.f2.canvas.before:
            Color(1,1,1,0.5) # green; colors range from 0-1 instead of 0-255
            self.f2.rect5 = RoundedRectangle(size=self.f2.size,
                               pos=self.f2.pos)
            self.f2.l1 =  Label(text="Computer", font_size=60, color=(0, 0, 0, 1))
            Color(1,0,0,0.5)
            self.f2.line5 = Line(circle=(self.f2.size[0]+25, self.f2.size[1]-20, self.f2.size[1]/3), width=5)
        
        self.f2.bind(pos=self.update_rect5, size=self.update_rect5)
        
        ###############################################################################################
        self.f3 = FloatLayout()
        self.add_widget(self.f3)

        with self.f3.canvas.before:
            Color(0,1,0,.5) # green; colors range from 0-1 instead of 0-255
            self.f3.rect6 = RoundedRectangle(size=self.f3.size,
                               pos=self.f3.pos)
            self.f3.l2 =  Label(text="Player", font_size=60, color=(0, 0, 0, 1))
            Color(1,0,0,0.5)
            self.f3.line6 = Line(points=[self.f3.center_x - self.f3.size[0]/4, self.f3.center_y + self.f3.size[1]/4, 
                                         self.f3.center_x + self.f3.size[0]/4, self.f3.center_y - self.f3.size[1]/4], width=5)
            self.f3.line7 = Line(points=[self.f3.center_x + self.f3.size[0]/4, self.f3.center_y + self.f3.size[1]/4, 
                                         self.f3.center_x - self.f3.size[0]/4, self.f3.center_y - self.f3.size[1]/4], width=5)
        
        self.f3.bind(pos=self.update_rect6, size=self.update_rect6)
        #############################################################################################
        self.b1.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b2.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b3.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b4.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b5.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b6.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b7.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b8.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        self.b9.bind(on_press = partial(button_click, self.f2, self.f3, self.f1))
        btn_self[str(self.b1.text)] = self.b1
        btn_self[str(self.b2.text)] = self.b2
        btn_self[str(self.b3.text)] = self.b3
        btn_self[str(self.b4.text)] = self.b4
        btn_self[str(self.b5.text)] = self.b5
        btn_self[str(self.b6.text)] = self.b6
        btn_self[str(self.b7.text)] = self.b7
        btn_self[str(self.b8.text)] = self.b8
        btn_self[str(self.b9.text)] = self.b9
       
    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
    
    def update_rect1(self, instance, value):
        instance.rect1.pos = (instance.size[0]*0.05 ,instance.size[1]*0.4 )
        instance.rect1.size = (instance.size[0]*0.9 ,instance.size[1]*0.45)
    
    def update_rect2(self, instance, value):
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
        instance.l1.pos = (self.pos[0]+instance.rect5.pos[0]+instance.rect5.size[0]/2.7, self.pos[1]+instance.rect5.pos[1]+instance.rect5.size[1]*0.7)
        instance.line5.circle = (self.pos[0]+self.size[0]*0.25, self.pos[1]+self.size[1]*0.155, instance.rect5.size[0]/3.5)
        
    def update_rect6(self, instance, value):
        instance.rect6.pos = (self.pos[0]+self.size[0]*0.6,self.pos[1]+self.size[1]*0.1)
        instance.rect6.size = (self.size[0]*0.3, self.size[1]/2*0.3)
#        instance.l2.pos = (self.pos[0]+self.size[0]*0.55, self.pos[1]+self.size[1]*0.125)
#        instance.l2.pos = (instance.rect6.pos[0]-instance.rect6.size[0]*0.15, instance.rect6.pos[1]+instance.rect6.size[1]*0.21)
        instance.l2.pos = (self.pos[0]+instance.rect6.pos[0]+instance.rect6.size[0]/2.7, self.pos[1]+instance.rect6.pos[1]+instance.rect6.size[1]*0.7)
        
        instance.line6.points = [instance.rect6.pos[0]+instance.rect6.size[0]*0.2, instance.rect6.pos[1]+instance.rect6.size[1]*0.13,
                                 instance.rect6.pos[0]+instance.rect6.size[0]*0.73, instance.rect6.pos[1]+instance.rect6.size[1]*0.65]
        instance.line7.points = [instance.rect6.pos[0]+instance.rect6.size[0]*0.18, instance.rect6.pos[1]+instance.rect6.size[1]*0.65,
                                 instance.rect6.pos[0]+instance.rect6.size[0]*0.73, instance.rect6.pos[1]+instance.rect6.size[1]*0.18]
        


class main(MDApp):
    def build(self):
        return lyt()

if __name__ == '__main__':
    main().run()
