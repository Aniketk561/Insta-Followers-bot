import pyautogui
import webbrowser
import subprocess
import time
import os
import csv
import logging
import string
import random
from telegram.ext import Updater, CommandHandler, run_async
from telegram import ChatAction
from os import execl
from sys import executable

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
BOT_TOKEN = '1482617956:AAHK_4qSCMk56TT99Bx4ZxoRUY7IMg1T6vQ'
print("BOT RUNNING!")

updater = Updater(token = BOT_TOKEN, use_context=True)
dp = updater.dispatcher
firstName = ["Alan", "Murat", "Azad", "Necati", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan",
                 "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                 "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
                 "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel",
                 "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam",
                 "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil",
                 "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed",
                 "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian",
                 "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay",
                 "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert",
                 "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs",
                 "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf",
                 "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider",
                 "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen",
                 "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan",
                 "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer",
                 "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs",
                 "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet",
                 "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio",
                 "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep",
                 "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez",
                 "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis",
                 "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran",
                 "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved",
                 "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley",
                 "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal",
                 "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun",
                 "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan",
                 "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub",
                 "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise",
                 "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley",
                 "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz",
                 "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz",
                 "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay",
                 "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod",
                 "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue",
                 "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony",
                 "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly",
                 "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee",
                 "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan",
                 "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody",
                 "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan",
                 "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak",
                 "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan",
                 "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Melim"]

surName = ["Abak", "Demir", "Bala", "yilmaz", "Ediz",
               "yasar", "Ozbal", "Aydin", "kara",
               "Bakar", "Zengin", "Bilgin", "Kilic",
               "karabulut", "Abbas", "Hammoud", "Alan",
               "tilki", "Aslan", "Boz", "karaeski",
               "Deniz", "Temiz", "Alpaslan", "Demirci",
               "Erol", "Guneri", "yasin", "yelken",
               "Elmas", "Altin", "guller", "Bagci",
               "yucel", "korkmaz", "cetin","Dari",
               "Albayrak", "Tekin", "Yurtkulu", "Metin",
               "Suvari", "Kizilay", "Inan", "tasi", "Akdeniz",
               "Albagu", "alk", "Acu", "Altun", "Karagul",
               "Avkar", "Ayana", "Alagan", "Akar"]

@run_async
def restart(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="Restarting, Please wait!")
	execl(executable, executable, "chromium.py")

def status(update, context):
	pyautogui.screenshot('ss.png')
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
	context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
	os.remove('ss.png')

def check(update, context):
	a= str(pyautogui.position())
	print(a)
	context.bot.send_message(chat_id=update.message.chat_id, text="Values:" + a)


def instagram(update,context):
	#subprocess.Popen("C:\\Program Files (x86)\\Hotspot Shield\\bin\\hsscp.exe") 
	pyautogui.FAILSAFE = False
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	ignameStr = update.message.text.split()[-1]
	context.bot.send_message(chat_id=update.message.chat_id, text="Starting IG bot For: \n" + ignameStr)
	def followers():
		#pyautogui.press('launchapp1')
		#while True:
		#	var = pyautogui.locateOnScreen('startvpn.png')
		#	if var != None:
		#		pyautogui.click(var)
		#		break
		chars=string.ascii_lowercase + random.choice(['.', '_'])
		usernameStr = ''.join(random.choice(chars) for _ in range(8)) + random.choice(string.digits)
		passwordStr = 'idkpassword'
		fullnameStr = ''.join(random.choice(firstName) + ' ' + random.choice(surName))
		webbrowser.open('https://mail.tm/en')
		time.sleep(3)
		pyautogui.click(1883, 123)
		while True:
			var = pyautogui.locateOnScreen('generatemail.png')
			if var != None:
				pyautogui.click(var)
				break
		time.sleep(3)
		pyautogui.click(461, 124)
		time.sleep(1)
		webbrowser.open_new_tab('https://www.instagram.com/accounts/emailsignup/')
		time.sleep(5)
		pyautogui.press('tab', presses=2)
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press('tab')
		pyautogui.write(fullnameStr)
		pyautogui.press('tab')
		pyautogui.write(usernameStr)
		pyautogui.press('tab')
		pyautogui.write(passwordStr)
		pyautogui.press('enter')
		time.sleep(3)
		pyautogui.press('tab', presses=4)
		pyautogui.press('enter')
		pyautogui.press('pagedown')
		pyautogui.press('enter')
		pyautogui.press('tab')
		pyautogui.press('enter')
		pyautogui.hotkey('ctrl', 'shift', 'tab')
		while True:
			var = pyautogui.locateOnScreen('verifymail.png')
			if var != None:
				pyautogui.click(var)
				break
		
		time.sleep(3)
		pyautogui.doubleClick(1122, 746)
		pyautogui.hotkey('ctrl', 'c')
		pyautogui.hotkey('ctrl', 'shift', 'tab')
		pyautogui.press('tab', presses=2)
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press('tab')
		pyautogui.press('enter')
		time.sleep(15)
		webbrowser.open('https://www.instagram.com/'+ ignameStr)
		time.sleep(3)
		pyautogui.press('tab')
		pyautogui.press('enter')
		time.sleep(5)
		pyautogui.hotkey('ctrl', 'shift', 'tab')
		pyautogui.click(1517, 156)
		time.sleep(3)
		pyautogui.click(1382, 409)
		time.sleep(3)
		pyautogui.hotkey('alt', 'f4')
		#pyautogui.press('launchapp1')
		#time.sleep(3)
		#while True:
		#	var = pyautogui.locateOnScreen('stopvpn.png')
		#	if var != None:
		#		pyautogui.click(var)
		#		break
		with open('ID-list.csv', 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([usernameStr, passwordStr, fullnameStr])
			file.close()
		time.sleep(3)
		followers()
	followers()


def main():
	dp.add_handler(CommandHandler("ig", instagram))
	dp.add_handler(CommandHandler("restart", restart))
	dp.add_handler(CommandHandler("check", check))
	dp.add_handler(CommandHandler("status", status))
	updater.start_polling()

if __name__ == '__main__':
    main()