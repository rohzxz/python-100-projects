import clear
dic ={
    "harry":"human being",
    "Spoon":"object"
}
print(dic["harry"])
print(dic.keys())

from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
# cleardomo = clear()
# print(cleardomo)
bids ={}
bidding_finished = False

def find_highest_bidder(bid_record):
  highest_bid =0
  winner =""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner =bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
print(logo)
    
while not bidding_finished:
  nameInput = input(f"what is your name ?\n")
  bidInput = int(input(f"what is bid price ? \n"))
  bids[nameInput]= bidInput
  should_continue= input("are they any other bidders? type yes or no ") 
  if should_continue == "no":
    bidding_finished =True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  