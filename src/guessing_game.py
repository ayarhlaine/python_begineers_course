MAX_ATTEMPT_LIMIT = 3
secret_world = "Apple"
guess = ""
no_of_attempt = 0
is_guess_correct = False

while secret_world != guess and no_of_attempt < MAX_ATTEMPT_LIMIT:
    guess = input("Enter guess with the name of fruits: ")
    no_of_attempt += 1
    if secret_world == guess:
        is_guess_correct = True

if is_guess_correct:
    print("You win!")
else:
    print("Out of limit, you lose!")
