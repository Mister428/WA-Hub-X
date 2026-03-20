import subprocess
import time
import random
import os
from threading import Thread

def load_spam_messages(filename="spam.txt"):
    if not os.path.exists(filename):
        default_messages = [
            "Test spam 1 🚀",
            "Test spam 2 🔥",
            "Test spam 3 💥",
            "Contactez-nous maintenant ! 📱",
            "Offre spéciale limitée ⏰"
        ]
        with open(filename, 'w') as f:
            f.write('\n'.join(default_messages))
    
    with open(filename, 'r', encoding='utf-8') as f:
        messages = [line.strip() for line in f.readlines() if line.strip()]
    return messages

def open_whatsapp_link(phone_number, message):
    clean_number = ''.join(filter(str.isdigit, phone_number))
    encoded_message = message.replace(' ', '%20').replace('\n', '%0A')
    link = f"https://wa.me/{clean_number}?text={encoded_message}"
    
    try:
        subprocess.Popen(['xdg-open', link])
    except:
        try:
            subprocess.Popen(['open', link])
        except:
            subprocess.Popen(['start', link], shell=True)

def spam_worker(phone_number, messages, spam_count, delay_range):
    for i in range(spam_count):
        msg = random.choice(messages)
        open_whatsapp_link(phone_number, msg)
        delay = random.uniform(*delay_range)
        time.sleep(delay)

def main():
    print("🔥 WhatsApp Spammer Tool")
    print("=" * 50)
    
    target_number = input("📱 Numéro cible: ").strip()
    spam_count = int(input("🔢 Nombre de spams: "))
    delay_min = float(input("⏱️ Délai min (s): "))
    delay_max = float(input("⏱️ Délai max (s): "))
    
    messages = load_spam_messages()
    
    confirm = input("\n🚀 Lancer? (o/n): ").lower()
    if confirm == 'o':
        spam_thread = Thread(target=spam_worker, args=(target_number, messages, spam_count, (delay_min, delay_max)))
        spam_thread.daemon = True
        spam_thread.start()
        print("💥 Spam lancé! Ctrl+C pour arrêter.")
        try:
            spam_thread.join()
        except KeyboardInterrupt:
            print("\n🛑 Arrêté.")

if __name__ == "__main__":
    main()