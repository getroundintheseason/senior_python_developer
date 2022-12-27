from fibonacci import Fibonacci, Permutation

class phone:
	def __init__(self, **kwargs):
		self.price = kwargs['price']
		self.camera_count = kwargs['camera_count']
		self.screen_size = kwargs['screen_size']

class GooglePhone(phone):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def special_freature(self, input_list):
    	return self.getEvenGreaterThan10(input_list)

    def getEvenGreaterThan10(self, input_list):
    	temp_list = [i for i in input_list if i>10 and i%2==0]
    	temp_list.sort()
    	return temp_list


class TaiwanPhone(phone):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def special_freature(self, index):
        res = Fibonacci(index)
        px = int((res%100)/10)
        y = res%10

        return Permutation(px, y)


if __name__ == "__main__":
	a = GooglePhone(price=10, camera_count=3, screen_size=5) 
	print(a.special_freature([11,12,14,15,16,17,18,19,8]))


	b = TaiwanPhone(price=20, camera_count=1, screen_size=3)
	print(b.special_freature(10))