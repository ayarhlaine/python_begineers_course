def check_gender_and_height(is_male, is_tall):
    if is_male and is_tall:
        print("You are a tall man.")
    elif is_male and not is_tall:
        print("You are a short man.")
    elif not is_male and is_tall:
        print("You are a tall woman.")
    else:
        print("You are a short woman.")


check_gender_and_height(True, True)
check_gender_and_height(True, False)
check_gender_and_height(False, True)
check_gender_and_height(False, False)
