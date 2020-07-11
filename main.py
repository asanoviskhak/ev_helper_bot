import sys
import time
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

print("[System] Bot has started.")

user = [line.rstrip('\n') for line in open('C:/Users/asano/Desktop/c++/.vscode/user.txt','rt')]

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "pythonbot-b0f0d",
  "private_key_id": "79ff476dba5604a57dc63c70008a183c1d288643",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDw9VPAWJKCtc82\nyHa90m4J94oTYX3x4tASq0ghPA8sqt7G4T4YZ0XPVqcDNhwagYPfqG9dlp0kvrst\ndwWIeFfezPFfeeJQw3pw8axFn/EmBniRz8goNiNtkenwvrUcJTzRqSCdxPBDzTeC\n3ibPu2oi9k+BU5ryKNC+LajRVwAGN6iTwjsA0N3RtIVIiCK7hajGx884Q6SE5gI3\nYgnd47k3DjZiJ4eHVZUESDgObdoeGSWNdRC/t2OkWFOiRf8qubVe68B/AOkl/k8W\nVds/k5t5LENPKvaqmeiKXU7Rvt0j0HUVlcJVFHlPCvhR+geFzXeAxBje2udUqka3\n2oRmAMmTAgMBAAECggEAD5kqB0kUju6bD+ZRPX+KTQ3fu9pzTz3KD3NUE4aySsdy\n7Xf2T5kb3Uy0OhJ+Jj8dHNToBKxz1sWcE1jhnFCCC7PDqlUXD/hfjEEw0D8G2tnP\nY00KnYPHrlekR8forH5CniXvLRdrIFCAF/IunAL7X3EHe41Aeg2nWbBV/ds+bqh6\nkCq6tAhGy3HoqpXkynKxGAwu6RmUyXeRjDmOygbk9BSBsMbwcJzuTUYdQhmE3gkx\nrvPIGMrwLLYvLWIoNq5o33CsRDqBSXWNhk6mSdpXUVYRGctXMLAc4oX2pP0Leyv7\nFP5REPfnO6Pg4WngE4if19xikBouD9ujBtMyFUyoeQKBgQD+smMzE0Mx8ESRAh9+\nTgiKsltm6u1OXp3u4DoWg6X9kp4hb+qWlPXHfKzXnq92Z4k8DnjjB9gDoLWKCDO8\nqhFqMjNIDs1ubXb0UbyMh0hc+NkpD7s/GIBEzADWhtszMyNgcsXlxv/zJEb97DsL\nlUHSixhoq9NzCZZ0rdJvIOHEuQKBgQDyMPHChORNbq9lmORw4Ax09R6ZZzlwi9C3\n9x2hnUzKGIH08q7LBNECWLn30jRrhioSdZLoza8ahYezZFjS2ZBGPFiqWM1hUa+S\nxglbPZx76yL0HsPN5Tubjx9sjxgiAdh7MDqh+eHyDjeXeso1VIULXExaVXB/2LAF\nqfQ8dlhyqwKBgHX0CWrq/dCP1EFPuWQWIXCSPzA/ll0YBo5NO7mXiHURxLf5i6vn\nGpgjTiyhaeMs+epdTXDe/hRYBhsBx2wVWvFShFtXt53vhgqKHAb80+9ys6eHiJEk\n+Kpjy/OOCtAAW97b6HiMm5Zv84y/LW0k15H5Jvm6sbdx9kLdCTq8ALLJAoGBAKJN\nWIah5hlaFqLAPj7CdraeWb415dFdcScHrMzUjFRW7ihHxgl5ldO7wAyqysRP6bvr\nHON0i2b7m0AF/Fx4vm3DHSwzTJduVXnHyxdhB5AnuIneYBuIBlUuKcHndyW7FOch\nH/nSaq97BZg3CnGIzYwac3SKE1Up0nRJO8qVCJr3AoGAGw5fQo/teo40QFq5FcRF\nTWlIhD64kOhRUvh0jxckRd85AT86+zs6HusK5sXu2/Whw8CEyBGplB9o+D0o0L6Y\nm6WdlrDBo6UaBY+VpU6Fi3WgSbnAmBLRUzCWhib5iJIMuZ7aZ8NCCD9zI9i/ZWMu\n0Q9FoW8OoubZCY85xtjt00Y=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-gv77s@pythonbot-b0f0d.iam.gserviceaccount.com",
  "client_id": "100750914705548586623",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-gv77s%40pythonbot-b0f0d.iam.gserviceaccount.com"
})

import telebot
import random
import json
import time
from itertools import permutations
from pprint import pprint

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythonbot-b0f0d.firebaseio.com'
})

API_TOKEN = '1343576972:AAHmGX4Da7GJQHqSLppkCNrTHBjDI41PbyQ'
bot = telebot.TeleBot(API_TOKEN)



pref = db.reference('EV')
dref = db.reference('DUTY')
# people_ref.set({
#     'user1':'asanoviskhak',
#     'user2':'hello_world'
# })


livingNow = ["Administrator"]

# @bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
# def on_user_joins(m):
# 	cid = m.chat.id
# 	inviter = m.from_user.first_name
# 	if m.content_type == 'new_chat_participant':
# 		if m.new_chat_participant.id == bot.get_me().id:
# 			chatid = m.chat.id
# 			if str(cid) not in user:
# 				user.append(str(cid))
# 				with open('user.txt', 'a') as f:
# 					f.write(str(cid)+"\n")
# 			bot.send_message(cid, "WOAAH! That was a very fast transport! 😨\nHi! My Name is Logging Bot clone! \n" + str(inviter) + " has invited me into this group!\n\nIf you want to Setup me type /setup into the Chat.\nI will try to bridge all your messages to another group! 😉\nIf you want to see all the cute guys behind the Bot type /credits 😇")
# 			print ("New group received.")
# 			userwhogotadded = m.new_chat_participant.first_name
# 			username = m.new_chat_participant.username
# 			groupname = m.chat.title
# 			groupid = str(m.chat.id)
# 			bot.send_message(m.chat_id, "# DEBUG # " + "Bot got invited to the group " + str(groupname) + '(' + groupid + ')' , parse_mode="HTML")


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")



@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_members[0].username
    pref.child('ev{}'.format(str(message.chat.id))).push(user_name)
    bot.send_message(message.chat.id, "Welcome to Ev , @{0}!".format(user_name))
# need to do this
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

@bot.message_handler(commands=['cleaning'])
def cleaningDuty(message):
    all_people = pref.child('ev{}'.format(str(message.chat.id))).get()
    all_duty = dref.child('duty{}'.format(str(message.chat.id)))
    all_duty.push(1)
    d=[]
    c=0
    for a in all_people.items():
        d.append(str(a[1]))
        c+=1
    s = len(all_duty.get())%c     
    perm = shift(d,s)
    k = 0
    rooms = ['Trash & Balcony(1,2): ',
            'Kitchen: ', 
            'Salon & Entrance: ', 
            'Big Toilet: ',
            'Small Toilet: ',
            'Groceries: ']
    duty = ""
    if (c==5):
        duty += rooms[0] + "@"+perm[0] + "\n"
        duty += rooms[1] + "@"+perm[1] + "\n"
        duty += rooms[2] + "@"+perm[2] + "\n"
        duty += rooms[3] + "@"+perm[3] + "\n"
        duty += rooms[4] + "@"+perm[4] + "\n"
    if (c==6):
        duty += rooms[0] + "@"+perm[0] + " & @" + perm[4] + "\n"
        duty += rooms[1] + "@"+perm[1] + " & @" + perm[5] + "\n"
        duty += rooms[2] + "@"+perm[2] + "\n"
        duty += rooms[3] + "@"+perm[3] + "\n"
        duty += rooms[4] + "@"+perm[4] + "\n"
    if (c==7):
        duty += rooms[0] + "@"+perm[0] + " & @" + perm[5] + "\n"
        duty += rooms[1] + "@"+perm[1] + " & @" + perm[6] + "\n"
        duty += rooms[2] + "@"+perm[2] + "\n"
        duty += rooms[3] + "@"+perm[3] + "\n"
        duty += rooms[4] + "@"+perm[4] + "\n"
    if (c==8):
        duty += rooms[0] + "@"+perm[0] + " & @" + perm[5] + "\n"
        duty += rooms[1] + "@"+perm[1] + " & @" + perm[6] + " & @" + perm[7] + "\n"
        duty += rooms[2] + "@"+perm[2] + "\n"
        duty += rooms[3] + "@"+perm[3] + "\n"
        duty += rooms[4] + "@"+perm[4] + "\n"
    if (c>=9):
        duty += rooms[0] + "@"+perm[0] + " & @" + perm[5] + "\n"
        duty += rooms[1] + "@"+perm[1] + " & @" + perm[6] + " & @" + perm[7] + "\n"
        duty += rooms[2] + "@"+perm[2] + "\n"
        duty += rooms[3] + "@"+perm[3] + "\n"
        duty += rooms[4] + "@"+perm[4] + "\n"
        duty += rooms[5] + "@"+perm[8] + "\n"

    bot.send_message(message.chat.id, "{} \n Deadline: Saturday(22:30) ".format(duty))
        
    

@bot.message_handler(commands=['help'])
def help(m):
	cid = m.chat.id
	bot.send_message(cid, "*Bot Help Page*\n\n/setup - Start setup the Bot in this group\n/setloggingid <Group-ID> - Sets a group ID to log all messages and send it into the group\n/id - Gets the current group-id\n /nobroadcasts - Opts you from Broadcasts out.\nAlso if you like to support our work please rate the bot at https://telegram.me/storebot?start=IchLoggeBot", parse_mode="Markdown")
		
@bot.message_handler(commands=['housingfee'])
def housingFee(m):
    cid = m.chat.id
    nid = bot.get_chat_members_count(cid)
    bot.send_message(cid, "Answer these questions, and I will calcualate the fee for house per each member:")
    bot.send_message(cid, "What is the rent price?: ")

    

# @bot.message_handler(commands=['setup'])
# def welcome(m):
# 	cid = m.chat.id
# 	bot.send_message(cid, "*Welcome to this group!*\n *1)* Create a *new* Group and add the Bot into the Group.\n *2)* Type /id and copy the group-ID.\n *3)* Finish the setup by type /setloggingid <ID of other Group> in the group where the messages shall get noticed. Make sure you set the id WITH the minus ( - ) sign.\n* 4)* You are *finished!* _The Bot will start collecting and sending messages into the Logging Group!_\n", parse_mode="Markdown")


bot.polling(none_stop=True, interval=0, timeout=3)


