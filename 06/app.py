from flask import Flask, request, abort,render_template,redirect

import json,urllib.request



from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    StickerMessage,
    Emoji,
    ImageMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    StickerMessageContent,
    
)

app = Flask(__name__)

myT='YOUR_CHANNEL_ACCESS_TOKEN'
myC='YOUR_CHANNEL_SECRET'

configuration = Configuration(access_token=myT)
handler = WebhookHandler(myC)

ansA=[]
city=''

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=(API授權碼)&format=JSON'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

def myG(aa):
    ansA.clear()
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location=output['records']['location']
    for i in location:
        city = i['locationName']
        if city==aa:
            wx = i['weatherElement'][0]['time'][0]['parameter']['parameterName']
            maxtT = i['weatherElement'][4]['time'][0]['parameter']['parameterName']
            mintT = i['weatherElement'][2]['time'][0]['parameter']['parameterName']
            ci = i['weatherElement'][3]['time'][0]['parameter']['parameterName']
            pop = i['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            ansA.append(city)
            ansA.append(wx)
            ansA.append(mintT)
            ansA.append(maxtT)
    return ansA   


@handler.add(MessageEvent, message=StickerMessageContent)
def handle_sticker_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[StickerMessage(
                    package_id=event.message.package_id,
                    sticker_id=event.message.sticker_id)
                ]
            )
        )


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    getText=event.message.text
    #bb=myG('新北市')
    #print(bb[3])
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        if getText=='1':            
            line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
            messages=[
                TextMessage(text='回傳:2023/10/26'),
                TextMessage(text='答案是~' + str(myG('臺北市')))
           ]
            
            )
        )
        elif getText=='2':            
            line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=str(myG('桃園市')))]
            )
        )
        elif getText=='3':            
            line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=str(myG('新竹市'))),]
            )
        )
        elif getText=='4':            
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[StickerMessage(
                    package_id='446',
                    sticker_id='1988')
                ]
            )
        )
        elif getText=='5':
            emojis = [Emoji(index=0, product_id="5ac1bfd5040ab15980c9b435", emoji_id="001"),
                      Emoji(index=13, product_id="5ac1bfd5040ab15980c9b435", emoji_id="002")]
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='$ LINE emoji $', emojis=emojis)]
                )
            )
        elif getText=='6':            
            
            url='https://avatars.githubusercontent.com/u/100542608?s=96&v=4'
            
            app.logger.info("url=" + url)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(original_content_url=url, preview_image_url=url)
                    ]
                )
            )
        else:
            line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text='1->臺北市.2->桃園市.3->新竹市')]
            )
        )



if __name__ == "__main__":
    app.run(debug=True)