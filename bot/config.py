import os

# Debugging ke liye environment variables print karna
print("API_ID:", os.getenv("API_ID"))
print("API_HASH:", os.getenv("API_HASH"))

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN") or "7570456143:AAGf0yle57FwtUNM33QdBvYoflTWjCVdivg"
    API_ID = int(os.getenv("API_ID")) if os.getenv("API_ID") and os.getenv("API_ID").isdigit() else 26079994
    API_HASH = os.getenv("API_HASH") or "5c68a2bb6b5447b7f2d372c8643c44d1"
    
    DATABASE_URL = os.getenv("DATABASE_URL") or ""
    SUDO_USERS = os.getenv("SUDO_USERS") or ""  # Space-separated users
    SUPPORT_CHAT_LINK = os.getenv("SUPPORT_CHAT_LINK") or ""
    DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY") or "./downloads/"
    
    G_DRIVE_CLIENT_ID = os.getenv("G_DRIVE_CLIENT_ID") or ""
    G_DRIVE_CLIENT_SECRET = os.getenv("G_DRIVE_CLIENT_SECRET") or ""

class BotCommands:
    Download = ['download', 'dl']
    Authorize = ['auth', 'authorize']
    SetFolder = ['setfolder', 'setfl']
    Revoke = ['revoke']
    Clone = ['copy', 'clone']
    Delete = ['delete', 'del']
    EmptyTrash = ['emptyTrash']
    YtDl = ['ytdl']

class Messages:
    START_MSG = "**Hi there {}.**\n__I'm Google Drive Uploader Bot. You can use me to upload any file / video to Google Drive from direct link or Telegram Files.__\n__You can know more from /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__I can upload files from direct link or Telegram Files to your Google Drive. All i need is to authenticate me to your Google Drive Account and send a direct download link or Telegram File.__\n\nI have more features... ! Wanna know about it ? Just walkthrough this tutorial and read the messages carefully.",

        f"**Authenticating Google Drive**\n__Send the /{BotCommands.Authorize[0]} commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /{BotCommands.Revoke[0]} to revoke your currently logged Google Drive Account.__\n\n**Note: I will not listen to any command or message (except /{BotCommands.Authorize[0]} command) until you authorize me.\nSo, Authorization is mandatory !**",

        f"**Direct Links**\n__Send me a direct download link for a file and I will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.__\n\n**__Examples:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```",

        f"**Custom Folder for Upload**\n__Want to upload in custom folder or in__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.__",

        f"**Delete Google Drive Files**\n__Use /{BotCommands.Delete[0]} (File/Folder URL) to delete file.__\n__Use /{BotCommands.EmptyTrash[0]} to empty trash.__",

        "**Developed by @Unknown_RK01**"
    ]

    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded, try after 24 hours.__"

    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n__File id - {} Not found. Make sure it exists and is accessible by the logged account.__"

    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in a valid format."

    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"

    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"

    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"

    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.**\n[{}]({}) __({})__"

    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"

    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"

    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"

    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"

    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'

    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate a new one by the Authorization URL__'

    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and copy the final website same like http://localhost/?code= .**\n__Visit the URL > Allow permissions > Copy full website  > Send it here__"

    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"

    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'

    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfully.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'

    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"

    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"

    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you sent is not a folder.__"

    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"

    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with the command.**\n__Usage - /{} (GDrive Link)__"

    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"

    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"

    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"

    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"

    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
