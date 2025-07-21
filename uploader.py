import os
import random
import json
from instagrapi import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
IG_USERNAME = os.getenv("INSTAGRAM_USERNAME")
IG_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Config
MEDIA_FOLDER = "media_folder"  # Folder path where your images/videos are stored
HISTORY_FILE = "posted_history.json"

# Initialize Instagram Client
cl = Client()
cl.login(IG_USERNAME, IG_PASSWORD)

# Load posted history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as file:
        posted_history = json.load(file)
else:
    posted_history = []

# === Offline Captions List ===
captions_list = ["Coffee bhi chahiye, wi-fi bhi aur pyaar bhi. Multitasking on point! #KrazyNotesy",
"Monday aaya, mood gaya! #KrazyNotesy",
"Aaj kal to weight sirf tension ka badh raha hai... #KrazyNotesy",
"Sorry yaar, kal se pakka gym! #KrazyNotesy",
"Timepass ho raha hai, life ka koi aim nahi. #KrazyNotesy",
"Duniya gol hai, toh main ghoom raha hoon! #KrazyNotesy",
"Zindagi na milegi dobara... par neend har din chahiye. #KrazyNotesy",
"Coffee bhi chahiye, wi-fi bhi aur pyaar bhi. Multitasking on point! #funny #hinglish #coffee #wifi #love #KrazyNotesy",
"Ab toh dosti bhi Wi-Fi jaisi ho gayi hai—jab signal kam toh game over! #funny #dosti #wifi #KrazyNotesy",
"Work from home: Pyjamas official dress hai yahaan. #funny #wfh #pyjamas #KrazyNotesy",
"Dil se engineer, dimaag se bhi nahi. #funny #engineer #students #KrazyNotesy",
"Status toh sab rakhte hai, hum toh mood rakhte hai. #funny #status #mood #KrazyNotesy",
"Raat bhar Netflix, din bhar regret. #funny #netflix #regrets #KrazyNotesy",
"Attendance ki kami se zyada neend ki kami mehsoos hoti hai. #funny #attendance #sleep #KrazyNotesy",
"Coding me bug hai, zindagi me thug hai. #funny #coding #life #KrazyNotesy",
"Na tu hero, na main zero, dono timepass ka saaman hai. #funny #friendship #timepass #KrazyNotesy",
"Swag ka level toh battery ke percentage se bhi kam hai. #funny #swag #battery #KrazyNotesy",
"Aaj soya nahi, kal uthunga nahi! #funny #sleep #lazy #KrazyNotesy",
"Breakfast ke bahane uthne wale hum. #funny #breakfast #foodie #KrazyNotesy",
"Family group = Good morning sticker ka museum. #funny #family #whatsapp #KrazyNotesy",
"Sardi mein nahaane ki soch hi particular hai. #funny #winter #bath #KrazyNotesy",
"DP to hai, but asli wala andaaz baaki hai. #funny #dp #profile #KrazyNotesy",
"Free time mein busy rehne ka natak! #funny #free #busy #KrazyNotesy",
"Padhai ka time kabhi nahi aata. #funny #study #student #KrazyNotesy",
"Majboori ka naam zindagi, boss ka naam majboori! #funny #work #boss #KrazyNotesy",
"Lagta hai arrival late, magar attitude on time. #funny #attitude #late #KrazyNotesy",
"Kitni bhi sleep le lo, neend ki talash khatam nahi hoti. #funny #sleep #tired #KrazyNotesy",
"Kya bolti public, humko farak nahi padta. #funny #public #carefree #KrazyNotesy",
"Kabutar ja ja ja, WhatsApp pe aa aa aa. #funny #whatsapp #fun #KrazyNotesy",
"Girlfriend nahi, meri toh life hi single hai. #funny #single #life #KrazyNotesy",
"Ye friendship bhi WhatsApp ke tick ke saath hoti hai. #funny #whatsapp #friendship #KrazyNotesy",
"Ghanti bajate ho ya mood bajate ho? #funny #mood #bell #KrazyNotesy",
"Bhoolne ka time nahi milta, sab kuch yaad hai. #funny #memory #sarcasm #KrazyNotesy",
"Assignment pending hai, par memes update ho rahe hain. #funny #assignment #memes #KrazyNotesy",
"College ki chuttiyon ka asli maza baap ke samne nahi hai. #funny #college #vacation #KrazyNotesy",
"Padhaku hone ka pressure, timepass hone ka pleasure. #funny #study #pleasure #KrazyNotesy",
"Recharge tu kar le, network toh kabhi bhi ja sakta hai. #funny #phone #network #KrazyNotesy",
"Humse miloge toh smile toh guaranteed hai. #funny #smile #guaranteed #KrazyNotesy",
"Crush ke reply ka intezaar, Olympics ka medal nahi hai. #funny #crush #wait #KrazyNotesy",
"Office ki kahani, ghar pe mummy ki pareshani! #funny #office #home #KrazyNotesy",
"Tan tana tan, tan tan tara… kaam ka hai bahana saara. #funny #kaam #excuse #KrazyNotesy",
"Dil ka dard hai, ice cream ke saath thoda kam hai. #funny #icecream #love #KrazyNotesy",
"Farzi smile, asli drama. #funny #smile #drama #KrazyNotesy",
"Filter laga le, reality aayegi fir bhi! #funny #filter #reality #KrazyNotesy",
"Bhai ka birthday hai, treat remote se bhej. #funny #birthday #treat #KrazyNotesy",
"Monday ki morning, neend ki warning! #funny #monday #morning #KrazyNotesy",
"Selfie expert, life ke moment me ignorant. #funny #selfie #moment #KrazyNotesy",
"Assignment aur girlfriend, dono attention chahti hain. #funny #assignment #girlfriend #KrazyNotesy",
"Engineer banna mushkil hai, samjhaana usse bhi mushkil! #funny #engineer #student #KrazyNotesy",
"Teacher: 'Ye tumne kiya?' Main: 'Bas aise hi ho gaya!' #funny #teacher #studentlife #KrazyNotesy",
"Girlfriend nahi, toh achha hai, pocket safe hai! #funny #single #money #KrazyNotesy",
"Ranveer Singh ki energy, meri neend ki urgency! #funny #celebrity #sleep #KrazyNotesy",
"Mask pehna hai, par smile visible nahi hai. #funny #mask #smile #KrazyNotesy",
"Chillana nahi hai, meme bhejna hai. #funny #memes #chill #KrazyNotesy",
"Note ban gaye electronic, feelings ab bhi emotional. #funny #digital #feelings #KrazyNotesy",
"Log kehte hain attitude hai, hum kehte hain gratitude hai! #funny #attitude #gratitude #KrazyNotesy",
"Zindagi ka shortcut chahiye, toh alarm snooze karlo. #funny #lazy #alarm #KrazyNotesy",
"Khaana khane se pehle photo zaruri hai! #funny #foodie #photo #KrazyNotesy",
"Lecture boring, par attendance mandatory. #funny #lecture #student #KrazyNotesy",
"Phone ki battery gayi, toh mood bhi gaya. #funny #phone #battery #KrazyNotesy",
"Koi na samjhe, toh Google se puch lo. #funny #google #solution #KrazyNotesy",
"Bas ek aur episode, fir so jaunga! #funny #netflix #binge #KrazyNotesy",
"Sunday aaya, Phir bhi homework yaad aaya. #funny #sunday #homework #KrazyNotesy",
"Sab kuch milta hai, bas shaanti nahi milti. #funny #peace #life #KrazyNotesy",
"Repeat mode pe zindagi chal rahi hai. #funny #routine #life #KrazyNotesy",
"Mummy ka phone, jail ka zone! #funny #mummy #phone #KrazyNotesy",
"Kaam se jyada kaam ki acting karo. #funny #work #drama #KrazyNotesy",
"Toh kya hua agar koi nahi milta, pizza to mil hi jata hai! #funny #pizza #single #KrazyNotesy",
"Exam ki dua chahiye, aur thoda luck bhi! #funny #exam #students #KrazyNotesy",
"Kal college jana hai... abhi soch ke thak gaya hoon. #funny #college #lazy #KrazyNotesy",
"Mask ka fashion chal raha hai, par asli chhupa toh dil hai. #funny #covid #mask #KrazyNotesy",
"Wi-fi slow ho toh patience bhi slow ho jata hai. #funny #wifi #relatable #KrazyNotesy",
"Maggi 2-minute mein ready, par meri zindagi abhi bhi loading hai. #funny #maggi #relatable #KrazyNotesy",
"Shararat toh bachpan se hi hai! #funny #nostalgia #childhood #KrazyNotesy",
"Pyaar ek dhoka hai, par pizza mein bhi maza hai. #funny #pizza #love #KrazyNotesy",
"Ghadi ki soiyaan chal rahi hain, par hum toh soye pade hain. #funny #sleep #lazy #KrazyNotesy",
"Netflix aur chill? Nahi, life aur bill! #funny #netflix #money #KrazyNotesy",
"Apne toh plans bante hi cancel hone ke liye hain. #funny #plans #relatable #KrazyNotesy",
"Sardi ho ya garmi, ghar se bahar nahi jana hai humne. #funny #homebody #KrazyNotesy",
"Selfie lele re, filter lagale re! #funny #selfie #filter #KrazyNotesy",
"Jaldi uthna hai, par neend ki bhi self-respect hai. #funny #sleep #morning #KrazyNotesy",
"Raat ki neend, class ka attendance, aur salary-teeno kam hai! #funny #students #money #KrazyNotesy",
"Khaane mein taste nahi, zindagi mein rest nahi. #funny #food #life #KrazyNotesy",
"Data pack khatam, zindagi bhi khatam! #funny #internet #relatable #KrazyNotesy",
"Mere jokes pe hans lo, warna main khud hans lunga. #funny #jokes #selflove #KrazyNotesy",
"Weight loss dream hai, but samose supreme hai. #funny #foodie #weightloss #KrazyNotesy",
"Dosti mein no sorry, no thank you. Bas treat chahiye! #funny #friendship #treat #KrazyNotesy",
"Wi-fi mil jaaye toh jagah apni lagti hai. #funny #wifi #desivibes #KrazyNotesy",
"Crush reply kare toh earthquake aa jaye! #funny #crush #flirting #KrazyNotesy",
"Budget tight, dil light! #funny #money #positivevibes #KrazyNotesy",
"Book mein answers nahi, Google zindabad! #funny #students #google #KrazyNotesy",
"College assignments-rocket science se kam nahi. #funny #assignments #students #KrazyNotesy",
"Sab kuch milega, bas maths ka answer nahi. #funny #math #students #KrazyNotesy",
"Parents bolte hain: 'Beta kuch karle', toh insta pe reel bana le! #funny #parents #reels #KrazyNotesy",
"Tareef ki toh aadat nahi hai yaar! #funny #compliment #awkward #KrazyNotesy",
"Work from home: 1% kaam, 99 aram! #funny #wfh #life #KrazyNotesy",
"Apna to style hi alag hai, attitude mein swag hai! #funny #style #attitude #KrazyNotesy",
"Bunk karte hain toh guilt nahi, swag aata hai. #funny #bunk #swag #KrazyNotesy",
"Kya din the school ke, lunch mein sabka dabba mera! #funny #school #food #KrazyNotesy",
"Dil hai ki maanta nahi, but neend har waqt aati hai. #funny #sleep #relatable #KrazyNotesy",
"Yeh jo daadi hai, lockdown ka asar hai. #funny #lockdown #beard #KrazyNotesy",
"Raat bhar Netflix, din bhar regret. #funny #netflix #regrets #KrazyNotesy"
,"Attendance ki kami se zyada neend ki kami mehsoos hoti hai. #funny #attendance #sleep #KrazyNotesy"
,"Coding me bug hai, zindagi me thug hai. #funny #coding #life #KrazyNotesy"
,"Na tu hero, na main zero, dono timepass ka saaman hai. #funny #friendship #timepass #KrazyNotesy"
,"Swag ka level toh battery ke percentage se bhi kam hai. #funny #swag #battery #KrazyNotesy"
,"Aaj soya nahi, kal uthunga nahi! #funny #sleep #lazy #KrazyNotesy"
,"Breakfast ke bahane uthne wale hum. #funny #breakfast #foodie #KrazyNotesy"
,"Family group = Good morning sticker ka museum. #funny #family #whatsapp #KrazyNotesy"
,"Sardi mein nahaane ki soch hi particular hai. #funny #winter #bath #KrazyNotesy",
"DP to hai, but asli wala andaaz baaki hai. #funny #dp #profile #KrazyNotesy",
"Free time mein busy rehne ka natak! #funny #free #busy #KrazyNotesy",
"Padhai ka time kabhi nahi aata. #funny #study #student #KrazyNotesy",
"Majboori ka naam zindagi, boss ka naam majboori! #funny #work #boss #KrazyNotesy",
"Lagta hai arrival late, magar attitude on time. #funny #attitude #late #KrazyNotesy",
"Kitni bhi sleep le lo, neend ki talash khatam nahi hoti. #funny #sleep #tired #KrazyNotesy"
 
]

def generate_caption_with_hashtags(filename):
    return random.choice(captions_list)

def pick_unposted_media():
    all_files = os.listdir(MEDIA_FOLDER)
    unposted_files = [f for f in all_files if f not in posted_history]

    if not unposted_files:
        print("All media has been posted!")
        return None

    return random.choice(unposted_files)

def upload_to_instagram(file_path, caption):
    ext = file_path.lower().split('.')[-1]
    if ext in ['jpg', 'jpeg', 'png']:
        cl.photo_upload(file_path, caption)
    elif ext in ['mp4', 'mov']:
        cl.video_upload(file_path, caption, thumbnail = None)
    else:
        print(f"Unsupported file type: {ext}")
        return False
    return True

def save_history(file_name):
    posted_history.append(file_name)
    with open(HISTORY_FILE, "w") as file:
        json.dump(posted_history, file)

# === Main Execution ===
media_file = pick_unposted_media()

if media_file:
    file_path = os.path.join(MEDIA_FOLDER, media_file)
    print(f"Posting: {media_file}")
    caption = generate_caption_with_hashtags(media_file)
    print(f"Caption Generated:\n{caption}\n")

    if upload_to_instagram(file_path, caption):
        save_history(media_file)
        print("Upload successful and history updated!")
    else:
        print("Upload failed.")
else:
    print("No new media to post.")
