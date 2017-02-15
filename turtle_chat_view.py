#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE!
'Zain'

import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput

class start_menu:

    _SCREEN_WIDTH=500
    _SCREEN_HEIGHT=600

    def __init__(self):

        turtle.setup( width = self._SCREEN_WIDTH, height = self._SCREEN_HEIGHT )

        self.background()
        self.StartButton()
        self.Logo()
        self.Write_Start()

    def background(self):

        self.background = turtle.clone()
        turtle.register_shape('STARTMENU.gif')
        self.background.penup()
        self.background.goto(0,0)
        self.background.shape('STARTMENU.gif')

    def StartButton(self):

        self.button = turtle.clone()
        self.button.shape('square')
        self.button.penup()
        self.button.shapesize(2,10)
        self.button.color("white")
        self.button.goto(0,-50)

    def Logo(self):

        self.logo = turtle.clone()
        turtle.register_shape('Logo.gif')
        self.logo.penup()
        self.logo.goto(0,0)
        self.logo.shape('Logo.gif')

    def Write_Start(self):

        self.wrt_strt = turtle.clone()
        self.wrt_strt.penup()
        self.wrt_strt.pencolor("black")
        self.wrt_strt.hideturtle()
        self.wrt_strt.goto(-30,-212)
        self.wrt_strt.write('START', font = ('Courier',17,'bold'))

class TextBox(TextInput):

    def __init__(self):

        super(TextBox, self).__init__(pos = (0,-50))

        self.font = ('Courier',14,'bold')

        self.msg_box()

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

    def msg_box(self):

        self.msg_box = turtle.clone()
        self.msg_box.pencolor('white')
        self.msg_box.speed(0)
        self.msg_box.pensize(5)
        self.msg_box.hideturtle()
        self.msg_box.penup()
        self.msg_box.goto(-self.width/2+self.pos[0],100)
        self.msg_box.pendown()
        self.msg_box.goto(self.width/2+self.pos[0],100)
        self.msg_box.pensize(2)
        self.msg_box.goto(self.width/2+self.pos[0],200)
        self.msg_box.goto(-self.width/2+self.pos[0],200)
        self.msg_box.pensize(2)
        self.msg_box.goto(-self.width/2+self.pos[0],100)

    def write_msg(self):
        
        self.writer.clear()
        self.writer.pencolor("white")
        self.writer.write(self.new_msg , font = self.font)
        self.my_pos = self.writer.pos()
        self.x_pos = self.my_pos[0]

        if self.x_pos >= 90:

            self.writer.write(self.new_msg + "\r", font = self.font)

        else:
            self.writer.write(self.new_msg , font = self.font)

class SendButton(Button):

    def __init__(self, view):

        super(SendButton,self).__init__(pos = (0,-200))
        self.turtle.color("grey")

        self.view = view
        self.Write_Send()

    def Write_Send(self):

        self.wrt_snd = turtle.clone()
        self.wrt_snd.penup()
        self.wrt_snd.pencolor("white")
        self.wrt_snd.hideturtle()
        self.wrt_snd.goto(-30,-212)
        self.wrt_snd.write('SEND', font = ('Courier',17,'bold'))
        self.wrt_snd.onclick(self.fun)
        turtle.listen()

    def fun(self, x=None, y=None):

        self.view.send_msg()

class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=500
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Anonymous'):
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        ###

        self.username = username
        self.partner_name = partner_name
        
        #Make a new client object and store it in this instance.

        self.my_client = Client()
        
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.

        turtle.setup( width = self._SCREEN_WIDTH, height = self._SCREEN_HEIGHT )

        self.background = turtle.clone()
        turtle.register_shape("NYCBG4.gif")
        self.background.shape("NYCBG4.gif")
        self.background.goto(0,10)
        
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        
        self.msg_queue=[]

        self.textbox = TextBox()
        self.send_btn = SendButton(self)
        
        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
        
        self.display = turtle.clone()    
        self.display.penup()
        self.display.pencolor('white')
        self.display.speed(0)
        self.display.hideturtle()
        self.display.goto(-self.textbox.width/2+10+self.textbox.pos[0],180)
        
        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###

        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###

        self.setup_listeners()

    def send_msg(self):
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also call update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        
        self.my_client.send(self.textbox.new_msg)
        self.msg_queue.insert(0,self.textbox.new_msg)
        self.textbox.clear_msg()
        self.display_msg()

    def get_msg(self):
        
        return self.textbox.get_msg()

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''

        turtle.onkeypress( self.send_btn.fun, 'Return' )
        turtle.listen()

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        self.msg_queue.insert(0,show_this_msg)
        #Then, call the display_msg method to update the display
        self.display_msg()

    def display_msg(self):
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
        self.display.clear()
        self.display.write(self.msg_queue[0], font = self.textbox.font)
        
##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
        
if __name__ == '__main__':
    my_start_menu = start_menu()
    _WAIT_TIME=200 #Time between check for new message, ms

    def Start(self, x=None, y=None):
        
        my_view=View()
        
        def check() :
            msg_in=my_view.my_client.receive()
            if not(msg_in is None):
                if msg_in==my_view.my_client._END_MSG:
                    print('End message received')
                    sys.exit()
                else:
                    my_view.textbox.msg_box.goto(my_view.textbox.width/2+my_view.textbox.pos[0],100)
                    my_view.textbox.msg_box.goto(my_view.textbox.width/2+my_view.textbox.pos[0],230)
                    my_view.textbox.msg_box.goto(-my_view.textbox.width/2+my_view.textbox.pos[0],230)
                    my_view.textbox.msg_box.goto(-my_view.textbox.width/2+my_view.textbox.pos[0],100)
                    my_view.msg_received(msg_in)
            turtle.ontimer(check,_WAIT_TIME) #Check recursively
        check()
    my_start_menu.button.onclick(Start)
turtle.mainloop()
