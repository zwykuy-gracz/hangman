from words import word
PLAYER_CHANCES = 5
first_round = True
game_on = True


def greetings():
    print('You have 5 chances to guess the word')
    # print("We're looking for this word: ", len(word), 'letters', stripped_word)
    print(f"We're looking for this word: {len(word)} letters {stripped_word}")

def guessing_word(word):
    users_word_guess = input('please type the answear: ').lower()
    if users_word_guess == word:
        print('Bravo! you won!')
        return False
    else:
        return True

def loosing_chance():
    print('Nope, try again. You lost one chance')
    PLAYER_CHANCES -= 1
    print(f"Chances left: {PLAYER_CHANCES}")

def splitting_to_single_characters(word):
    splitted_word = [char for char in word]
    return splitted_word

def list_underscore_word_lenght(word):
    word_to_be_guessed = []
    for n in range(len(word)):
        word_to_be_guessed.append('_ ')  
    return word_to_be_guessed

def stripping_word(word_to_be_guessed):
    stripped_word = str(word_to_be_guessed).strip('[]').replace('\'', '').replace(',', '')
    return stripped_word

def removing_guessed_letter(word_to_be_guessed, split_list, users_guess):

    if users_guess in split_list:
        for i in range(len(word)):
            if split_list[i] == users_guess:
                split_list[i] = '*'
                word_to_be_guessed[i] = users_guess

    current_status_for_player = word_to_be_guessed
    current_status_to_be_guessed = split_list
    return current_status_for_player, current_status_to_be_guessed


word_to_be_guessed = list_underscore_word_lenght(word)
stripped_word = stripping_word(word_to_be_guessed)
split_list = splitting_to_single_characters(word)

greetings()

while PLAYER_CHANCES > 0 and game_on:

    game_options = input('What you want to do? guess a [L]etter, guess the [W]ord or [Q]uit the game? ').lower()
    if game_options == 'l':
        users_guess = input('give me a letter: ').lower()
        if users_guess in split_list:
            if first_round:
                tuple_of_hidden_word = removing_guessed_letter(word_to_be_guessed, split_list, users_guess)
                print(stripping_word(tuple_of_hidden_word[0]))
                first_round = False
            else:
                tuple_of_hidden_word = removing_guessed_letter(players_status, hidden_word, users_guess)
                print(stripping_word(tuple_of_hidden_word[0]))
                set_word = set(tuple_of_hidden_word[1])
                if len(set_word) == 1:
                    print('You won! You guessed all letters!')
                    break
            players_status, hidden_word = tuple_of_hidden_word
        else:
            print('Nope, try again. You lost one chance')
            PLAYER_CHANCES -= 1
            print(f"Chances left: {PLAYER_CHANCES}")

    elif game_options == 'w':
        game_on = guessing_word(word)
        if game_on:
            print('Nope, try again. You lost one chance')
            PLAYER_CHANCES -= 1
            print(f"Chances left: {PLAYER_CHANCES}")

    elif game_options == 'q':
        print('Bye bye')
        break
    else: print('Wrong option')
    