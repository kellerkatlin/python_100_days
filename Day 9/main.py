# # "TODO"-1: Pregunta el usuario para el input
# name = input("What is your name? ")
# price = int(input("What is the price?: $"))

# # "TODO"-2: Guardar data en el dictionary {name: price}
# bids[name] = price

# "TODO"-3 Whether if new bids need to be added
# "TODO"-4: Compare bids in the dictionary
import art

print(art.logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
bids = {}
continue_bidding = True 
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your price?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n *20")

