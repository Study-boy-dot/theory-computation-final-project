import os
from re import template
import bs4
from linebot.models.actions import MessageAction
from linebot.models.messages import TextMessage
import requests
import urllib.request as req
import numpy as np
from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookParser
# from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(id, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TextSendMessage(text))

    return "OK"

def send_image_url(id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.push_message(id, message)

    return "OK"

def show_manual(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Manual template',
        template=ButtonsTemplate(
                    thumbnail_image_url='https://cdn.akamai.steamstatic.com/steamcommunity/public/images/clans/27766192/6da8a65fb75742d808f12ab05b2453b56193e65c/schinese.jpg?t=1640734552',
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
                        MessageTemplateAction(
                            label='FSM圖',
                            text='fsm'
                        ),
                    ]
            )
    )
    
    line_bot_api.push_message(id, message)
    return "OK"

def send_button_carousel(id,imgs,urls,titles):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        type="carousel",
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=imgs[0],
                    title=titles[0],
                    text='內容簡介+購買鏈接',
                    actions=[
                        MessageTemplateAction(
                            label='內容簡介',
                            text='第1:'+titles[0]+'內容簡介'
                        ),
                        URITemplateAction(
                            label='購買鏈接（Steam）',
                            uri=urls[0]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=imgs[1],
                    title=titles[1],
                    text='內容簡介+購買鏈接',
                    actions=[
                        MessageTemplateAction(
                            label='內容簡介',
                            text='第2:'+titles[1]+'內容簡介'
                        ),
                        URITemplateAction(
                            label='購買鏈接（Steam）',
                            uri=urls[1]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=imgs[2],
                    title=titles[2],
                    text='內容簡介+購買鏈接',
                    actions=[
                        MessageTemplateAction(
                            label='內容簡介',
                            text='第3:'+titles[2]+'內容簡介'
                        ),
                        URITemplateAction(
                            label='購買鏈接（Steam）',
                            uri=urls[2]
                        )
                    ]
                )
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
                    thumbnail_image_url='https://cdn.akamai.steamstatic.com/steamcommunity/public/images/clans/27766192/6da8a65fb75742d808f12ab05b2453b56193e65c/schinese.jpg?t=1640734552',
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

def show_top3(id,link):
    line_bot_api = LineBotApi(channel_access_token)
    # web crawler ------------------------------------------------
    titles,imgs,urls,brieflys = web_crawler(link)
    # web crawler ------------------------------------------------

    # message packaging ------------------------------------------
    if send_button_carousel(id,imgs,urls,titles) == "OK":
        return "OK"

def show_bestgame_2021(id):
    line_bot_api = LineBotApi(channel_access_token)
    # web crawler ------------------------------------------------
    link = "https://zh-hant.10besty.com/best-steam-games/"
    titles,imgs,urls,brieflys = web_crawler(link)
    # web crawler ------------------------------------------------

    # message packaging ------------------------------------------
    if send_button_carousel(id,imgs,urls,titles) == "OK":
        return "OK"

def show_top3_rpg(id):
    line_bot_api = LineBotApi(channel_access_token)
    # web crawler ------------------------------------------------
    link = "https://zh-hant.10besty.com/best-rpg-games/"
    titles,imgs,urls,brieflys = web_crawler(link)
    # web crawler ------------------------------------------------

    # message packaging ------------------------------------------
    if send_button_carousel(id,imgs,urls,titles) == "OK":
        return "OK"
    
def show_top3_slg(id):
    line_bot_api = LineBotApi(channel_access_token)
    # web crawler ------------------------------------------------
    link = "https://zh-hant.10besty.com/best-strategy-games/"
    titles,imgs,urls,brieflys = web_crawler(link)
    # web crawler ------------------------------------------------

    # message packaging ------------------------------------------
    if send_button_carousel(id,imgs,urls,titles) == "OK":
        return "OK"    
    
def show_top3_casual(id):
    line_bot_api = LineBotApi(channel_access_token)
    # web crawler ------------------------------------------------
    link = "https://zh-hant.10besty.com/best-casual-games/"
    titles,imgs,urls,brieflys = web_crawler(link)
    # web crawler ------------------------------------------------

    # message packaging ------------------------------------------
    if send_button_carousel(id,imgs,urls,titles) == "OK":
        return "OK"

def show_top3_coorperation(id):
    line_bot_api = LineBotApi(channel_access_token)
    # web crawler ------------------------------------------------
    link = "https://zh-hant.10besty.com/best-co-op-games/"
    titles,imgs,urls,brieflys = web_crawler(link)
    # web crawler ------------------------------------------------

    # message packaging ------------------------------------------
    if send_button_carousel(id,imgs,urls,titles) == "OK":
        return "OK"

def send_briefly_message(event,id,titles,brieflys):
    line_bot_api = LineBotApi(channel_access_token)
    text = event.message.text
    if text[1] == '1':
        line_bot_api.push_message(id,TextSendMessage(titles[0]+" -- "+brieflys[0]))
    elif text[1] == '2':
        line_bot_api.push_message(id,TextSendMessage(titles[1]+" -- "+brieflys[1]))
    elif text[1] == '3':
        line_bot_api.push_message(id,TextSendMessage(titles[2]+" -- "+brieflys[2]))
    else:
        return "NOT OK"

    return "OK"

def web_crawler(link):
    # web crawler ------------------------------------------------
    request = req.Request(link,headers={
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
    brieflys = []
    for container in containers:
        game = container.findChildren('td')
        img = container.findNext('div').findChild('img').get('data-src')
        td = container.findNextSibling('table').findChildren('td')
        url = td[3].findChild('a').get('href')
        briefly = container.findNextSibling('p')
        if(i<3):
            titles.append(game[1].text)
            imgs.append(img)
            urls.append(url)
            brieflys.append(briefly.text)
        i+=1
    # web crawler ------------------------------------------------

    return titles,imgs,urls,brieflys
    