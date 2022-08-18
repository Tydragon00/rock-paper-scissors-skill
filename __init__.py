import random
import time
from mycroft import MycroftSkill, intent_handler


class RockPaperScissors(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)
        self.rps = ['Paper', 'Rock', 'Scissors']
        self.URock = False
        self.UPaper = False
        self.UScissors = False
        self.CRock = False
        self.CPaper = False
        self.CScissors = False

    @intent_handler('scissors.paper.rock.intent')
    def handle_request_scissorsPaperRock(self):
        # Welcome
        welcome_msg = "Welcome in 'Rock Paper Scissor' game"
        self.speak_dialog(welcome_msg)
        self.gui.show_text(welcome_msg)
        # Player choice
        self.gui.show_image(
            "https://miro.medium.com/max/800/1*8du96SQUQ0NlWmWvVu20Zw.png")

        rockImage = "https://images.unsplash.com/photo-1525857597365-5f6dbff2e36e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cm9ja3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
        paperImage = "https://images-na.ssl-images-amazon.com/images/I/91TzIzfZElL._AC._SR360,460.jpg"
        scissorImage = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-72665433-1579643451.jpg?resize=980:*"
        winImage = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyT9IK7PLXCw56mul2lMkok58d1o850D8N_g&usqp=CAU"
        loseImage = "https://media.istockphoto.com/vectors/game-over-on-screen-the-round-face-of-a-deceased-character-vector-id1199952763?k=20&m=1199952763&s=612x612&w=0&h=486yMqE8eKK7sMYFyzOd6GI26Ufgans95oMFBxLu_s0="
        tieImage = "https://www.studioorlandi.it/wp-content/uploads/2016/02/punto-di-pareggio-punto-di-equilibrio-break-even-point_opt1.jpg"
        selection = self.ask_selection(self.rps, 'Choose..')
        self.speak_dialog('player choice', {'type': selection})
        if (selection == 'Rock'):
            self.gui.show_image(rockImage)
            self.URock = True
        elif (selection == 'Paper'):
            self.gui.show_image(paperImage)
            self.UPaper = True
        elif (selection == 'Scissors'):
            self.gui.show_image(scissorImage)
            self.UScissors = True
        else:
            self.speak_dialog('Error: invalid choice')

        time.sleep(2)
        self.speak_dialog('Well, now it is my turn to choose')
        time.sleep(3)
        mylist = ['Paper', 'Rock', 'Scissors']
        selections = random.choice(mylist)
        if (selections == 'Rock'):
            self.CRock = True
            self.gui.show_image(rockImage)
            self.speak_dialog('cpu choice', {'choice': selections})
        elif (selections == 'Paper'):
            self.CPaper = True
            self.gui.show_image(paperImage)
            self.speak_dialog('cpu choice', {'choice': selections})
        elif (selections == 'Scissors'):
            self.CScissors = True
            self.gui.show_image(scissorImage)
            self.speak_dialog('cpu choice', {'choice': selections})
        else:
            self.speak_dialog('Error: invalid choice')

        time.sleep(2)
        if ((self.CPaper and self.UPaper) or (self.CRock and self.URock) or (self.CScissors and self.UScissors)):
            self.speak_dialog('That is a draw')
            self.gui.show_image(tieImage)
        elif ((self.CPaper and self.UScissors) or
              (self.CRock and self.UPaper) or
              (self.CScissors and self.URock)):
            self.speak_dialog('Congratulations, you win')
            self.gui.show_image(winImage)
        else:
            self.speak_dialog('Oh yes, I win')
            self.gui.show_image(loseImage)

        self.URock = False
        self.UPaper = False
        self.UScissors = False
        self.CRock = False
        self.CPaper = False
        self.CScissors = False


def create_skill():
    return RockPaperScissors()
