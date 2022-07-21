from instapy_cli import client
#import bot
#bot.login()
#bot.copypost()
totag="ss"
username = '2days_leonardo' #your username
password = 'Leonardo1522' #your password
image = 'img.jpg' #here you can put the image directory
text = '#Repost of @2days_leonardo by @2days_leonardo'
with client(username, password) as cli:
    cli.upload(image, text)