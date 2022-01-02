# TOC Project 2021

## Finite State Machine Graph
<img src='https://user-images.githubusercontent.com/80616480/147854848-508b1540-dd96-4d17-abe9-df56af42f013.png' width = 1000/>

## Run locally
Run python file app.py
Run with ngrok port 8000
Edit linedeveloper webhook url and postfixe with /webhook

## My Linebot
First in user state enter any key to access manual

<img src='https://user-images.githubusercontent.com/80616480/147855085-9391b4ba-8d07-4221-b087-02a8fcb0e17c.jpg' width = 300/>

### Three option to choose in manual state
#### First show the top 3 best games in 2021
Show in carousel columd mode
button below which is the description and the link of the game to steam

<img src='https://user-images.githubusercontent.com/80616480/147855093-59295d59-e220-455a-813e-82b983eec142.jpg' width = 300/>

#### Description

<img src='https://user-images.githubusercontent.com/80616480/147855128-708be69c-ecd0-4ccf-80e0-62a03bb27127.jpg' width = 300/>

#### Link to buy

<img src='https://user-images.githubusercontent.com/80616480/147855135-3b699432-d9f3-4194-901f-43a3ce593379.jpg' width = 300/>

#### Second show the category
1. RPG
2. SLG
3. Casual
4. Co-op

in state above which can see the description of these games and the link of these games in steam
#### Category

<img src='https://user-images.githubusercontent.com/80616480/147855179-cb5e5f99-3fec-41f3-be99-203f6f40e029.jpg' width = 300/>

<img src='https://user-images.githubusercontent.com/80616480/147855181-2f74d7d1-eb13-4417-9300-8af7bfc38603.jpg' width = 300/>

#### Third show the FSM graph of this linebot
Send image in linebot

<img src='https://user-images.githubusercontent.com/80616480/147855283-7f7bd2e8-b336-4abd-9209-87ce781eacf6.jpg' width = 300/>

### Tips
Type manual to back to manual state

Add local project to Heroku project

heroku git:remote -a {HEROKU_APP_NAME}

Upload project

```
git add .
git commit -m "Add code"
git push -f heroku master
```

Set Environment - Line Messaging API Secret Keys

```
heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
```
pygraphviz problem in heroku

run commands below can solve the problems

```
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku-community/apt
```

### Deploy with Github
must include Procfile and requirement.txt , runfile.txt(optional)
push to github branch master and deploy

### Link of server

https://{my_server_name}.herokuapp.com/webhook

### My server link in heroku
https://toc-final-project-2021.herokuapp.com/webhook

### Addition Function
Web-crawler
Send image

##References
https://zh-hant.10besty.com/best-steam-games/
https://zh-hant.10besty.com/best-strategy-games/
https://zh-hant.10besty.com/best-co-op-games/
https://zh-hant.10besty.com/best-casual-games/
https://zh-hant.10besty.com/best-rpg-games/
https://cdn.akamai.steamstatic.com/steamcommunity/public/images/clans/27766192/6da8a65fb75742d808f12ab05b2453b56193e65c/schinese.jpg?t=1640734552
