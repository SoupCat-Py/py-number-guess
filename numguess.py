# MOST STABLE VERSION (v3)
# copyright (c) 2025 Soup Cat

from random import randint as rand
import os, json

diffs = {
	'easy'	: 100,
	'medium' : 1000,
	'hard'   : 10000,
	'insane' : 1000000
}

json_path = os.path.expanduser('~/Downloads/numguess_hs.json')


def load_hs():
	global high_scores
	if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
		with open(json_path, 'x') as file:
			json.dump({},file)
			high_scores = {}
	else:
		with open(json_path,'r') as file:
			high_scores = json.load(file)

load_hs()

def save_hs():
	global high_scores
	if os.path.exists(json_path):
		with open(json_path,'w') as file:
			json.dump(high_scores, file)
	else:
		with open(json_path,'x') as file:
			file.close()

def save_and_close():
	save_hs()
	os._exit(0)

def get_num():
	asking = True
	while asking:
		num_in = input('> ')
		try:
			num_in = int(num_in)
			asking = False
			return num_in
		except:
			if num_in.lower() in ['exit','quit','close','give up']:
				return num_in.lower()

def get_diff():
	global high_scores
	print('Choose a difficulty:')
	print('EASY | MEDIUM | HARD | INSANE | CUSTOM (enter max)')
	
	asking = True
	while asking:
		diff_in = input('> ')
		# figure out what to do
		if diff_in.lower() in diffs:
			return diffs[diff_in.lower()]
		else:
			try:
				int(diff_in)
				return int(diff_in)
			except:
				if diff_in.lower() in ['exit','quit','close']:
					save_and_close()
				elif 'hs' in diff_in.lower():
					in_list = diff_in.lower().split(' ')
					if high_scores == {}:
						print('you have no high scores')
					try:
						print(f'your high score for {in_list[1]} is {high_scores[in_list[1]]}')
					except:
						if len(in_list) == 1:
							diff_len = 0
							for diff in high_scores:
								if len(str(diff)) > diff_len:
									diff_len = len(str(diff))
							for diff, score in high_scores.items():
								sep = '-' * (diff_len - len(str(diff)) + 3)
								print(f'{diff} {sep} {score}')
						elif in_list[1].lower() in ['clear','delete']:
							if 'y' in input('are you sure??? '):
								high_scores = {}
								save_hs()
								print('high scores cleared')
				elif 'help' in diff_in.lower():
					print('close program       - "close" or "quit" or "exit"')
					print('see the number      - "give up"')
					print('all high scores     - "hs"')
					print('specific high score - "hs [max]"')

def line():
	print('')
 
def sort_hs():
	return {k: high_scores[k] for k in sorted(high_scores, key=lambda x: int(x))}

# main loop
running = True
print('Welcome to the number guessing game!')
print('type "help" for commands')
while running:
	line()

	max = get_diff()
	
	num = rand(0,max)
	while num % 10 == 0:
		num = rand(0,max)
  
	line()

	# the actual game
	guessing = True
	tries = 0
	print(f'Guess a number from 1 to {max}')
	guesses = []
	while guessing:
		guess = get_num()

		# logic
		if guess == 'give up':
			print(f'the number was {num}')
			guessing = False
		elif guess in ['exit','quit','close']:
			save_and_close()
		
		elif guess == num:
			tries += 1
			line()
			print('YOU WIN!')
			print(f'it took you {tries} tries')

			# high scores
			if str(max) not in high_scores:
				high_scores[str(max)] = tries
				print('NEW HIGH SCORE!')
			elif str(max) in high_scores and tries < high_scores[str(max)]:
				high_scores[str(max)] = tries
				print('NEW HIGH SCORE!')

			print(f'your best was {high_scores[str(max)]}')
			high_scores = sort_hs()
			guessing = False
		elif guess > max:
			print('OUT OF RANGE')
		elif guess > num or guess < num:
			if guess not in guesses:
				tries += 1
				guesses.append(guess)
			else:
				print('you already guessed that')
			text = 'higher' if guess < num else 'lower'
			print(text)
