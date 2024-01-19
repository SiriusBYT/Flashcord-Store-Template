"""
This tool lets you quickly configure your page in a hurry.
Currently does not work/untested. Please do not use in production.
either way this does literally nothing rn lol cuz me lazy lul

This script does not do the following:
- Configure long descriptions
- Set "Other Modules by X" embeds
"""

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

Store_Page_Name = "module_name.html"
Folder_Name = "module_name-files"
Embed_FileName = "embed-banner.jpg"

def FlashcordStoreConfig():
    StoreHTML = "flashcord/store/" + Store_Page_Name
    with open(StoreHTML, 'r', encoding='utf-8') as StoreHTML_File:
        with open("outputtest.html", 'w', encoding='utf-8') as FinalStoreHTML_File:
            FinalStoreHTML_File.write(StoreHTML_File.read().replace("[NAME]", Name))
    return

FlashcordStoreConfig()