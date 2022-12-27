import random 
NAME_LIST = ["Abe", "Ron", "Ben", "Ken", "Umi", "Ika", "Emi", "Obi", "Tim", "Nia"]
CHAR_LIST = [i for i in range(65, 91)] + [i for i in range(97, 123)] + [i for i in range(48, 58)]  #upper + lower + num
CHAR_LIST_LEN = len(CHAR_LIST)

def generate_customer_id():
    s = ''
    s += chr(CHAR_LIST[random.randrange(0, CHAR_LIST_LEN-9)])
    for i in range(7):
        s += chr(CHAR_LIST[random.randrange(0, CHAR_LIST_LEN)])
    return s

def generate_customer_name(generate_customer_id):
	return NAME_LIST[random.randrange(0, 10)] + "." + generate_customer_id

def generate_frequency():
	return str(random.randrange(0, 21))

def generate_customer_mobile():
	#+886 918300227
	return '+886' + (str(random.randrange(100000000, 1000000000)))