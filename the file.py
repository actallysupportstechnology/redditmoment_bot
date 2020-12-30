import praw, time, traceback #packages for the bot

reddit = praw.Reddit(user_agent="<user agent>",
                     client_id="<client id>",
                     client_secret="<client secret>",
                     username="<bot's username>",
                     password="<bot's password>") #API credentials

slurs = ["<slur1>:",
         "<slur2>",
         "<slur3>"] #slurs

rm_modlist = ["Merari01",
             "aadre",
             "Kevin2GO",
             "officer_panda159",
             "IDislikeBabyYoda",
             "hwhouston517",
             "EffectivePineapple2",
             "Legendariummc",
             "Elerizo",
             "x-SpookyReddit-x",
             "esoterix_luke",
             "Malachi_Noel3",
             "Tech-Support-420",
             "redditmoment_bot",
             "thePotatoRises",
             "Babar77",
             "PhlogistonAster",
             "Kick-All",
             "TheSebtacular",
             "CuriosityBoie",
             "DuplicateDestroyer",
             "savevideo",
             "repostsleuthbot",
             "haikusbot",
             "wordscounterbot"] #list of whitelisted mods

slurwarningmessage = """
**RULE 2: DON'T BE RUDE**

Your comment was removed because it contains a rude word

If you feel like this removal was a mistake, **Use this link to send us a mod mail message** [here](https://www.reddit.com/message/compose?to=%2Fr%2FRedditMoment&subject=About my removed comment&message=I'm w$
"""
#the warning message

while True:
    try:
        for comment in reddit.subreddit("redditmoment").stream.comments(skip_existing=True): 
            for slur in slurs:
                if slur in comment.body and comment.author.name not in rm_modlist:
                    comment.reply(slurwarningmessage.format(comment.permalink)).mod.distinguish() #replies to the comment with the slur
                    comment.mod.remove() #removes the comment with the slur
                    print('Replied to comment ' + comment.id + ' by u/' + comment.author.name) #prints the information in the console log
                    break
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('Shutting Down')
        quit()
               
