class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6765826972"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002133191051
    TOKEN = "6785717206:AAEzOZVgWP0D9H-TNo4b8HXfoe97ShUJ1B8"
    mongo_url = "mongodb+srv://shuyaaaaa12:NvpoBuRp7MVPcAYA@cluster0.q2yycqx.mongodb.net/"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = "6433468"
    api_hash = "7895dfd061f656367ccab30032"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True