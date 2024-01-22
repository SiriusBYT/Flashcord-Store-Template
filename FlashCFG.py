import api
"""
This tool lets you quickly configure your page in a hurry.
Read https://github.com/SiriusBYT/Flashcord/wiki/The-Flashcord-Store-Template for how this file works.

This script does not do the following but will in the future:
- Set "Other Modules by X" embeds automatically (A long time later! Requires internet & communication to sirio-network.com)
"""

# Edit the following things
isRepluggedPlugin = False
isFlashcordCompetitor = False # TBD, does absolutely nothing for now (Pages for Themes, yes the Flashcord store will... host themes other than Flashcord. This is a stupid idea which is why this isn't implemented yet and why I'm still just thinking about it.)
AllowAPI = True # Allows the script to connect to the SGN servers in order to make your store page more complete without user input


Name = "FlashCFG-Built Store Template"
Short_Description = "This store page was created using the Flashcord Store Quick Config Python Script!"
Version = "v1.2.0"
License_Year = "2024"
License = "Unlicense"


GitHub_Profile = "SiriusBYT" # Notice: this will be converted to lowercase and will be your folder name after modules/plugins
GitHub_Repo = "Flashcord-Store-Template" 
GitHub_Contributors = "SiriusBYT"

Discord = "https://discord.gg/z93kHwGuZt"
SNDL_Theme = "Light"
Embed_Color = "#FF69FF"

Store_Page_Name = "module_template.html" # NO capitals! Underscores only! CANNOT HAVE "-files" AT THE END!
Folder_Name = "module_template-files" # NO capitals! Underscores only! Must have "-files" at the end!
Embed_FileName = "embed-banner.png" # Notice: GIFs work!
Store_Embed_FileName = "embed-banner.png" # I would still suggest against it due to AuraCloud-E2A's limited space.

Long_Description = '<p>Long descriptions are actually quite the doozy, they require actual HTML code to be set inside this little variable. \n \
While quite impractical looking, it lets you entirely skip the manual process of opening your Store Page HTML ENTIRELY!</p> \n \
<p class="SNDL-ParenthesizedText">This has limitations though... Of course...</p> \n \
<p>You obviously need HTML and SNDL knowledge if you wanna make this look as nice as possible.</p> \n \
<p>But of course since this is just a python variable inserted into HTML code that means that yes, you can:</p> \n \
<div class="SNDL-DashList"> \n \
    <p>Create certain parts of your long description to have parts of your module/plugin info update itself when you rebuild your Store page! For example this is version ' + Version + ' of FlashCFG that built this page!</p> \n \
    <p>And you can probably do a lot more but since I ran out of ideas, well you go figure it out yourself.</p> \n \
</div>'

# NOT recommended to modify, do this only if you know what you're doing! 
StoreTemplate = "flashcord/store/templates/default/default-store_template.html"
EmbedTemplate = "flashcord/store/templates/default/default-embed_template.html"

# Don't touch this, it will get overwritten anyways but still. Don't touch just in case.
HTMLFile = ""

# Don't touch this either. This will cause problems if your store page is for a Flashcord Module!
UserFolderName = GitHub_Profile.lower()

def GetEmbedCode():
    HTMLCode = ''
    API_Folders = []
    def CallAPI():
        if isRepluggedPlugin == True:
            API_Request = "GET/" + "PLUGINS/" + GitHub_Profile.upper()
        elif isFlashcordCompetitor == True:
            API_Request = "GET/" + "THEMES/" + GitHub_Profile.upper()
        else:
            API_Request = "GET/" + "MODULES/" + GitHub_Profile.upper()
        RequestResults = api.FlashClient_API_Request(API_Request)
        return RequestResults
    API_Folders = CallAPI()
    #print("TYPE:",type(API_Folders))
    #print("DATA:",API_Folders)
    if API_Folders != None:
        API_Folders = API_Folders.replace("[","").replace("]","").replace('"','').split(",")
        try:
            API_Folders.remove(Folder_Name)
        except:
            DoNothing = ""
        for cycle in range (len(API_Folders)):
            API_Folders[cycle] = API_Folders[cycle] + "-files"
            HTMLCode = HTMLCode + '<iframe class="Flashcord-Module_Embed" src="' + API_Folders[cycle] + '/embed.html"></iframe>\n'
    else:
        HTMLCode = HTMLCode + '<iframe class="Flashcord-Module_Embed" src="' + Folder_Name + '/embed.html"></iframe>\n'
    return HTMLCode

# This code is disgusting but it works, will optimize when I feel like it.
# NOTICE: this has ZERO error handling (or very little)! This is fucking horrible but I don't know yet how to do those and at the time of writing it's fucking 23h28
def GetHTMLFile(FileConcerned):
    if FileConcerned == "Store Page":
        if isRepluggedPlugin == True:
            File = "flashcord/store/plugins/" + GitHub_Profile.lower() + "/" + Store_Page_Name
        else:
            File = "flashcord/store/modules/" + GitHub_Profile.lower() + "/" + Store_Page_Name
    elif FileConcerned == "Embed":
        if isRepluggedPlugin == True:
            File = "flashcord/store/plugins/" + GitHub_Profile.lower() + "/" + Folder_Name + "/embed.html"
        else:
            File = "flashcord/store/modules/" + GitHub_Profile.lower() + "/" + Folder_Name + "/embed.html"
    else:
        print('[FlashCFG // GetHTMLFile] ERROR: Sirius A was here and pissed on the moon. (What the fuck is a "', FileConcerned, '"?!)')
        return "FUCK"
    return File

def FileBackup(FileToBackup):
    print("[FlashCFG // Backup] The", FileToBackup, "will now be backed up...")
    HTMLFile = GetHTMLFile(FileToBackup)
    HTMLFile_Backup = HTMLFile.replace(".html",".bak-html")
    try:
        with open(HTMLFile, 'r', encoding='utf-8') as HTMLFile_File:
            with open(HTMLFile_Backup, 'w', encoding='utf-8') as HTMLFile_Backup_File:
                HTMLFile_Backup_File.write((HTMLFile_File.read()))
        print("[FlashCFG // Backup] ", HTMLFile_Backup, "has been created and is now backed up.")
    except:
        print("[FlashCFG // Backup] ", HTMLFile_Backup, "doesn't exist! Creating empty file instead...")
        with open(HTMLFile, 'w', encoding='utf-8') as EditHTML_File:
            EditHTML_File.write("")

def HTMLConfigurator(Step):
    # We're doing this the MarkSNDL way, I can't fucking figure out how to do this the objectively better way
    # This is surprisingly way better than the current version of MarkSNDL though LMFAO
    HTMLArray = []
    if Step == 0:
        print("[FlashCFG // HTML-CFG] Now building the Store Page...")
        HTMLFile = GetHTMLFile("Store Page")
        StepFile = "// Store Page"
    elif Step == 1:
        print("[FlashCFG // HTML-CFG] Now building the Embed...")
        HTMLFile = GetHTMLFile("Embed")
        StepFile = "// Embed"
    else:
        print("[FlashCFG // HTML-CFG] ERROR: Sirius A was here and replaced Sirius B's Yae wallpaper with a Kirara one.", '(What the fuck is Step "', Step, '"?!)')
        return "FUCK"

    if AllowAPI == True:
        print('[FlashCFG // HTML-CFG] Connecting to SGN servers to fill the "More by" section...')
        MoreByCode = GetEmbedCode() # NOTICE: Will phone to the SGN servers!
        print(f'[FlashCFG // HTML-CFG] The "More by" section will have:\n{MoreByCode}')
    else:
        MoreByCode = '<iframe class="Flashcord-Module_Embed" src="' + Folder_Name + '/embed.html"></iframe>\n'
    

    with open(StoreTemplate, 'r', encoding='utf-8') as StoreTemplate_File:
        with open(EmbedTemplate, 'r', encoding='utf-8') as EmbedTemplate_File:
            with open(HTMLFile, 'w', encoding='utf-8') as EditHTML_File:
                EditHTML_File.write("")
            with open(HTMLFile, 'a', encoding='utf-8') as EditHTML_File:
                if Step == 0:
                    HTMLArray = StoreTemplate_File.readlines()
                elif Step == 1:
                    HTMLArray = EmbedTemplate_File.readlines()
                else:
                    print("[FlashCFG // HTML-CFG] WARNING: Sirius A was here and caused another Big Bang", '(What the fuck is Step "', Step, '"?!)')
                    print("[FlashCFG // HTML-CFG] Also how in the LIVING FUCK DID YOU TRIGGER THIS ERROR without triggering the previous one?")
                    return "FUCK"
                for line in range (len(HTMLArray)):
                    # print('[FlashCGG] Processing Line"', line, '" which is "', HTMLArray[line], '".')
                    HTMLArray[line] = HTMLArray[line].replace("[NAME]", Name)
                    HTMLArray[line] = HTMLArray[line].replace("[SHORT_DESC]", Short_Description)
                    HTMLArray[line] = HTMLArray[line].replace("[LONG_DESC]", Long_Description)
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
                    HTMLArray[line] = HTMLArray[line].replace("[STORE_USER_FOLDER]", UserFolderName)
                    HTMLArray[line] = HTMLArray[line].replace("[FLASHSTORE_API-EMBEDS]", MoreByCode)
                    EditHTML_File.write(HTMLArray[line])
                    ProcessingProgress = ((line+1)/len(HTMLArray))*100
                    print('[FlashCFG // HTML-CFG] Processed Line', line+1, '/', len(HTMLArray), '(', ProcessingProgress, '%).', StepFile)
                    # print('[FlashCGG] Processed Line is now "', HTMLArray[line], '".')

def FlashcordStoreConfig():
    print("[FlashCFG] Script initiated.")
    FileBackup("Store Page")
    HTMLConfigurator(0)
    FileBackup("Embed")
    HTMLConfigurator(1)
    print("[FlashCFG] Script complete.")
    return

FlashcordStoreConfig()