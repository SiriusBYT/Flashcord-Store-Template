"""
This tool lets you quickly configure your page in a hurry.
Read https://github.com/SiriusBYT/Flashcord/wiki/The-Flashcord-Store-Template for how this file works.

This script does not do the following and will never do it:
- Configure long descriptions manually with SNDL (see MarkSNDL when it comes out if you can't be fucked learning SNDL, it will convert Markdown to SNDL's structure.)
- Set "Other Modules by X" embeds
"""

# Edit the following things
IsRepluggedPlugin = False
IsRepluggedTheme = False # TBD, does absolutely nothing for now
Name = "Epic Flashcord Module"
Short_Description = "This module was created using the Flashcord Store Quick Config Python Script!"
Version = "v6.9"
License_Year = "2024"
License = "License dz nuts"


GitHub_Profile = "SiriusBYT"
GitHub_Repo = "Flashcord"
GitHub_Contributors = "SiriusBYT"

Discord = "https://discord.gg/404"
SNDL_Theme = "Dark"
Embed_Color = "#FF0000"

Store_Page_Name = "module_template.html" # NO capitals! Underscores only! CANNOT HAVE "-files" AT THE END!
Folder_Name = "module_template-files" # NO capitals! Underscores only! Must have "-files" at the end!
Embed_FileName = "embed-banner.png" # Notice: GIFs work!
Store_Embed_FileName = "embed-banner.png" # I would still suggest against it due to AuraCloud-E2A's limited space.

StorePage_Template = "store_template.html" # NOT recommended to modify, do this only if you know what you're doing!

# This code is disgusting but it works, will optimize when I feel like it.
# NOTICE: this has ZERO error handling (or very little)! This is fucking horrible but I don't know yet how to do those and at the time of writing it's fucking 23h28
def FileBackup(FileToBackup):
    print("[FlashCFG // Backup] The ", FileToBackup, "will now be backed up...")
    if FileToBackup == "Store Page":
        if IsRepluggedPlugin == True:
            HTMLFile = "flashcord/store/plugins/" + + "/" + Store_Page_Name
            print("[FlashCFG // Backup] ", FileToBackup, "will now be backed up...")
        else:
            HTMLFile = "flashcord/store/modules/" + "/" + Store_Page_Name
    elif FileToBackup == "Embed":
        if IsRepluggedPlugin == True:
            HTMLFile = "flashcord/store/plugins/" + Folder_Name + "/embed.html"
        else:
            HTMLFile = "flashcord/store/modules/" + Folder_Name + "/embed.html"
    else:
        print("")
    HTMLFile_Backup = HTMLFile.replace(".html",".bak-html")
    with open(HTMLFile, 'r', encoding='utf-8') as HTMLFile_File:
        with open(HTMLFile_Backup, 'w', encoding='utf-8') as HTMLFile_Backup_File:
            HTMLFile_Backup_File.write((HTMLFile_File.read()))

def HTMLConfigurator():
    StoreHTML = HTMLFile = "flashcord/store/plugins/" + Store_Page_Name
    # We're doing this the MarkSNDL way, I can't fucking figure out how to do this the objectively better way
    # This is surprisingly way better than the current version of MarkSNDL though LMFAO
    with open(StoreHTML_Backup, 'r', encoding='utf-8') as StoreHTML_Backup_File:
        with open(StoreHTML, 'w', encoding='utf-8') as StoreHTML_File:
            StoreHTML_File.write("")
        with open(StoreHTML, 'a', encoding='utf-8') as StoreHTML_File:
            HTMLArray = StoreHTML_Backup_File.readlines()
            for line in range (len(HTMLArray)):
                # print('[FlashCGG] Processing Line"', line, '" which is "', HTMLArray[line], '".')
                HTMLArray[line] = HTMLArray[line].replace("[NAME]", Name)
                HTMLArray[line] = HTMLArray[line].replace("[SHORT_DESC]", Short_Description)
                HTMLArray[line] = HTMLArray[line].replace("[VERSION]", Version)
                HTMLArray[line] = HTMLArray[line].replace("[LICENSE_YEAR]", License_Year)
                HTMLArray[line] = HTMLArray[line].replace("[LICENSE]", License)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_PROFILE]", GitHub_Profile)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_REPO]", GitHub_Repo)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_CONTRIBUTORS]", GitHub_Contributors)
                HTMLArray[line] = HTMLArray[line].replace("[DISCORD_LINK]", Discord)
                HTMLArray[line] = HTMLArray[line].replace("[THEME]", SNDL_Theme)
                HTMLArray[line] = HTMLArray[line].replace("[EMBED_COLOR]", Embed_Color)
                HTMLArray[line] = HTMLArray[line].replace("[STORE_PAGE_NAME]", Store_Page_Name)
                HTMLArray[line] = HTMLArray[line].replace("[FOLDER_NAME]", Folder_Name)
                HTMLArray[line] = HTMLArray[line].replace("[EMBED_FILENAME]", Embed_FileName)
                HTMLArray[line] = HTMLArray[line].replace("[STORE_EMBED_FILENAME]", Store_Embed_FileName)
                StoreHTML_File.write(HTMLArray[line])
                ProccessingProgress = (line/len(HTMLArray))*100
                print('[FlashCFG // HTMLCFG] Proccessed Line', line, '/', len(HTMLArray), '(', ProccessingProgress, '%).')
                # print('[FlashCGG] Processed Line is now "', HTMLArray[line], '".')

def FlashcordStoreConfig():
    FileBackup("StorePage")
    HTMLArray = []
    print("[FlashCFG] - Quickly Configuring the Store Page...")


        print("[FlashCFG] - Backing up embed page files...")

        EmbedHTML_Backup = EmbedHTML.replace(".html",".bak-html")
        with open(EmbedHTML, 'r', encoding='utf-8') as EmbedHTML_File:
            with open(EmbedHTML_Backup, 'w', encoding='utf-8') as EmbedHTML_Backup_File:
                EmbedHTML_Backup_File.write((EmbedHTML_File.read()))

        HTMLArray = []
        print("[FlashCFG] - Quickly Configuring the Embed Page...")
        with open(EmbedHTML_Backup, 'r', encoding='utf-8') as EmbedHTML_Backup_File:
            with open(EmbedHTML, 'w', encoding='utf-8') as EmbedHTML_File:
                EmbedHTML_File.write("")
            with open(EmbedHTML, 'a', encoding='utf-8') as EmbedHTML_File:
                HTMLArray = EmbedHTML_Backup_File.readlines()
                for line in range (len(HTMLArray)):
                    print('[FlashCGG] Processing Line"', line, '" which is "', HTMLArray[line], '".')
                    HTMLArray[line] = HTMLArray[line].replace("[NAME]", Name)
                    HTMLArray[line] = HTMLArray[line].replace("[SHORT_DESC]", Short_Description)
                    HTMLArray[line] = HTMLArray[line].replace("[VERSION]", Version)
                    HTMLArray[line] = HTMLArray[line].replace("[LICENSE_YEAR]", License_Year)
                    HTMLArray[line] = HTMLArray[line].replace("[LICENSE]", License)
                    HTMLArray[line] = HTMLArray[line].replace("[GITHUB_PROFILE]", GitHub_Profile)
                    HTMLArray[line] = HTMLArray[line].replace("[GITHUB_REPO]", GitHub_Repo)
                    HTMLArray[line] = HTMLArray[line].replace("[GITHUB_CONTRIBUTORS]", GitHub_Contributors)
                    HTMLArray[line] = HTMLArray[line].replace("[DISCORD_LINK]", Discord)
                    HTMLArray[line] = HTMLArray[line].replace("[THEME]", SNDL_Theme)
                    HTMLArray[line] = HTMLArray[line].replace("[EMBED_COLOR]", Embed_Color)
                    HTMLArray[line] = HTMLArray[line].replace("[STORE_PAGE_FILENAME]", Store_Page_Name)
                    HTMLArray[line] = HTMLArray[line].replace("[FOLDER_NAME]", Folder_Name)
                    HTMLArray[line] = HTMLArray[line].replace("[EMBED_FILENAME]", Embed_FileName)
                    HTMLArray[line] = HTMLArray[line].replace("[STORE_EMBED_FILENAME]", Store_Embed_FileName)
                    EmbedHTML_File.write(HTMLArray[line])
                    print('[FlashCGG] Processed Line is now "', HTMLArray[line], '".')



    return

FlashcordStoreConfig()