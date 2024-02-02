import json
import time

def ManifestHooker():
    with open("manifest.json", "r", encoding="utf8") as Manifest:
        Manifest_JSON = json.load(Manifest)
    # Now's the time to copy paste code from the closed source "Flashplug" script MUHAHAHA
    Addon_Name = Manifest_JSON["name"]
    Addon_Description = Manifest_JSON["description"]
    Addon_Version = Manifest_JSON["version"]
    Addon_AuthorKey = Manifest_JSON["author"]
    try:
        Addon_Author = Addon_AuthorKey["github"]
        Addon_Contributors = "None"
    except:
        Addon_Contributors = []
        for subcycle in range (len(Addon_AuthorKey)):
            if subcycle == 1:
                Addon_AuthorSubKey = Addon_AuthorKey[subcycle]
                Addon_Author = Addon_AuthorSubKey["name"]
            else:
                Addon_AuthorSubKey = Addon_AuthorKey[subcycle]
                Addon_Contributors.append(Addon_AuthorSubKey["name"])
    try:
        Addon_ImageKey = Manifest_JSON["image"]
        if Addon_ImageKey[0] == "h": Addon_Image = Manifest_JSON["image"]
        else: Addon_Image = Addon_ImageKey[0]
    except: Addon_Image = "https://sirio-network.com/sbin/This is fine.png"
    try: Addon_GitHubRepo = Manifest_JSON["source"]
    except: Addon_GitHubRepo = "https://sirio-network.com/404"
    Addon_License = Manifest_JSON["license"]
    isFlashcordCompetitor = False; isRepluggedPlugin = False
    if Manifest_JSON["type"] == "replugged-theme": isFlashcordCompetitor = True
    else: isRepluggedPlugin = True
    Addon_Contributors = str(Addon_Contributors)
    Addon_Contributors = Addon_Contributors.replace("[","").replace("]","").replace("'","")


    # Convert to Dictionary and then dump to FlashCFG.json
    FlashCFG_JSON = {}
    FlashCFG_JSON["name"] = Addon_Name
    FlashCFG_JSON["long_description"] = "<p>MAKE SURE TO REPLACE THIS AND ADD A LONG DESCRIPTION! Or yknow, copy paste the short description if you're that lazy.</p>"
    FlashCFG_JSON["short_description"] = Addon_Description
    FlashCFG_JSON["version"] = Addon_Version
    FlashCFG_JSON["author"] = Addon_Author
    FlashCFG_JSON["contributors"] = Addon_Contributors
    FlashCFG_JSON["github_repo"] = Addon_GitHubRepo
    FlashCFG_JSON["img_store"] = Addon_Image
    FlashCFG_JSON["img_embed"] = Addon_Image
    FlashCFG_JSON["license"] = Addon_License
    CTime = time.localtime()
    FlashCFG_JSON["license_year"] = str(CTime.tm_year)

    FlashCFG_JSON["is_rpplugin"] = isRepluggedPlugin
    FlashCFG_JSON["is_rptheme"] = isFlashcordCompetitor
    FlashCFG_JSON["images_are_full_links"] = True

    FlashCFG_JSON["internal_name"] = "change_this"
    FlashCFG_JSON["discord_link"] = "https://discord.com/CHANGE-THIS"
    FlashCFG_JSON["sndl_theme"] = "Light"
    FlashCFG_JSON["embed_color"] = "#00AAFF"

    with open("FlashCFG_ManifestHooker.json", "w", encoding="utf-8") as FlashCFG_ManifestHooker:
        FlashCFG_ManifestHooker.write(json.dumps(FlashCFG_JSON, indent = 1))
    
ManifestHooker()