import subprocess
import time
import random
import os
from threading import Thread
import sys

CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f"""{CYAN}
    ╔══════════════════════════════════════════╗
    ║  {GREEN}██╗  ██╗██╗███╗   ██╗ █████╗ ███████╗  {CYAN}║
    ║  {GREEN}██║  ██║██║████╗  ██║██╔══██╗██╔════╝  {CYAN}║
    ║  {GREEN}███████║██║██╔██╗ ██║███████║█████╗    {CYAN}║
    ║  {GREEN}██╔══██║██║██║╚██╗██║██╔══██║██╔══╝    {CYAN}║
    ║  {GREEN}██║  ██║██║██║ ╚████║██║  ██║███████╗  {CYAN}║
    ║  {GREEN}╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝  {CYAN}║
    ║                                        {CYAN}║
    ║{BOLD}{YELLOW}        Digital Crew 243 - Neo     {CYAN}║
    ╚══════════════════════════════════════════╝{RESET}
    """)

def typewriter(text, color=CYAN, delay=0.03):
    colored_text = f"{color}{text}{RESET}"
    for char in colored_text:
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
    typewriter("INITIALIZING NEURALINK...", GREEN, 0.02)
    
    typewriter("TARGET ACQUISITION:", BLUE)
    target_number = input(f"{PURPLE}╠══[DC243]> {RED}PHONE: {RESET}").strip()
    
    typewriter("FLOOD INTENSITY:", BLUE)
    spam_count = int(input(f"{PURPLE}╠══[DC243]> {RED}COUNT: {RESET}"))
    
    typewriter("ATTACK TIMING:", BLUE)
    delay_min = float(input(f"{PURPLE}╠══[DC243]> {RED}MIN(s): {RESET}"))
    delay_max = float(input(f"{PURPLE}╠══[DC243]> {RED}MAX(s): {RESET}"))
    
    messages = load_spam_messages()
    typewriter(f"PAYLOADS LOADED: {len(messages)}", YELLOW)
    
    clear_screen()
    print_banner()
    typewriter("NEURALINK SYNC CONFIRMED?", RED)
    confirm = input(f"{PURPLE}╠══[DC243]> {RED}LAUNCH (Y/N): {RESET}").lower()
    
    if confirm == 'y':
        typewriter("FLOOD SEQUENCE ACTIVE...", GREEN)
        typewriter("DIGITAL CREW 243 - ONLINE", YELLOW)
        
        spam_thread = Thread(target=spam_worker, args=(target_number, messages, spam_count, (delay_min, delay_max)))
        spam_thread.daemon = True
        spam_thread.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            typewriter("NEURALINK DISCONNECTED", RED)
    else:
        typewriter("OPERATION CANCELLED", RED)

if __name__ == "__main__":
    main()