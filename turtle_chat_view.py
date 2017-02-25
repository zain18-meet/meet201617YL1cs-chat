#2016-2017 PERSONAL PROJECTS: TurtleChat!

Creator = 'Zain'

import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput

class Start_Menu:

    _SCREEN_WIDTH=500
    _SCREEN_HEIGHT=600

    def __init__(self):

        turtle.setup( self._SCREEN_WIDTH, self._SCREEN_HEIGHT )

        self.background()
        self.StartButton()
        self.Logo()
        self.credits()

    def credits(self):

        self.credits = turtle.clone()
        self.credits.pencolor('white')
        self.credits.hideturtle()
        self.credits.penup()
        self.credits.goto(-220,-275)
        self.credits.write('Created by' + ':' + '\r' + 'Zain Al Qalawi', font = ('Courier',14,'bold'))

    def background(self):

        self.background = turtle.clone()
        turtle.register_shape('STARTMENU.gif')
        self.background.penup()
        self.background.goto(0,0)
        self.background.shape('STARTMENU.gif')

    def StartButton(self):

        self.button = turtle.clone()
        self.button.shape('square')
        self.button.goto(0,-200)
        self.button.penup()
        self.button.shapesize(2,10)
        self.button.color("white")

    def Logo(self):

        self.logo = turtle.clone()
        turtle.register_shape('Logo.gif')
        self.logo.penup()
        self.logo.goto(0,0)
        self.logo.shape('Logo.gif')


class TextBox(TextInput):

    def __init__(self):

        super(TextBox, self).__init__(pos = (0,-50))

        self.font = ('Courier',14,'bold')

        self.Msg_box()
        self.Msg_box2()

    def draw_box(self):

        self.draw = turtle.clone()
        self.draw.hideturtle()
        self.draw.pencolor("white")
        self.draw.speed(0)
        self.draw.penup()
        self.draw.pensize(5)
        self.draw.goto(-self.width/2+self.pos[0],self.pos[1]-self.height)
        self.draw.pendown()
        self.draw.goto(self.width/2+self.pos[0],self.pos[1]-self.height)
        self.draw.goto(self.width/2+self.pos[0],self.pos[1])
        self.draw.goto(-self.width/2+self.pos[0],self.pos[1])
        self.draw.goto(-self.width/2+self.pos[0],self.pos[1]-self.height)

    def Msg_box(self):

        self.msg_box = turtle.clone()
        self.msg_box.hideturtle()
        self.msg_box.pencolor('white')
        self.msg_box.speed(0)
        self.msg_box.pensize(5)
        self.msg_box.penup()
        self.msg_box.goto(self.pos[0],90)
        self.msg_box.pendown()
        self.msg_box.goto(self.width+self.pos[0],90)
        self.msg_box.goto(self.width+self.pos[0],230)
        self.msg_box.goto(self.pos[0],230)
        self.msg_box.goto(self.pos[0],90)

    def Msg_box2(self):

        self.msg_box2 = turtle.clone()
        self.msg_box2.hideturtle()
        self.msg_box2.pencolor('white')
        self.msg_box2.speed(0)
        self.msg_box2.pensize(5)
        self.msg_box2.penup()
        self.msg_box2.goto(-self.width+self.pos[0],90)
        self.msg_box2.pendown()
        self.msg_box2.goto(self.pos[0],90)
        self.msg_box2.goto(self.pos[0],230)
        self.msg_box2.goto(-self.width+self.pos[0],230)
        self.msg_box2.goto(-self.width+self.pos[0],90)


    def write_msg(self):
        
        self.writer.clear()
        self.writer.pencolor("white")
        self.writer.goto(-self.width/2+10+self.pos[0],self.pos[1]-self.height+20)

        if (len(self.new_msg)%17) == 0:
            
            self.new_msg = self.new_msg + '\r'

        self.writer.write(self.new_msg , font = self.font)

class SendButton(Button):

    def __init__(self, view):

        super(SendButton,self).__init__(pos = (0,-200))
        self.turtle.color("grey")

        self.view = view
        self.Write_Send()

    def Write_Send(self):

        self.wrt_snd = turtle.clone()
        self.wrt_snd.hideturtle()
        self.wrt_snd.penup()
        self.wrt_snd.pencolor("white")
        self.wrt_snd.goto(-30,-212)
        self.wrt_snd.write('SEND', font = ('Courier',17,'bold'))
        self.wrt_snd.onclick(self.fun)
        turtle.listen()

    def fun(self, x=None, y=None):

        self.view.send_msg()

class View:
    
    def __init__(self,username='I',partner_name='Anonymous'):

        self.username = username
        self.partner_name = partner_name
        
        self.my_client = Client()
        
        self.msg_queue=[]

        self.Chat_Background()
        
        self.textbox = TextBox()
        self.send_btn = SendButton(self)
        self.Display_turtle_setup()
        self.Sent_Title()
        self.Recieved_Title()

        self.setup_listeners()
        turtle.listen()

    def Chat_Background(self):

        self.background = turtle.clone()
        self.background.speed(0)
        turtle.register_shape("NYCBG1.gif")
        turtle.register_shape("NYCBG2.gif")
        turtle.register_shape("NYCBG3.gif")
        turtle.register_shape("NYCBG4.gif")
        self.background.shape("NYCBG1.gif")
        self.background.goto(0,10)

    def Switch_bg1(self):

        self.background.shape("NYCBG1.gif")
        self.background.goto(0,10)

    def Switch_bg2(self):

        self.background.shape("NYCBG2.gif")
        self.background.goto(0,0)

    def Switch_bg3(self):

        self.background.shape("NYCBG3.gif")
        self.background.goto(0,10)

    def Switch_bg4(self):

        self.background.shape("NYCBG4.gif")
        self.background.goto(0,10)

    def Display_turtle_setup(self):

        self.display = turtle.clone()
        self.display.hideturtle()
        self.display.penup()
        self.display.pencolor('white')
        self.display.speed(0)
        self.display.goto(-self.textbox.width+10+self.textbox.pos[0],105)

        self.display2 = turtle.clone()
        self.display2.hideturtle()
        self.display2.penup()
        self.display2.pencolor('white')
        self.display2.speed(0)
        self.display2.goto(10+self.textbox.pos[0],105)

    def Sent_Title(self):

        self.Sent = turtle.clone()
        self.Sent.speed(0)
        self.Sent.pencolor('white')
        self.Sent.hideturtle()
        self.Sent.penup()
        self.Sent.goto(-130,230)
        self.Sent.write('SENT', font = ('Courier',20,'bold'))

    def Recieved_Title(self):

        self.recieve = turtle.clone()
        self.recieve.speed(0)
        self.recieve.pencolor('white')
        self.recieve.hideturtle()
        self.recieve.penup()
        self.recieve.goto(50,230)
        self.recieve.write('RECIEVED', font = ('Courier',20,'bold'))

    def send_msg(self):

        show_this_msg_u=self.username+ ' sent:\r'+ self.textbox.new_msg
        self.my_client.send(self.textbox.new_msg)
        self.msg_queue.insert(0,show_this_msg_u)
        self.textbox.clear_msg()
        self.display_msg()

    def get_msg(self):
        
        return self.textbox.get_msg()

    def setup_listeners(self):

        turtle.onkeypress( self.send_btn.fun, 'Return' )
        turtle.onkeypress(self.Switch_bg1, "Up")
        turtle.onkeypress(self.Switch_bg2, "Right")
        turtle.onkeypress(self.Switch_bg3, "Down")
        turtle.onkeypress(self.Switch_bg4, "Left")
        turtle.listen()

    def msg_received(self,msg):

        show_this_msg=self.partner_name+ ' sent:\r'+ msg
        self.msg_queue.append(show_this_msg)
        self.display_msg2()

    def display_msg(self):

        self.display.clear()
        self.display.write(self.msg_queue[0], font = self.textbox.font)

    def display_msg2(self):

        self.display2.clear()
        self.display2.write(self.msg_queue[-1], font = self.textbox.font)
        
##############################################################
##############################################################
        
if __name__ == '__main__':
    my_start_menu = Start_Menu()
    _WAIT_TIME=200

    def Start(x=None, y=None):
        
        my_view=View()
        
        def check() :
            msg_in=my_view.my_client.receive()
            if not(msg_in is None):
                if msg_in==my_view.my_client._END_MSG:
                    print('End message received')
                    sys.exit()
                else:
                    my_view.msg_received(msg_in)
            turtle.ontimer(check,_WAIT_TIME)
        check()
    my_start_menu.button.onclick(Start)
    turtle.onkeypress( Start, 'Return')
    turtle.listen()
turtle.mainloop()
