import os
import csv
import random 
from utilities import generate_customer_id, generate_customer_name, generate_frequency, generate_customer_mobile

class CsvHanlder (object):
	"""docstring for ClassName"""
	def __init__(self, **kwargs):
		super(object, self).__init__()
		#請設計一個 CsvHanlder class，當它被初始化時，會偵測相同目錄下是否存在一個 ilovecoffee 資料夾，若無則建立，有則略過。

		if os.path.isdir('ilovecoffee'):
			print("ilovecoffee directory exist")
		else:
			print("ilovecoffee directory doesn't exist")
			os.system("mkdir ilovecoffee")


	def create_csv(self):
		header = ['customer_id', 'customer_name', 'customer_mobile', 'frequency']

		with open('./ilovecoffee/customers.csv', 'w',newline='') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=',')
			csvwriter.writerow(header)

			number_history  = {} #hash for speedup checking procedures
			for i in range(3):
				customer_id = generate_customer_id()

				customer_mobile = generate_customer_mobile()
				while(number_history.get(customer_mobile)):
					customer_mobile = generate_customer_mobile()

				single_row = [
					"{}".format(customer_id),
					"{}".format(generate_customer_name(customer_id)),
					"{}".format(customer_mobile),
					"{}".format(generate_frequency()),
				]
				csvwriter.writerow(single_row)
				number_history[customer_mobile] = True
			fieldnames = header


	def calculate_csv(self):
		with open('./ilovecoffee/customers.csv',newline='') as csvfile:
			rows = csv.DictReader(csvfile)

			mode_map = [0 for i in range(21)] #for 中位數

			s = 0 #for 平均數
			#s = []
			for r in rows:
				val = int(r['frequency'])
				mode_map[val] += 1
				s += val
				#s.append(val)

			mode = max(mode_map)
			mode_max_count = 0
			for i in mode_map:
				if i == mode:
					mode_max_count += 1
			if mode_max_count > 1:
				mode = None
				

			total = sum(mode_map)
			print(f"total nums = {total}")
			median, prev_val, prev, current = (0, 0, 0, 0)
			for i, i_val in enumerate(mode_map):
				current += i_val
				if int(total/2) in range(prev, current):
					if total%2 == 0 and total/2 == prev:
						median = (i + prev_val)*0.5
						break
					elif total%2 == 0:
						median = i
						break
					else:
						median = i
						break
				if i_val > 0:
					prev_val = i
				prev = current
			
			print("平均數 = {}".format(round(s/total, 5)))
			print("眾數 = {}".format(mode))
			print("中位數 = {}".format(median))

def main():
	c = CsvHanlder()
	c.create_csv()
	c.calculate_csv()

if __name__ == '__main__':
	main()