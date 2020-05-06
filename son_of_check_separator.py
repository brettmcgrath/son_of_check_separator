import math

print("Welcome to the handy dandy check separator. \nIn parts of this program where you are entering costs, you will be prompted to continue entering costs. Press 0 to move forward if there are no more costs to enter.")

payer_dict = {}
self_pay_dict = {}
other_charge_dict = {}
keys_list = []
shared_total = 0

payers = input("Do you have receipts that were paid by more than one person? ")
if payers == "yes":
	num_payers = int(input("From how many different payers do you have receipts? "))

for i in range(num_payers):
	payer_name = input("Name of payer {}: ".format(i+1))
	payer_dict.update({payer_name : 0})
	self_pay_dict.update({payer_name : 0})
	other_charge_dict.update({payer_name : 0})
	keys_list.append(payer_name)

def calc_total(): 
	print("Each person owes as follows (negative numbers reflect that you get paid):")
	for number, key in enumerate(keys_list):
		print(number + 1, key, ((shared_total / num_payers) + (other_charge_dict[key]) + (self_pay_dict[key])) - payer_dict[key])
	print("What each person paid pre-calculation: {}".format(payer_dict))
	print("What people bought for themselves: {}".format(self_pay_dict))
	print("Unshared costs to reimburse others: {}".format(other_charge_dict))
	print("Total amount of shareable costs that were split evenly: {}".format(shared_total))

def self_pay():
	global payer_dict
	global shared_total
	global self_pay_dict
	self_payer = input("Are there any charges on someone's receipt that they are wholly and solely responsible for? ")
	if self_payer == "yes": 
		for number, key in enumerate(payer_dict):
			print(number + 1, key)
		self_charge = keys_list[(int(input("Select who has charges on their bill no one else is responsible for splitting: ")) - 1)]
		already_paid = float(input("Enter ammount: "))
		self_pay_dict[(self_charge)] += already_paid
		shared_total -= already_paid
		while already_paid != 0:
			already_paid = float(input("Enter ammount: "))
			self_pay_dict[(self_charge)] += already_paid
			shared_total -= already_paid
		else:
			self_pay()
	else:
		calc_total()

def deduct():	
	global payer_dict
	global shared_total
	global other_charge_dict
	do_ya = input("Do you need to charge any items on one bill to anyone else's? ")
	if do_ya == "yes":
		for number, key in enumerate(payer_dict):
			print(number + 1, key)
		keys_list[(int(input("Select who needs items off their bill: ")) - 1)]
		chargee = keys_list[(int(input("Select who is charged: ")) - 1)]
		deduction = float(input("{}'s expenditure: ".format(chargee)))
		other_charge_dict[(chargee)]+=deduction
		shared_total -= deduction
		while deduction != 0:
			deduction = float(input("{}'s expenditure: ".format(chargee)))
			other_charge_dict[(chargee)]+=deduction
			shared_total -= deduction
		if deduction == 0:
			deduct()
	else: 
		self_pay()
		
def check_inventory(): 
	global shared_total
	global payer_dict
	for keys in payer_dict:
		check_count = int(input("How many checks did {} pay for? ".format(keys)))
		for checks in range(check_count):
			check_total = float(input("total of check {} for {}: ".format(checks+1, keys)))
			shared_total+=check_total
			payer_dict[(keys)]+=(check_total)
	deduct()
	
check_inventory()