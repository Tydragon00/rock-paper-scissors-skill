from mycroft import MycroftSkill, intent_file_handler


class RockPaperScissors(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('scissors.paper.rock.intent')
    def handle_scissors_paper_rock(self, message):
        self.speak_dialog('scissors.paper.rock')


def create_skill():
    return RockPaperScissors()

