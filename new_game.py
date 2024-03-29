# -*- coding: utf-8 -*-
from kivy.uix.widget import Widget
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer, NavigationDrawerToolbar,\
        NavigationDrawerIconButton, NavigationDrawerDivider, NavigationDrawerSubheader
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle,Line,RoundedRectangle
from kivymd.theming import ThemeManager
Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '500')
from functools import partial
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
#from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.uix.selectioncontrol import MDCheckbox
import threading
from my_toast import toast
#from kivymd.toast.kivytoast.kivytoast import Toast
import time
import random
from kivy.metrics import dp, sp
from kivy.config import Config
from kivy.lang import Builder
from kivymd.uix.button import MDFillRoundFlatIconButton
###########################################################################################
###   0 for ZERO    and   S
corner_points={};
data={'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2}
#possibilities = {'1':[1,2,3], '2':[1,4,7], '3':[1,5,9], '4':[2,5,8], '5':[3,6,9], '6':[3,5,7], '7':[4,5,6], '8':[7,8,9]}
possibilities = {'1':[[1,2,3],'h'], '2':[[1,4,7],'v'], '3':[[1,5,9],'s1'], '4':[[2,5,8], 'v'], '5':[[3,6,9],'v'], '6':[[3,5,7],'s2'],
                 '7':[[4,5,6],'h'], '8':[[7,8,9],'h']}
btn_self={};reset=0;btn_count=0;o_count=0;x_count=0;draw_count=0;

remaining_btn=[1,2,3,4,5,6,7,8,9];all_zero=[];all_one=[];player=1;com=0;li=[];all_one_com=[]
##################################################################################################
def clear_data(l7, l8, l9, event):
    global o_count, x_count, draw_count
    App.get_running_app().config.set('result','o_win',int(0))
    App.get_running_app().config.write()
    App.get_running_app().config.set('result','x_win',int(0))
    App.get_running_app().config.write()
    App.get_running_app().config.set('result','draw',int(0))
    App.get_running_app().config.write()
    
    l7.text = str(0)
    l8.text = str(0)
    l9.text = str(0)
    
    o_count=0
    x_count=0
    draw_count=0

def navigator_lyt(self,main_box_self, l7, l8, l9):
#    tool_box = FloatLayout(
#                          size_hint=[1,0.9],
#                          pos=(main_box_self.width, main_box_self.height*0.9))
    tb = MDToolbar(title='',background_palette= 'Primary')
    tb.md_bg_color = [0,0,0,0] 
    tb.elevation = 0
    tb.left_action_items= [['menu', lambda x : self.toggle_nav_drawer()]]
#    tb.left_action_items= [['menu', lambda x : main_box_self.toggle_nav_drawer()]]
    tb.pos_hint = {'x':0, 'y':0.9}
#        self.tb.size = [self.main_box.width, self.main_box.height*0.1]
#    tool_box.add_widget(tb)
    #########################################################################
    self.nav_drawer = MDNavigationDrawer(spacing=dp(0))
    self.nav_drawer.canvas.children[1].rgba = [1,1,1,0.8]
    self.nav_drawer.canvas.children[3].source = 'images/menu_image.jpg'
#        self.nav_drawer.ids['drawer_title'].text = 'Nagendra'
    self.nav_drawer.ids['drawer_logo'].source = 'images/menu_image.jpg'
    self.nav_drawer.ids['drawer_logo'].color = [1,1,1,0]
##############################################################################
    with self.nav_drawer.ids['drawer_logo'].canvas.after:
        Color(1,1,1,.8)
        self.nav_drawer.ids['drawer_logo'].rect1 = RoundedRectangle(segments=15, radius=[9000])
        self.nav_drawer.ids['drawer_logo'].rect1.source = 'images/my_photo.jpg' # my_photo
        
    def update_rect1(instance, value):
        instance.rect1.pos=[instance.pos[0]+68,instance.pos[1]+30]
        instance.rect1.size = [instance.size[1]*0.8, instance.size[1]*0.8]
#        instance.rect1.pos=[instance.pos[0]+(instance.size[0]-instance.size[1])/2+5,instance.pos[1]+dp(30)]
#        instance.rect1.size = [instance.size[0]*0.6, instance.size[1]*0.75]
#            instance.rect1.radius = [instance.rect1.size[0]-(instance.rect1.size[0])/2]
    self.nav_drawer.ids['drawer_logo'].bind(pos=update_rect1, size=update_rect1)
    
#        ##########################################################
#        nav_sub = NavigationDrawerSubheader(text='sepera')
#        self.nav_drawer.add_widget(nav_sub)
    self.nav_draw_icon1 = NavigationDrawerIconButton(icon='delete',text='Delete data',
                                                     icon_color=[0,0,0,0.5],use_active=True)
#        self.nav_draw_icon1.text_color = [1,0,0,0.1]
    self.nav_draw_icon1.bind(on_press=partial(clear_data, l7, l8, l9))
    self.nav_drawer.add_widget(self.nav_draw_icon1)
    line_sep = NavigationDrawerDivider()
    self.nav_drawer.add_widget(line_sep)

    self.add_widget(self.nav_drawer)
        
#    main_box_self.add_widget(tool_box)
    main_box_self.add_widget(tb)
    
    return self.nav_draw_icon1
#####################################################################################################

    
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
    
def renable(f1,sleep_time):
    global btn_self, data, all_zero, all_one, remaining_btn
    time.sleep(sleep_time)
    for i in range(1, len(btn_self)+1):
        btn_self[str(i)].canvas.after.children.clear()
        f1.canvas.after.children.clear()
        btn_self[str(i)].disabled = False
    return

def go_to_reset(f1, sleep_time, *args):
    global btn_self, data, all_zero, all_one, remaining_btn, btn_count
    for i in range(1, len(btn_self)+1):
        btn_self[str(i)].disabled = True
    
    t2 = threading.Thread(target=renable, args=(f1, sleep_time,))
    t2.start()
    for ii in f1.parent.children:
        if (ii.id == 'f2'):
            f2  = ii
        elif (ii.id == 'f3'):
            f3 = ii
    try:
        if (args[0] == 'check'):
            f2.canvas.before.children[0].rgba = [1,1,1,0.5]
            f3.canvas.before.children[0].rgba = [0,1,0,0.5]
    except:
        pass
    data={'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2}
    btn_count=0
    all_zero=[];all_one=[];
    remaining_btn=[1,2,3,4,5,6,7,8,9]
    return
    

def winner_check(f1, f2, f3, all_zero, all_one):
    global possibilities, x_count, o_count,data
    re={};
    for j in range(1,9):
        if (all(x in all_one for x in possibilities[str(j)][0]) == True or all(x in all_zero for x in possibilities[str(j)][0]) == True):
            li = data[str(possibilities[str(j)][0][0])]
            if (li == 1):
                re['1'] = possibilities[str(j)]
            elif (li == 0):
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
                if (li == 1):
                    f1.line1 = Line(points=point, width=20)
                    f1.canvas.ask_update()
                    #################################################################################
                    toast(text='Player won this round', duration=2.5, icon='emoticon-lol')
                    f3.canvas.before.children[0].rgba = [0,1,0,0.5]
                    f2.canvas.before.children[0].rgba = [1,1,1,0.5]
                    #######################################################################################
                    x_count += 1
                elif (li == 0):
                    ############################################################################
                    f1.line1 = Line(points=point, width=20)
                    #################################################################################
                    toast(text='Computer won this round', duration=2.5, icon='emoticon-sad')
                    f2.canvas.before.children[0].rgba = [0,1,0,0.5]
                    f3.canvas.before.children[0].rgba = [1,1,1,0.5]
                    #######################################################################################
                    o_count += 1
            return re
def iswinner(curr):
    global li
    for i in remaining_btn:
        li.append(i)
        for j in range(1,9):
            if (all(x in li for x in possibilities[str(j)][0]) == True):
                return i
            else:
                pass
        li = list(curr)

def chooseRandomMoveFromList(remaining_btn, movesList):
        possibelmove=[];
        
        for i in movesList:
            if (i in remaining_btn):
                possibelmove.append(i)
        
        if len(possibelmove) != 0:
            return random.choice(possibelmove)
        else:
            return None

def comturn(remaining_btn):
    global btn_self, all_zero,li, all_one
    ################################################################
    # First, check if we can win in the next move
    li = list(all_zero)
    win = iswinner(all_zero)
    if (win != None):
        return win
    ########################################################################
    # Check if the player could win on his next move, and block them.
    li = list(all_one)
    win = iswinner(all_one)
    if (win != None):
        return win
    ##########################################################################
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(remaining_btn, [1,3,7,9])
    if move != None:
        return move
    ################################################################
    # Try to take the center, if it is free.
    move = chooseRandomMoveFromList(remaining_btn, [5])
    if move != None:
        return move
    ###########################################################
    # Move on one of the sides.
    return chooseRandomMoveFromList(remaining_btn, [2, 4, 6, 8])
    ########################################################################

def start_again():
    global remaining_btn, btn_self
    time.sleep(2.5)
    btn_no = comturn(remaining_btn)
    btn_self[str(btn_no)].trigger_action(duration=0)

def button_click(f2, f3, f1, f4, btn):
    global corner_points, data, btn_self, reset, btn_count, o_count, x_count, draw_count, possibilities
    global all_zero, all_one, remaining_btn
    btn.disabled = True
    ###########################################################################
    for kk in f1.parent.children:
        if kk.id == 'ch1':
            ch1 = kk.active
        elif (kk.id == 'ch2'):
            ch2 = kk.active
    ##################################################################################
    for m in (f4.children):
        if (m.id == 'l7'):
            L7 = m
        elif (m.id == 'l8'):
            L8 = m
        elif (m.id == 'l9'):
            L9 = m
    ############################################################################
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
    remaining_btn.remove(int(btn.text))
    if (draw == 0):
        all_zero.append(int(btn.text))
    else:
        all_one.append(int(btn.text))
#    if (btn_count > 4 and btn_count < 10):
    re = winner_check(f1, f2, f3, all_zero, all_one)#result_logic(btn, data, f1, f2, f3)
    if (re != 0 and re != None):
        #############################################################################################
#            who_win = list(re.keys())[0]
        t1 = threading.Thread(target=go_to_reset, args=(f1, 2.5))
        t1.start()
        t1.join()
        L7.text = str(o_count)
        L8.text = str(x_count)
        L9.text = str(draw_count)
        ###########################################################
        App.get_running_app().config.set('result','o_win',int(o_count))
        App.get_running_app().config.write()
        App.get_running_app().config.set('result','x_win',int(x_count))
        App.get_running_app().config.write()
        App.get_running_app().config.set('result','draw',int(draw_count))
        App.get_running_app().config.write()
        ###############################################
        if (ch1 == True):
            if (list(re.keys())[0] == '0'):
                t3 = threading.Thread(target=start_again)
                t3.start()
        return
    elif (btn_count == 9):
        #############################################################################################
#            who_win = ''
        t1 = threading.Thread(target=go_to_reset, args=(f1, 2.5))
        t1.start()
        toast(text='This round is a draw', duration=1.5, icon='emoticon-happy')
        draw_count += 1
        L7.text = str(o_count)
        L8.text = str(x_count)
        L9.text = str(draw_count)
        ###########################################################
        App.get_running_app().config.set('result','o_win',int(o_count))
        App.get_running_app().config.write()
        App.get_running_app().config.set('result','x_win',int(x_count))
        App.get_running_app().config.write()
        App.get_running_app().config.set('result','draw',int(draw_count))
        App.get_running_app().config.write()
        ###############################################
        if (f2.canvas.before.children[0].rgba == [0,1,0,0.5] and ch1 == True):
            t3 = threading.Thread(target=start_again)
            t3.start()
        return
    #######################################################################################
    if (ch1 == True):
        if (draw == 1):
            btn_no = comturn(remaining_btn)
            btn_self[str(btn_no)].trigger_action(duration=0)
    ######################################################################################

def check_btn(f1,self, *args):
    pr = self.id
    for jj in self.parent.children:
        if (jj.id == 'ch1'):
            ch1 = jj
        elif (jj.id == 'ch2'):
            ch2 = jj
    if (pr == 'ch1'):
        ch2.active = False
        ch1.active = True
    elif (pr == 'ch2'):
        ch2.active = True
        ch1.active = False
        
    go_to_reset(f1, 0, 'check')
    return

class lyt(FloatLayout):
    def __init__(self, config, **kwargs):
        super(lyt, self).__init__(**kwargs)
        global draw_count,x_count,o_count;
        ################################################################
        main_size = Window.size
#        f0 = FloatLayout(size=main_size)
#        self.add_widget(f0)
        self.size = main_size
        with self.canvas.before:
            Color(0.8,0.8,0.8,1)
            self.rect1 = RoundedRectangle(size = main_size, pos = self.pos)
            self.rect1.source = 'main_lyt.jpg'
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        ########################################################################
        self.f1 = FloatLayout(id='f1',size_hint = (0.9, 0.5), 
                              pos_hint={'x':0.05, 'y':0.4})
        self.add_widget(self.f1)
        with self.f1.canvas.before:
            Color(1,1,1,0)
#            self.f1.rect1 = RoundedRectangle(id='rect1',size=(self.f1.size[0], self.f1.size[1]), pos = self.f1.pos)
            self.f1.rect1 = RoundedRectangle(id='rect1',size_hint=self.f1.size_hint, pos_hint = self.f1.pos_hint)
            Color(51/255, 25/255, 0, 1)
            self.f1.line1 = Line(points=[], width=5)
            self.f1.line2 = Line(points=[], width=5)
            self.f1.line3 = Line(points=[], width=5)
            self.f1.line4 = Line(points=[], width=5)
            
        self.f1.bind(pos=self.update_rect1 ,size= self.update_rect1)
#        
#        ###########################################################################################
        self.b1 = Button(text=str(1),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.01, 'y': 0.69}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b1)
        
        self.b2 = Button(text=str(2),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.35, 'y': 0.69}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b2)
        
        self.b3 = Button(text=str(3),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.69, 'y': 0.69}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b3)
##        #########################################################################################
        self.b4 = Button(text=str(4),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.01, 'y': 0.35}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b4)
        
        self.b5 = Button(text=str(5),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.35, 'y': 0.35}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b5)
        
        self.b6 = Button(text=str(6),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.69, 'y': 0.35}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b6)
##        ###########################################################################################
        self.b7 = Button(text=str(7),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.01, 'y': 0.01}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b7)
        
        self.b8 = Button(text=str(8),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.35, 'y': 0.01}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b8)
        
        self.b9 = Button(text=str(9),size_hint=(0.3, 0.3),
                pos_hint={'x': 0.69, 'y': 0.01}, background_color =(1,1,1,0), color=[0,0,0,0], disabled_color=[0,0,0,0])
        self.f1.add_widget(self.b9)
###########################################################################################################################
        self.f2 = FloatLayout(id='f2',pos_hint={'x':0.05, 'y':0.07}, 
                              size_hint=(0.3,  0.15))
        self.add_widget(self.f2)
        self.f2.l2 =  Label(id='l2',text="Computer", font_size=15, color=(51/255, 25/255, 0, 1),
                            pos_hint = {'center_x':0.5, 'center_y':0.85})
        self.f2.add_widget(self.f2.l2)
        with self.f2.canvas.before:
            Color(1,1,1,0.5) # green; colors range from 0-1 instead of 0-255
            self.f2.rect2 = RoundedRectangle(size_hint=self.f2.size_hint,
                               pos_hint=self.f2.pos_hint, _radius=5)
            Color(1,0,0,1)
            self.f2.line2 = Line(circle=(self.f2.size[0]+25, self.f2.size[1]-20, self.f2.size[1]/3), width=5)
        
        self.f2.bind(pos=self.update_rect2, size=self.update_rect2)
#        
        ###############################################################################################
        self.f3 = FloatLayout(id='f3',pos_hint={'x':0.65, 'y':0.07}, 
                              size_hint=(0.3,  0.15))
        self.add_widget(self.f3)
        self.f3.l3 =  Label(id='l3',text="Player", font_size=15, color=(51/255, 25/255, 0, 1), 
                            pos_hint = {'center_x':0.5, 'center_y':0.85})
        self.f3.add_widget(self.f3.l3)
        with self.f3.canvas.before:
            Color(0,1,0,0.5) # green; colors range from 0-1 instead of 0-255
            self.f3.rect3 = RoundedRectangle(size_hint=self.f3.size_hint,
                               pos_hint=self.f3.pos_hint, _radius=5)
            Color(0,0,1,1)
            self.f3.line6 = Line(points=[self.f3.center_x - self.f3.size[0]/4, self.f3.center_y + self.f3.size[1]/4, 
                                         self.f3.center_x + self.f3.size[0]/4, self.f3.center_y - self.f3.size[1]/4], width=5)
            self.f3.line7 = Line(points=[self.f3.center_x + self.f3.size[0]/4, self.f3.center_y + self.f3.size[1]/4, 
                                         self.f3.center_x - self.f3.size[0]/4, self.f3.center_y - self.f3.size[1]/4], width=5)
        
        self.f3.bind(pos=self.update_rect3, size=self.update_rect3)
#        
        
        ############################################################################################
        self.f4 = FloatLayout(pos_hint={'x':0.05, 'y':0.26}, 
                              size_hint=(0.9,  0.1))
        self.add_widget(self.f4)
        self.f4.l4 =  Label(id='l4',text="-wins", font_size=15, color=(51/255, 25/255, 0, 1),
                            pos_hint = {'center_x':0.19, 'center_y':0.4})
        self.f4.add_widget(self.f4.l4)
        
        self.f4.l5 =  Label(id='l5',text="-wins", font_size=15, color=(51/255, 25/255, 0, 1),
                            pos_hint = {'center_x':0.6, 'center_y':0.4})
        self.f4.add_widget(self.f4.l5)
        
        self.f4.l6 =  Label(id='l6',text="draw", font_size=15, color=(51/255, 25/255, 0, 1),
                            pos_hint = {'center_x':0.9, 'center_y':0.4})
        self.f4.add_widget(self.f4.l6)
        ###################################################################################################
        o_count = int(config.get('result','o_win'))
        x_count = int(config.get('result','x_win'))
        draw_count = int(config.get('result','draw'))
        ##################################################################################
        self.f4.l7 =  Label(id='l7',text=str(o_count), font_size=15, color=(51/255, 25/255, 0, 1),
                            pos_hint = {'center_x':0.1, 'center_y':0.85})
        self.f4.add_widget(self.f4.l7)
        
        self.f4.l8 =  Label(id='l8',text=str(x_count), font_size=15, color=(51/255, 25/255, 0, 1),
                            pos_hint = {'center_x':0.55, 'center_y':0.85})
        self.f4.add_widget(self.f4.l8)
        
        self.f4.l9 =  Label(id='l9',text=str(draw_count), font_size=15, color=(51/255, 25/255, 0, 1),
                            pos_hint = {'center_x':0.9, 'center_y':0.85})
        self.f4.add_widget(self.f4.l9)
        
        ##############################################################################################
        self.box1 = BoxLayout(orientation='horizontal',pos_hint={'x':0.05, 'y':0.01}, 
                              size_hint=(0.3,  0.05))
        self.bb = Button(text='clear')
        self.bb.bind(on_release=partial(clear_data, self.f4.l7, self.f4.l8, self.f4.l9))
        self.box1.add_widget(self.bb)
        self.add_widget(self.box1)
        ##############################################################################################
        with self.f4.canvas.before:
            Color(1,1,1,0) # green; colors range from 0-1 instead of 0-255
            self.f4.rect4 = RoundedRectangle(size_hint=self.f3.size_hint,
                               pos_hint=self.f3.pos_hint, _radius=5)
            Color(1,0,0,0.5)
            self.f4.line8 = Line(circle=(self.f4.size[0]+25, self.f4.size[1]-20, self.f4.size[1]/3), width=6)
            
            Color(0,0,1,0.5)
            self.f4.line9 = Line(points=[self.f4.center_x - self.f4.size[0]/4, self.f4.center_y + self.f4.size[1]/4, 
                                         self.f4.center_x + self.f4.size[0]/4, self.f4.center_y - self.f4.size[1]/4], width=6)
            self.f4.line10 = Line(points=[self.f4.center_x + self.f4.size[0]/4, self.f4.center_y + self.f4.size[1]/4, 
                                         self.f4.center_x - self.f4.size[0]/4, self.f4.center_y - self.f4.size[1]/4], width=6)

        self.f4.bind(pos=self.update_rect4, size=self.update_rect4)
    ###################################################################################################################
        self.b1.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b2.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b3.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b4.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b5.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b6.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b7.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b8.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        self.b9.bind(on_press = partial(button_click, self.f2, self.f3, self.f1, self.f4))
        btn_self[str(self.b1.text)] = self.b1
        btn_self[str(self.b2.text)] = self.b2
        btn_self[str(self.b3.text)] = self.b3
        btn_self[str(self.b4.text)] = self.b4
        btn_self[str(self.b5.text)] = self.b5
        btn_self[str(self.b6.text)] = self.b6
        btn_self[str(self.b7.text)] = self.b7
        btn_self[str(self.b8.text)] = self.b8
        btn_self[str(self.b9.text)] = self.b9    
    #######################################################################################################
        self.checkbox3 = MDCheckbox(active = True,pos_hint =  {'center_x':0.1, 'center_y':0.96},
                                    size_hint=(0.08,0.05))
        self.add_widget(self.checkbox3)
        self.checkbox3.checkbox_icon_down = 'checkbox-blank-outline'
        self.checkbox3.check_anim_in.animated_properties['font_size'] = sp(15)
        self.checkbox3.unselected_color = (102/255,51/255,0,.8)
        self.checkbox3.selected_color = (102/255,51/255,0,.8)
        self.checkbox3.disabled = True
        self.checkbox3.disabled_color = (102/255,51/255,0,.8)
        
        self.checkbox1 = MDCheckbox(id='ch1',active = True,pos_hint =  {'center_x':0.1, 'center_y':0.96},
                                    size_hint=(0.08,0.05))
        self.add_widget(self.checkbox1)
        self.checkbox1.checkbox_icon_down = 'check'
        self.checkbox1.unselected_color = (1,1,1,0)
        self.checkbox1.selected_color = (1,0,0,1)
        self.checkbox1.bind(on_press = partial(check_btn, self.f1))
        self.checkbox1.check_anim_in.animated_properties['font_size'] = sp(30)
        
        self.lbl1 = Label(text='Computer',pos_hint =  {'center_x':0.23, 'center_y':0.96},
                          color=(51/255, 25/255, 0, 1),bold=True)
        self.add_widget(self.lbl1)
        
        self.checkbox5 = MDCheckbox(active = True,pos_hint =  {'center_x':0.7, 'center_y':0.96},
                                    size_hint=(0.08,0.05))
        self.add_widget(self.checkbox5)
        self.checkbox5.checkbox_icon_down = 'checkbox-blank-outline'
        self.checkbox5.check_anim_in.animated_properties['font_size'] = sp(15)
        self.checkbox5.unselected_color = (102/255,51/255,0,.8)
        self.checkbox5.selected_color = (102/255,51/255,0,.8)
        self.checkbox5.disabled = True
        self.checkbox5.disabled_color = (102/255,51/255,0,.8)
        
        self.checkbox2 = MDCheckbox(id='ch2',active = False,pos_hint =  {'center_x':0.7, 'center_y':0.96},
                                    size_hint=(0.08,0.05))
        self.add_widget(self.checkbox2)
        self.checkbox2.checkbox_icon_down = 'check'
        self.checkbox2.unselected_color = (1,1,1,0)
        self.checkbox2.selected_color = (1,0,0,1)
        self.checkbox2.bind(on_press = partial(check_btn, self.f1))
        self.checkbox2.check_anim_in.animated_properties['font_size'] = sp(30)
        
        self.lbl2 = Label(text='Friend',pos_hint =  {'center_x':0.8, 'center_y':0.96},
                          color=(51/255, 25/255, 0, 1),bold=True)
        self.add_widget(self.lbl2)
        
        self.checkbox2.ripple_scale = 0    ## To disable the button ripple effect
        self.checkbox1.ripple_scale = 0
        
        
        b1 = NavigationLayout()
        self.add_widget(b1)
        navigator_lyt(b1, self, self.f4.l7, self.f4.l8, self.f4.l9)
        
    #########################################################################################################
    def update_rect(self, instance, value):
        instance.rect1.pos = instance.pos
        instance.rect1.size = instance.size
        
    def update_rect1(self, instance, value):
        instance.rect1.pos = instance.pos#(instance.size[0]*0.05 ,instance.size[1]*0.4 )
        instance.rect1.size = instance.size#(instance.size[0]*0.9 ,instance.size[1]*0.45)
        instance.line1.points = [instance.rect1.pos[0]+instance.rect1.size[0]/3, instance.rect1.pos[1]+instance.rect1.size[1]/1,
                                 instance.rect1.pos[0]+instance.rect1.size[0]/3, instance.rect1.pos[1]] 
    
        instance.line2.points = [instance.rect1.pos[0]+instance.rect1.size[0]*(2/3), instance.rect1.pos[1]+instance.rect1.size[1]/1,
                                 instance.rect1.pos[0]+instance.rect1.size[0]*(2/3), instance.rect1.pos[1]] 

        instance.line3.points = [instance.rect1.pos[0], instance.rect1.pos[1]+instance.rect1.size[1]*(2/3),
                                 instance.rect1.pos[0]+instance.rect1.size[0], instance.rect1.pos[1]+instance.rect1.size[1]*(2/3)]
        
        instance.line4.points = [instance.rect1.pos[0], instance.rect1.pos[1]+instance.rect1.size[1]*(1/3),
                                 instance.rect1.pos[0]+instance.rect1.size[0], instance.rect1.pos[1]+instance.rect1.size[1]*(1/3)]    
    
    def update_rect2(self, instance, value):
        instance.rect2.pos = instance.pos#(self.pos[0]+self.size[0]*0.1,self.pos[1]+self.size[1]*0.03)
        instance.rect2.size = instance.size#(self.size[0]*0.3, self.size[1]/2*0.3)
        instance.l2.pos = instance.pos
#        instance.l2.size = instance.l2.texture_size
        instance.l2.font_size = instance.size[0]/5
#        instance.l2.pos = (self.pos[0]+instance.rect2.pos[0]+instance.rect2.size[0]/2.7, 
#                           self.pos[1]+instance.rect2.pos[1]+instance.rect2.size[1]*0.7)
#        instance.line5.circle = (self.pos[0]+self.size[0]*0.25, self.pos[1]+self.size[1]*0.155, instance.rect5.size[0]/3.5)
        instance.line2.circle = (instance.rect2.pos[0]+instance.rect2.size[0]/2, 
                                 instance.rect2.pos[1]+instance.rect2.size[1]/2.5, instance.rect2.size[0]/5)

        
    def update_rect3(self, instance, value):
        instance.rect3.pos = instance.pos#(self.pos[0]+self.size[0]*0.1,self.pos[1]+self.size[1]*0.03)
        instance.rect3.size = instance.size#(self.size[0]*0.3, self.size[1]/2*0.3)
        instance.l3.pos = instance.pos
#        instance.l2.size = instance.l2.texture_size
        instance.l3.font_size = instance.size[0]/5
        instance.line6.points = [instance.rect3.pos[0]+instance.rect3.size[0]*0.15, instance.rect3.pos[1]+instance.rect3.size[1]*0.22,
                                 instance.rect3.pos[0]+instance.rect3.size[0]*0.73, instance.rect3.pos[1]+instance.rect3.size[1]*0.55]
        instance.line7.points = [instance.rect3.pos[0]+instance.rect3.size[0]*0.18, instance.rect3.pos[1]+instance.rect3.size[1]*0.55,
                                 instance.rect3.pos[0]+instance.rect3.size[0]*0.73, instance.rect3.pos[1]+instance.rect3.size[1]*0.22]
        
    def update_rect4(self, instance, value):
        instance.rect4.pos = instance.pos#(self.pos[0]+self.size[0]*0.1,self.pos[1]+self.size[1]*0.03)
        instance.rect4.size = instance.size#(self.size[0]*0.3, self.size[1]/2*0.3)
        instance.line8.circle = (instance.rect4.pos[0]+instance.rect4.size[0]*0.05, 
                                 instance.rect4.pos[1]+instance.rect4.size[1]*0.35, instance.rect4.size[1]*0.15)
        
        instance.l4.pos = instance.pos
        instance.l4.font_size = instance.size[1]*0.33
        
        instance.line9.points = [instance.rect4.pos[0]+instance.rect4.size[0]*0.45, instance.rect4.pos[1]+instance.rect4.size[1]*0.17,
                                 instance.rect4.pos[0]+instance.rect4.size[0]*0.5, instance.rect4.pos[1]+instance.rect4.size[1]*0.5]
        instance.line10.points = [instance.rect4.pos[0]+instance.rect4.size[0]*0.45, instance.rect4.pos[1]+instance.rect4.size[1]*0.5,
                                 instance.rect4.pos[0]+instance.rect4.size[0]*0.5, instance.rect4.pos[1]+instance.rect4.size[1]*0.22]
        
        instance.l5.pos = instance.pos
        instance.l5.font_size = instance.size[1]*0.33
        instance.l6.pos = instance.pos
        instance.l6.font_size = instance.size[1]*0.33
        instance.l7.pos = instance.pos
        instance.l7.font_size = instance.size[1]*0.33
        instance.l8.pos = instance.pos
        instance.l8.font_size = instance.size[1]*0.33
        instance.l9.pos = instance.pos
        instance.l9.font_size = instance.size[1]*0.33
        
    def update_rect_ch(self, instance, value):
        print(instance.size)
        instance.rectch1.rectangle = [instance.pos[0], instance.pos[1]+instance.size[1]/3.5, instance.size[0]/7,instance.size[0]/7]
        instance.rectch.pos = instance.pos
        instance.rectch.size = instance.size
        instance.lbl1.pos = [instance.pos[0], instance.pos[1]]
        instance.lbl1.font_size = instance.size[0]/7
#        print(instance.lbl1.pos)
#        instance.lbl2.pos = instance.pos
        instance.checkbox1.pos_hint = {'center_x':0., 'center_y':0.6}
#        instance.checkbox2.pos = instance.pos
        instance.checkbox1.size = instance.size
#        instance.checkbox2.size = instance.size
        
#        print(dir(instance.checkbox1))

class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    def build_config(self, config):
        config.setdefaults('result', {
            'o_win': 0,
            'x_win': 0,
            'draw' : 0
        })
    
    def build(self):
        config = self.config
        return lyt(config)


if __name__ == '__main__':
    MyApp().run()
