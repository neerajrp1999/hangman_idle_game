import random
from hangman_guessing import guess_list
from hangman_life import game_name,lives

guessing_word=random.choice(guess_list).lower()
#print(guess_list)
word_letters=len(guessing_word)

game_over=False
tries=6
print(game_name)

print(f'The word you guessed is {guessing_word}')


result=[]
for _ in range(word_letters):
    result+='_'
#print(result)

while not game_over:
    user_guessing=input('Guess a Letter: ')

    if user_guessing in result:
        print(f'The letter you have guessed is {user_guessing}')
    for position in range(word_letters):
        letter=guessing_word[position]
        if letter==user_guessing:
            result[position]=letter

    if user_guessing not in guessing_word:
        print(f'You guessed {user_guessing} , This letter is not in the word, you lose a try')


        tries-=1
        if tries==0:
            game_over=True
            print('Game Over, You Lose the Game, try again later')
    print(f"{' '.join(result)}")
    if '_' not in result:
        game_over=True
        prin('You are winner , congratulations')
    print(lives[tries])
