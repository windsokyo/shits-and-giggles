import random
from time import sleep

def spin_row():
	symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
	return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
	print("********")
	print("|".join(row))
	print("********")

def get_payout(row, bet):
	if row[0] == row[1] == row[2]:
		if row[0] == '🍒':
			return bet * 3
		elif row[0] == '🍉':
			return bet * 4
		elif row[0] == '🍋':
			return bet * 5
		elif row[0] == '🔔':
			return bet * 10
		elif row[0] == '⭐':
			return bet * 20
	return 0


def main():
	balance = 100
	print("_________________________\nWelcome to the Coin Slots\nSymbols: 🍒 🍉 🍋 🔔 ⭐\n_________________________")

	while balance > 0:
		print(f"Current balance: ₱{balance}")
		bet = input("Please enter your bet: ₱")

		if not bet.isdigit():
			print("Please enter a VALID number.")
			continue

		bet = int(bet)

		if bet == balance:
			print("Can't lose yet!")
			continue

		if bet > balance:
			print("Insufficient funds.")
			continue

		if bet <= 0:
			print("Your bet must be greater than 0.")
			continue

		balance -= bet

		row = spin_row()
		print("Spinning...")
		sleep(0.5)
		print(print_row(row))

		payout = get_payout(row, bet)
		if payout > 0:
			print(f"You won ₱{payout}")
		else:
			print(f"Sorry, but you lost this round.")

		balance += payout

		play_again = input("Would you like to spin again? (Y/N)").upper()
		if play_again != 'Y':
			break

	print(f"Game over! Your final balance is ₱{balance}.")
			
if __name__ == "__main__":
	main()