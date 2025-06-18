# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

import art

print(art.logo)

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    # max(bidding_dictionary)

    for bidder in bidding_dictionary:
        # 金額の値を取り出す
        bid_amount = bidding_dictionary[bidder]

        # 比較して、今までの最高額より高ければ更新
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


continue_bidding = True
bids = {}
while continue_bidding :
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()
        if should_continue == "no":
            continue_bidding = False
            find_highest_bidder(bids)
        elif should_continue == "yes":
            print("\n" * 20)


