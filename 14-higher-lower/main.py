from random import choice
from game_data import data
from art import vs, logo


def pick_account():
    return choice(data)


def pick_account_correctly(other_account):
    account = pick_account()
    is_not_correct = True
    while is_not_correct:
        if account == other_account:
            account = pick_account()
        else:
            is_not_correct = False

    return account


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account_a["country"]}"


def check_answer(answer, acc_a, acc_b) -> bool:
    correct_answer = "A" if acc_a['follower_count'] > acc_b['follower_count'] else "B"

    return answer == correct_answer


print(logo)
score = 0
game_over = False
account_a = pick_account()
account_b = pick_account_correctly(account_a)
while not game_over:
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if check_answer(answer, account_a, account_b):
        score += 1
        print(f"You're right! Current Score {score}")
        account_a = account_b
        account_b = pick_account_correctly(account_a)
    else:
        print(f"You're Wrong! Current Score {score}")
        game_over = True
