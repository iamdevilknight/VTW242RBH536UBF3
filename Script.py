class script(object):
    START_TXT = """<b>Hey {} !</b>

<b><i>I'm An Advanced Group Managing bot Created For @MovieJunctionGrp π₯</b></i>"""
    HELP_TXT = """Hey {}
<b>Here Is A Brief Details About Some of the Features Of Mine...</b>"""
    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄: {}
β― π²ππ΄π°ππΎπ: @MasterOfTG
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: N/A
β― π±πΎπ ππ΄πππ΄π: N/A
β― π±ππΈπ»π³ πππ°πππ: v2.0.0 [ Stable ]"""
    SOURCE_TXT = """<b>β― Kanged And Modified By @MasterOfTG π</b>

<b>β― Special Courtesy To :
   β Team Eva Maria
   β Team TrojanzHex
   β Team CrazyBotsz
   β Team InFoTel </b>

<b>β― Bot Managed By :
   β @DoubleAgent2
   β @Mr_WarLord
   β @Jeffrey_morgan2</b>

- <a href=https://t.me/MovieJunction>Team Movie Junction β‘</a>"""
    MANUELFILTER_TXT = """<b>Feature: Filter</b>

- <b>Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message.</b>

<b>NOTE:</b>
<b>1. Diana can only used at @MovieJunctionGrp π.
2. only admins can add filters in diana.
3. So Ultimately You're Just Wasting Your Time π€.</b>

<b>Commands and Usage:</b>
<b>β’ /filter </b>- <code>add a filter in chat</code>
<b>β’ /filters </b>- <code>list all the filters of a chat</code>
<b>β’ /del </b>- <code>delete a specific filter in chat</code>
<b>β’ /delall </b>- <code>delete the whole filters in a chat (chat owner only)</code>"""
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
2.<code> That's It,Now I Will Index The Channel Files In</code> @MovieJunctionGrp β‘.
3.<code> And Obviously Won't Work Anywhere Else π</code>"""
    CONNECTION_TXT = """<b>Feature: Connections</b>

<b>- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.</b>

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
<b>β’ /connect  </b>- <code>connect a particular chat to your PM</code>
<b>β’ /disconnect</b> - <code>disconnect from a chat</code>
<b>β’ /connections </b>- <code>list all your connections</code>"""
    EXTRAMOD_TXT = """<b>Feature: Extra Modules</b>

<b>NOTE:</b>
these are the extra features of diana

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>
β’ <code>There Are A Bunch Of Extra Modules Kanged From @BanhammerMarie_bot And Still Not Added In This Essay πͺ(ΰ΄?ΰ΄ΰ΄Ώ π),Gud Luck Finding Them Yourself π</code>"""
    ADMIN_TXT = """Feature: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /block  - <code>to block a user from using diana.</code>
β’ /unblock  - <code>to unblock a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>2{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
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

β Ban Commands :
β’ /ban - <code>Ban A User From Group.[If You Have Any Reasons,Type That After A Space.]</code>
β’ /kick - <code>Kick Out A User.</code>
β’ /tban - <code>Ban A User For Some Period Of Time (1m/1h/1d/1w/).</code>
β’ /unban - <code>Un Ban A User.</code>

NOTE : <code>These Commands Can Be Used By Replying or Mentioning A User,And Most Importantly Any Of These Commands Can't Be Used Against An Admin Of The Group.</code>"""

    MUTERES_TEXT = """<b>Commands and Usage:</b>

β Mute Commands :
β’ /mute - <code>Mute A User (By Mentioning Or Replying).</code>
β’ /tmute - <code>Mute A User For A Period Of Time (1m/1h/1d/1w)</code>
β’ /unmute  - <code>Un Mute A User.</code>

NOTE : <code>These Commands Can Be Used By Replying or Mentioning A User,And Most Importantly Any Of These Commands Can't Be Used Against An Admin Of The Group.</code>"""

    WARNRES_TEXT = """<b>Commands and Usage:</b>

β Warn Commands :
β’ /warn  -  <code>Warn A User By Mentioning Or Replying [eg: /warn @mention reason.]</code>
β’ /resetwarn - <code>Reset Warns Of A User.</code>
β’ /warns - <code>Get A User's Number, And Reason Of Warnings,Can Be Used By Mentioning Or Replying</code>
β’ /addwarn  - <code>Set Automated Warn Filter For Some Words.[eg: /setwarn ""wtf"" No Abusive Words Allowed Here π .]</code>
β’ /nowarn - <code>Stop A Warning Filter.</code>
β’ /warnlist - <code>List Of All Current Warn Filters.</code>
β’ /warnlimit  - <code>Set A Limit For Warn,After Exceeding This Limit User Will Be Banned From Chat.</code>
β’ /strongwarn True/False - <code>If True User Will Be Banned After Warning,Else Will be just kicked.</code>

NOTE : <code>These Commands Can Be Used By Replying or Mentioning A User,And Most Importantly Any Of These Commands Can't Be Used Against An Admin Of The Group.</code>"""
    GREETINGS_TEXT = """<b>Feature: Greetings</b>

<b>NOTE:
This Module Only Works In Groups</b>

<b>Commands and Usage:</b>

<b>β Welcome Commands :</b>
β’ /welcome on/off - <code>Enable/Disable Welcome Message.</code>
β’ /setwelcome - <code>Set A Custom Message.</code>
β’ /cleanwelcome on/off - <code>If On Then Deletes Previous Welcome Messages When A New Member Joins.</code>
β’ /resetwelcome - <code>Reset The Welcome Message.</code>

<b>β Goodbye Commands :</b>
β’ /goodbye - <code>Same Usage And Args as Welcome Commands [Replace welcome with goodbye in above mentioned commands]</code>"""

## Pattishow Ends Here
