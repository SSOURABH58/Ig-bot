from InstagramAPI.InstagramAPI import InstagramAPI
import bot

bot.login()
bot.copypost()
#bot.dowmlode()
InstagramAPI = InstagramAPI(bot.username,bot.password)
InstagramAPI.login() # login
photo_path = "img.jpg"
caption = bot.totag
InstagramAPI.uploadPhoto(photo_path, caption = caption)