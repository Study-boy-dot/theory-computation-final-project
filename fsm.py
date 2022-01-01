from transitions.extensions import GraphMachine

from utils import send_button_carousel,send_button_game_classify, send_text_message,show_bestgame_2021,show_manual
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_rpg(self,event):
        text = event.message.text
        return text.lower() == "角色扮演" 

    def is_going_to_slg(self,event):
        text = event.message.text
        return text.lower() == "策略" 

    def is_going_to_casual(self,event):
        text = event.message.text
        return text.lower() == "休閒" 

    def is_going_to_coorperation(self,event):
        text = event.message.text
        return text.lower() == "多人合作" 

    def is_going_to_manual(self,event):
        text = event.message.text
        return text.lower() == "manual"

    def is_going_to_show_bestgame(self,event):
        text = event.message.text
        return text.lower() == "show 2021 best game"

    def is_going_to_game_classify(self, event):
        text = event.message.text
        return text.lower() == "game classify"

    def on_enter_rpg(self,event):
        print("Entering RPG")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger rpg")
        self.go_back()

    def on_exit_rpg(self):
        print("Exiting RPG")

    def on_enter_manual(self, event):
        print("Entering Manual")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger manual")
        userid = event.source.user_id
        show_manual(userid)

    def on_enter_rpg(self, event):
        print("Entering RPG")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger RPG")
        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_slg(self, event):
        print("Entering SLG")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger SLG")
        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_casual(self, event):
        print("Entering Casual")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger Casual")
        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_coorperation(self, event):
        print("Entering coorperation")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger coorperation")
        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_show_bestgame(self, event):
        print("Entering best game 2021")
        userid = event.source.user_id
        show_bestgame_2021(userid)

    def on_enter_game_classify(self, event):
        print("Entering game classify")
        userid = event.source.user_id
        send_button_game_classify(userid)