
from termcolor import colored

def display_art():
    # ASCII Art for the message
    art = r"""
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║        🛠️ TOOL AVAILABLE FOR PURCHASE 🛠️        ║
    ║                                                  ║
    ║  Contact https://t.me/witchshophub to purchase   ║
    ║                                                  ║
    ║                Available Versions:               ║
    ║                                                  ║
    ║          1. 🌐 Web Version                       ║
    ║          2. 🐍 Python-Based                      ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    """
    # Print the ASCII art with green color
    print(colored(art, 'green'))

if __name__ == "__main__":
    display_art()
def send_email():
    subject = '🔥 Exclusive Tool for Sale! 🔥'
    body = """
    Hi there,  

    We are excited to offer you our latest tool that will make your work easier and more efficient!  

    ✅ Features:  
    - Fast and reliable  
    - Easy to use  
    - Affordable price  

    👉 To purchase, contact us at [@witchshophub](https://t.me/witchshophub).  

    Best Regards,  
    Witch Shop Hub Team  
    """

if __name__ == "__main__":
    send_email()
