def skip_more_mafia():
	find("HMMIlHiIMKUl.png")
	hover("1314087904035.png")
	click("1314087916882.png")
	click("F1l.png")


def full_screen():
	# Turn screen full
	hover("1314084232728.png")
	click("5.png")
	click("1314084149113.png")


def open_attack():
	# Open attack window
	hover("Z.png")
	click("ff.png")
	click("1314083920754.png")

def close_window():
	click("X.png")

def get_money():
	for x in findAll("1315535521722.png"):
		# Get money
		hover("1315535538044.png")
		click("7.png")
		click("1315535558482.png")

def has_bullets():
	# Returns true if the screen has bullets, otherwise, false.
	return not (find("1314088449654.png"))

def attack():
	hover("1314088569457.png")
	click("1314088588017.png")
	click("ATTACK.png")
	wait("1314088720880.png")

def close_attack_result():
	hover("1314088679928.png")
	click("1314088720880.png")
	click("A.png")

def save_money():
	# open bank
	hover("1315535105119.png")
	click("1315535139765.png")

	# save money
	hover("sell")	
	click("1315535499189.png")
	popup("over")
	return
	
	print hover("Illili.png")
	click("1315535320305.png")
	close_window()

def find_all(obj):
	for x in findAll(obj):
		print x
	popup("over")

get_money()