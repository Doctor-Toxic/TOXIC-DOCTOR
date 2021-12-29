Import os
Os.system(“pip install Telethon==1.24.0”)
From telethon.sync import TelegramClient
From telethon.sessions import StringSession
Print(“”)
Print(“””Wᴇʟᴄᴏᴍᴇ ᴛᴏ MoneyHeist Usᴇʀʙᴏᴛ Sᴛʀɪɴɢ Gᴇɴᴇʀᴀᴛᴏʀ ”””)
Print(“””Kɪɴᴅʟʏ ᴇɴᴇᴛᴇʀ ʏᴏᴜʀ ᴅᴇᴛᴀɪʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ! “””)

API_KEY = input(“API_KEY: “)
API_HASH = input(“API_HASH: “)

While True:
 Try:
  With TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   Print(
       “String Sent To Your Saved Message, Store It To A Safe Place!! “
   )
   Print(“”)
   Session = client.session.save()
   Client.send_message(
       “me”,
       F”Here Is Your String Session For Using MoneyHeist Userbot\n(**Tap to copy it**)👇 \n\n `{session}` \n\n And Visit @MM_USERBOT For Any Help !”
   )

   Print(
       “Thanks for Choosing MoneyHeist Have A Good Time….Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work”
   )
 Except Exception as e:
  Print(str€)
  Print(
      “\nWrong phone number \n make sure its with correct country code. Example : +919961998999 ! Kindly Retry”
  )
  Print(“”)
  Continue
 Break
