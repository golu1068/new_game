"""
KivyToast
=========

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example:

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.toast.kivytoast.kivytoast import toast


class Test(MDApp):

    def show_toast(self):
        toast('Test Kivy Toast')

    def build(self):
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        id: toolbar
        title: 'Test Toast'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: '']]

    FloatLayout:

        MDRaisedButton:
            text: 'TEST KIVY TOAST'
            on_release: app.show_toast()
            pos_hint: {'center_x': .5, 'center_y': .5}

'''
        )

Test().run()
"""

from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder

from kivymd import images_path
from kivymd.uix.button import MDFillRoundFlatIconButton
Builder.load_string(
    """
<Toast>:
    canvas:
        Color:
            rgba: 0.1,0.1,0.1,0   #.2, .2, .2, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
#            radius: [15,]
"""
)


class Toast(ModalView):
    duration = NumericProperty(2.5)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.1}
        self.background_color = [0, 0, 0, 0]
        self.background = f"{images_path}transparent.png"
        self.opacity = 0
        self.auto_dismiss = True
#        self.label_toast = MDFillRoundFlatIconButton(text='vlhweljnbwl',icon=("emoticon-happy"))#Label(size_hint=(None, None), opacity=0)
        self.label_toast = MDFillRoundFlatIconButton()#Label(size_hint=(None, None), opacity=0)
        #####################################################################
        self.label_toast._radius = 5
        self.label_toast.children[0].children[0].text_color = (1,1,0,1)   ## emoji color
        self.label_toast.md_bg_color = (0,0,0,1)     ## change the button bg color
         
#        print(self.label_toast.children[0].spacing)
#        self.label_toast.children[0].spacing = dp(1)
#        print(self.label_toast.children[0].spacing)
        
#        print(self.label_toast.children[0].children[0].theme_text_color)
#        self.label_toast.children[0].children[0].theme_text_color = 'Error'
#        print(self.label_toast.children[0].children[0].theme_text_color)
        
#        print((self.label_toast.theme_text_color))
#        self.label_toast.theme_text_color = 'ContrastParentBackground'  ## Chnage the color of text

#        print((self.label_toast.text_color))  ## Change the color of both text and icon
#        self.label_toast.text_color = (1,0,0,1)
#        print((self.label_toast.specific_text_color))  ## same as text color

        #############################################################################
        btn_size = self.label_toast.size
#        self.label_check_texture_size(self, btn_size) #
#        self.label_toast.bind(texture_size=self.label_check_texture_size)
        self.add_widget(self.label_toast)

    def label_check_texture_size(self, instance, texture_size):
        texture_width, texture_height = texture_size
        if texture_width > Window.width:
            instance.text_size = (Window.width - dp(10), None)
            instance.texture_update()
            texture_width, texture_height = instance.texture_size
        self.size = (texture_width + 65, texture_height + 45)

    def toast(self, text_toast, icon):
        self.pos_hint = {"center_x": 0.5, "center_y": 0.9}
        self.label_toast.text = text_toast
        self.label_toast.icon = icon
        self.open()

    def on_open(self):
        self.fade_in()
        Clock.schedule_once(self.fade_out, self.duration)

    def fade_in(self):
        Animation(opacity=1, duration=0.1).start(self.label_toast)
        Animation(opacity=1, duration=0.1).start(self)

    def fade_out(self, interval):
        Animation(opacity=0, duration=0.4).start(self.label_toast)
        anim_body = Animation(opacity=0, duration=0.4)
        anim_body.bind(on_complete=lambda *x: self.dismiss())
        anim_body.start(self)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            if self.auto_dismiss:
                self.dismiss()
                return False
        super(ModalView, self).on_touch_down(touch)
        return True


def toast(text, duration=2.5, icon='emoticon-tounge'):
    Toast(duration=duration).toast(text, icon=icon)
