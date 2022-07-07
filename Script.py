class script(object):
    START_TXT = """<b>Hey {} !</b>

<b><i>I'm An Advanced Group Managing bot Created For @MovieJunctionGrp 🔥</b></i>"""
    HELP_TXT = """Hey {}
<b>Here Is A Brief Details About Some of the Features Of Mine...</b>"""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: @MasterOfTG
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: N/A
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: N/A
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0.0 [ Stable ]"""
    SOURCE_TXT = """<b>✯ Kanged And Modified By @MasterOfTG 🙂</b>

<b>✯ Special Courtesy To :
   ● Team Eva Maria
   ● Team TrojanzHex
   ● Team CrazyBotsz
   ● Team InFoTel </b>

<b>✯ Bot Managed By :
   ● @DoubleAgent2
   ● @Mr_WarLord
   ● @Jeffrey_morgan2</b>

- <a href=https://t.me/MovieJunction>Team Movie Junction ⚡</a>"""
    MANUELFILTER_TXT = """<b>Feature: Filter</b>

- <b>Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message.</b>

<b>NOTE:</b>
<b>1. Diana can only used at @MovieJunctionGrp 😊.
2. only admins can add filters in diana.
3. So Ultimately You're Just Wasting Your Time 🤐.</b>

<b>Commands and Usage:</b>
<b>• /filter </b>- <code>add a filter in chat</code>
<b>• /filters </b>- <code>list all the filters of a chat</code>
<b>• /del </b>- <code>delete a specific filter in chat</code>
<b>• /delall </b>- <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Feature: <b>Filter Buttons</b>

- <b>Diana Bot Supports both url and alert inline buttons.</b>

<b>NOTE:</b>
<b>1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Diana supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format</b>

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MovieJunction)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Feature: <b>Auto Filter</b>

<b>NOTE:</b>
1.<code> Make Me The Admin Of Your Channel and And Add The Channel In Auth List.</code>
2.<code> That's It,Now I Will Index The Channel Files In</code> @MovieJunctionGrp ⚡.
3.<code> And Obviously Won't Work Anywhere Else 🙃</code>"""
    CONNECTION_TXT = """<b>Feature: Connections</b>

<b>- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.</b>

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
<b>• /connect  </b>- <code>connect a particular chat to your PM</code>
<b>• /disconnect</b> - <code>disconnect from a chat</code>
<b>• /connections </b>- <code>list all your connections</code>"""
    EXTRAMOD_TXT = """<b>Feature: Extra Modules</b>

<b>NOTE:</b>
these are the extra features of diana

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
• <code>There Are A Bunch Of Extra Modules Kanged From @BanhammerMarie_bot And Still Not Added In This Essay 😪(മടി 🙃),Gud Luck Finding Them Yourself 😅</code>"""
    ADMIN_TXT = """Feature: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /block  - <code>to block a user from using diana.</code>
• /unblock  - <code>to unblock a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>2{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""


## Pattishow Starts Here

    RESTRICTION_TEXT = """<b>Feature: Restrictions</b>

<b>There Are 3 Types Of Restriction Modules Available In Diana Bot To Restrict Users In Groups/Super Groups.

Ban,Mute and Warn.

Inorder To Use This Modules Diana Must Be An Admin Of The Chat With Ban Users Permission.</b>

Click On The Below Buttons To Know More.."""

    BANRES_TEXT = """<b>Commands and Usage:</b>

★ Ban Commands :
• /ban - <code>Ban A User From Group.[If You Have Any Reasons,Type That After A Space.]</code>
• /kick - <code>Kick Out A User.</code>
• /tban - <code>Ban A User For Some Period Of Time (1m/1h/1d/1w/).</code>
• /unban - <code>Un Ban A User.</code>

NOTE : <code>These Commands Can Be Used By Replying or Mentioning A User,And Most Importantly Any Of These Commands Can't Be Used Against An Admin Of The Group.</code>"""

    MUTERES_TEXT = """<b>Commands and Usage:</b>

★ Mute Commands :
• /mute - <code>Mute A User (By Mentioning Or Replying).</code>
• /tmute - <code>Mute A User For A Period Of Time (1m/1h/1d/1w)</code>
• /unmute  - <code>Un Mute A User.</code>

NOTE : <code>These Commands Can Be Used By Replying or Mentioning A User,And Most Importantly Any Of These Commands Can't Be Used Against An Admin Of The Group.</code>"""

    WARNRES_TEXT = """<b>Commands and Usage:</b>

★ Warn Commands :
• /warn  -  <code>Warn A User By Mentioning Or Replying [eg: /warn @mention reason.]</code>
• /resetwarn - <code>Reset Warns Of A User.</code>
• /warns - <code>Get A User's Number, And Reason Of Warnings,Can Be Used By Mentioning Or Replying</code>
• /addwarn  - <code>Set Automated Warn Filter For Some Words.[eg: /setwarn ""wtf"" No Abusive Words Allowed Here 😠.]</code>
• /nowarn - <code>Stop A Warning Filter.</code>
• /warnlist - <code>List Of All Current Warn Filters.</code>
• /warnlimit  - <code>Set A Limit For Warn,After Exceeding This Limit User Will Be Banned From Chat.</code>
• /strongwarn True/False - <code>If True User Will Be Banned After Warning,Else Will be just kicked.</code>

NOTE : <code>These Commands Can Be Used By Replying or Mentioning A User,And Most Importantly Any Of These Commands Can't Be Used Against An Admin Of The Group.</code>"""
    GREETINGS_TEXT = """<b>Feature: Greetings</b>

<b>NOTE:
This Module Only Works In Groups</b>

<b>Commands and Usage:</b>

<b>● Welcome Commands :</b>
• /welcome on/off - <code>Enable/Disable Welcome Message.</code>
• /setwelcome - <code>Set A Custom Message.</code>
• /cleanwelcome on/off - <code>If On Then Deletes Previous Welcome Messages When A New Member Joins.</code>
• /resetwelcome - <code>Reset The Welcome Message.</code>

<b>● Goodbye Commands :</b>
• /goodbye - <code>Same Usage And Args as Welcome Commands [Replace welcome with goodbye in above mentioned commands]</code>"""

## Pattishow Ends Here
