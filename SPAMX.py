import subprocess
import time
import random
import os
from threading import Thread
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print("""
    ╔══════════════════════════════════════════╗
    ║  ██╗  ██╗██╗███╗   ██╗ █████╗ ███████╗  ║
    ║  ██║  ██║██║████╗  ██║██╔══██╗██╔════╝  ║
    ║  ███████║██║██╔██╗ ██║███████║█████╗    ║
    ║  ██╔══██║██║██║╚██╗██║██╔══██║██╔══╝    ║
    ║  ██║  ██║██║██║ ╚████║██║  ██║███████╗  ║
    ║  ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝  ║
    ║                                          ║
    ║        Digital Crew 243 - Neo Edition    ║
    ╚══════════════════════════════════════════╝
    """)

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def load_spam_messages(filename="spam.txt"):
    if not os.path.exists(filename):
        default_messages = ["Digital Crew Alert 🚀", "243 Access Granted 🔥", "Neo Flood Active 💥"]
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
    print_banner()
    typewriter("INITIALIZING...", 0.02)
    
    typewriter("TARGET:", 0.02)
    target_number = input("╠══[DC243]> PHONE: ").strip()
    
    typewriter("INTENSITY:", 0.02)
    spam_count = int(input("╠══[DC243]> COUNT: "))
    
    typewriter("TIMING:", 0.02)
    delay_min = float(input("╠══[DC243]> MIN(s): "))
    delay_max = float(input("╠══[DC243]> MAX(s): "))
    
    messages = load_spam_messages()
    typewriter(f"LOADED: {len(messages)} MSG", 0.02)
    
    clear_screen()
    print_banner()
    typewriter("LAUNCH? (Y/N)", 0.02)
    confirm = input("╠══[DC243]> CONFIRM: ").lower()
    
    if confirm == 'y':
        typewriter("FLOOD ACTIVE...", 0.02)
        typewriter("DC243 ONLINE", 0.02)
        
        spam_thread = Thread(target=spam_worker, args=(target_number, messages, spam_count, (delay_min, delay_max)))
        spam_thread.daemon = True
        spam_thread.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            typewriter("ABORTED", 0.02)
    else:
        typewriter("CANCELLED", 0.02)

if __name__ == "__main__":
    main()