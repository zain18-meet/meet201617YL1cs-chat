#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE!
'Zain'

#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################

import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput

#####################################################################################
#####################################################################################

#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
#draw_box
#write_msg
#
#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (i.e. go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################

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
        self.msg_box.goto(self.width/2+self.pos[0],250)
        self.msg_box.goto(-self.width/2+self.pos[0],250)
        self.msg_box.goto(-self.width/2+self.pos[0],100)

    def write_msg(self):
        
        self.writer.clear()
        self.writer.pencolor("white")
        self.writer.write(self.new_msg , font = self.font)

#####################################################################################
#                                  SendButton                                       #
#####################################################################################
#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
#fun gets called whenever the button is clicked.  It's jobs will be to
#
# 1. send a message to the other chat participant - to do this,
#    you will need to call the send method of your Client instance
# 2. update the messages that you see on the screen
#
#HINT: You may want to override the __init__ method so that it takes one additional
#      input: view.  This will be an instance of the View class you will make next
#      That class will have methods inside of it to help
#      you send messages and update message displays.
#####################################################################################
#####################################################################################

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

    def fun(self, x=None, y=None):

        self.view.send_msg()

##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################

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

        self.turtles = []
        
        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###

##        for msg in msg_queue:
##
##            self.turtles.append(self.display = turtle.clone())
        
        self.display = turtle.clone()    
        self.display.penup()
        self.display.pencolor('white')
        self.display.speed(0)
        self.display.hideturtle()
        self.display.goto(-self.textbox.width/2+10+self.textbox.pos[0],170)
        
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

        turtle.onkeypress( self.send_btn.fun(), 'return' )
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
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        msg_in=my_view.my_client.receive()
        if not(msg_in is None):
            if msg_in==my_view.my_client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
