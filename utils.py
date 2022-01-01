import os
import bs4
import requests
import urllib.request as req
import numpy as np
from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookParser
# from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(id, message)

    return "OK"

def show_manual(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Manual template',
        template=ButtonsTemplate(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='遊戲推薦',
                    text='遊戲查詢',
                    actions=[
                        MessageTemplateAction(
                            label='2021年前3遊戲',
                            text='show 2021 best game'
                        ),
                        MessageTemplateAction(
                            label='遊戲分類',
                            text='game classify'
                        ),
                    ]
            )
    )
    
    line_bot_api.push_message(id, message)

    return "OK"

def send_button_game_classify(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=ButtonsTemplate(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='遊戲類型',
                    text='你喜歡玩什麼類型的遊戲？',
                    actions=[
                        MessageTemplateAction(
                            label='角色扮演',
                            text='角色扮演'
                        ),
                        MessageTemplateAction(
                            label='策略',
                            text='策略'
                        ),
                        MessageTemplateAction(
                            label='休閒',
                            text='休閒'
                        ),
                        MessageTemplateAction(
                            label='多人合作',
                            text='多人合作'
                        )
                    ]
            )
    )
    
    line_bot_api.push_message(id, message)

    return "OK"

def show_bestgame_2021(id):
    line_bot_api = LineBotApi(channel_access_token)
    # web crawler ------------------------------------------------
    url = "https://zh-hant.10besty.com/best-steam-games/"
    request = req.Request(url,headers={
        "Content-Type":"text/html; charset=UTF-8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

    })

    with req.urlopen(request) as response:
        result = response.read().decode("utf-8")
    root = BeautifulSoup(result,"html.parser")

    containers = root.find_all('h2')
    i=0
    titles = []
    imgs = []
    urls = []
    uptexts = []
    labels = []
    for container in containers:
        game = container.findChildren('td')
        img = container.findNext('div').findChild('img').get('data-src')
        td = container.findNextSibling('table').findChildren('td')
        url = td[3].findChild('a').get('href')
        uptext = container.findNextSibling('p')
        if(i<3):
            titles.append(game[1].text)
            imgs.append(img)
            urls.append(url)
            uptexts.append(uptext.text)
            labels.append("購買鏈接")
        i+=1
    # web crawler ------------------------------------------------

    # message packaging ------------------------------------------

    if send_button_carousel(id,imgs,urls,titles,uptexts,labels) == "OK":
        return "OK"

def send_button_carousel(id,imgs,urls,titles,uptexts,labels):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=imgs[0],
                    title=titles[0],
                    text=uptexts[0],
                    actions=[
                        URITemplateAction(
                            label=labels[0],
                            uri=urls[0]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=imgs[1],
                    title=titles[1],
                    text=uptexts[1],
                    actions=[
                        URITemplateAction(
                            label=labels[1],
                            uri=urls[1]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=imgs[2],
                    title=titles[2],
                    text=uptexts[2],
                    actions=[
                        URITemplateAction(
                            label=labels[2],
                            uri=urls[2]
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"
