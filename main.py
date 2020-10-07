import scratchapi2
import webbrowser
import sys

appTypeFile = open("CSSE_setup.txt", "r") #config file
appType = eval(appTypeFile.read())
prefUsername = appType["username"]

print("loading...")

f = open(appType["output"],'wb')
message = "<html><head><title>Custom Scratch Search Engine</title><style>body{background-color: AliceBlue;}p.title{font-family:Verdana, Geneva, sans-serif;font-size: large;color:darkBlue;}p.desc{font-family:Verdana, Geneva, sans-serif;font-size: small;color:dodgerBlue;}</style></head><body>"

if(eval(appType["hideUsername&Messages"])):
    print("showUsername&Messages off");
else:
    message += "<p class='desc'>Username: " + scratchapi2.User(prefUsername).username + ". You have " + str(scratchapi2.User(prefUsername).unread_messages()) + " unread messages.</p><hr>"
print("loading some more...")
searchlist = list(scratchapi2.Misc().search_projects(input("what is the search term? ").encode(encoding = "ascii", errors = "replace"), 5))
print("loading even more...")

for i in searchlist:
    message += ("\n <p class='title'>" + i.title + " by " + i.author.username + " at " + i.url + " <br></p><a href='" + i.url + "'><img src='" + i.image + "'><br></a><p class='desc'>" + i.instructions[:800] + "<br><br>" + i.description[:800] + "<br><br>" + str(i.views) + " views, " + str(i.loves) + " loves, " + str(i.favorites) + " faves." + "<br><br>Created on " + i.created[:10] + "</p><hr>")
message += "</body></html>"

f.write(message.encode(sys.stdout.encoding, errors='replace'))
f.close()

print("almost done...")

webbrowser.open_new_tab('scratch.html')