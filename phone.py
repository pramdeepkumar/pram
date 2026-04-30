# Simple PhonePe-like terminal app simulation
import getpass
import sys

users = {
	'user1': {'pin': '1234', 'balance': 5000, 'history': []},
	'user2': {'pin': '5678', 'balance': 3000, 'history': []}
}

def clear_screen():
	print("\n" * 50)

def login():
	print("=== Welcome to PhonePay ===")
	username = input("Enter username: ")
	if username not in users:
		print("User not found!")
		return None
	pin = getpass.getpass("Enter 4-digit PIN: ")
	if pin == users[username]['pin']:
		print("Login successful!\n")
		return username
	else:
		print("Incorrect PIN!")
		return None

def show_menu():
	print("1. Check Balance")
	print("2. Send Money")
	print("3. Transaction History")
	print("4. Exit")

def check_balance(username):
	print(f"Your balance: ₹{users[username]['balance']}")

def send_money(username):
	to_user = input("Send to (username): ")
	if to_user not in users or to_user == username:
		print("Invalid recipient!")
		return
	try:
		amount = float(input("Amount to send: ₹"))
	except ValueError:
		print("Invalid amount!")
		return
	if amount <= 0 or amount > users[username]['balance']:
		print("Insufficient balance or invalid amount!")
		return
	users[username]['balance'] -= amount
	users[to_user]['balance'] += amount
	users[username]['history'].append(f"Sent ₹{amount} to {to_user}")
	users[to_user]['history'].append(f"Received ₹{amount} from {username}")
	print(f"₹{amount} sent to {to_user} successfully!")

def transaction_history(username):
	print("--- Transaction History ---")
	if not users[username]['history']:
		print("No transactions yet.")
	else:
		for h in users[username]['history']:
			print(h)

def main():
	while True:
		user = login()
		if user:
			break
	while True:
		show_menu()
		choice = input("Choose an option: ")
		if choice == '1':
			check_balance(user)
		elif choice == '2':
			send_money(user)
		elif choice == '3':
			transaction_history(user)
		elif choice == '4':
			print("Thank you for using PhonePay!")
			sys.exit()
		else:
			print("Invalid choice!")
		input("\nPress Enter to continue...")
		clear_screen()

if __name__ == "__main__":
	main()
