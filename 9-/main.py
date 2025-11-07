from art import logo


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with ${bids[winner]} bid")


print(logo)


bids = {}

bidding = True
while bidding:
    name = input("What's your name: ")
    price = int(input("What's you bid: $"))
    bids[name] = price

    should_continue = input(
        "Are there any other bids? Type 'yes or 'no'.\n"
    ).lower()
    if should_continue == "no":
        bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 100)
