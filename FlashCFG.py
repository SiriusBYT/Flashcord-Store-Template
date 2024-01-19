"""
This tool lets you quickly configure your page in a hurry.
Currently does not work/untested. Please do not use in production.
either way this does literally nothing rn lol cuz me lazy lul

This script does not do the following:
- Configure long descriptions
- Set "Other Modules by X" embeds
"""

# Edit the following things
IsPlugin = False
Name = "Epic Flashcord Module"
Short_Description = "This module was created using the Flashcord Store Quick Config Python Script!"
Version = "v6.9"
License = "License dz nuts"

GitHub_Profile = "SiriusBYT"
GitHub_Repo = "Flashcord"
GitHub_Contributors = "SiriusBYT"

Discord = "https://discord.gg/404"
SNDL_Theme = "Dark"
Embed_Color = "#FF0000"

Store_Page_Name = "module_name.html" # NO capitals! Underscores only! CANNOT HAVE "-files" AT THE END!

Folder_Name = "module_name-files" # NO capitals! Underscores only! Must have "-files" at the end!
Embed_FileName = "embed-banner.jpg"
Store_Embed_FileName = "embed-banner.jpg"

def FlashcordStoreConfig():
    print("[FlashCFG] - Backing up files...")
    if IsPlugin == True:
        StoreHTML = "flashcord/store/plugins/" + Store_Page_Name
    else:
        StoreHTML = "flashcord/store/modules/" + Store_Page_Name
    StoreHTML_Backup = StoreHTML.replace(".html",".bak-html")
    with open(StoreHTML, 'r', encoding='utf-8') as StoreHTML_File:
        with open(StoreHTML_Backup, 'w', encoding='utf-8') as StoreHTML_Backup_File:
            StoreHTML_Backup_File.write((StoreHTML_File.read()))

    HTMLArray = []
    print("[FlashCFG] - Quickly Configuring the Store Page...")
    # We're doing this the MarkSNDL way, I can't fucking figure out how to do this the objectively better way
    with open(StoreHTML_Backup, 'r', encoding='utf-8') as StoreHTML_Backup_File:
        with open(StoreHTML, 'w', encoding='utf-8') as StoreHTML_File:
            StoreHTML_File.write("")
        with open(StoreHTML, 'a', encoding='utf-8') as StoreHTML_File:
            HTMLArray = StoreHTML_Backup_File.readlines()
            for line in range (len(HTMLArray)):
                print('[FlashCGG] Processing Line"', line, '" which is "', HTMLArray[line], '".')
                HTMLArray[line] = HTMLArray[line].replace("[NAME]", Name)
                HTMLArray[line] = HTMLArray[line].replace("[SHORT_DESC]", Short_Description)
                HTMLArray[line] = HTMLArray[line].replace("[VERSION]", Version)
                HTMLArray[line] = HTMLArray[line].replace("[LICENSE]", License)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_PROFILE]", GitHub_Profile)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_REPO]", GitHub_Repo)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_CONTRIBUTERS]", GitHub_Contributors)
                HTMLArray[line] = HTMLArray[line].replace("[DISCORD_LINK]", Discord)
                HTMLArray[line] = HTMLArray[line].replace("[THEME]", SNDL_Theme)
                HTMLArray[line] = HTMLArray[line].replace("[EMBED_COLOR]", Embed_Color)
                HTMLArray[line] = HTMLArray[line].replace("[FOLDER_NAME]", Folder_Name)
                HTMLArray[line] = HTMLArray[line].replace("[EMBED_FILENAME]", Embed_FileName)
                HTMLArray[line] = HTMLArray[line].replace("[STORE_EMBED_FILENAME]", Store_Embed_FileName)
                StoreHTML_File.write(HTMLArray[line])
                print('[FlashCGG] Processed Line is now "', HTMLArray[line], '".')
    return

FlashcordStoreConfig()