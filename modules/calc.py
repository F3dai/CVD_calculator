
class calculate:

	def __init__(self, age:int, ldl:int, cholesterol:int, hdl:int, diastolic:int, systolic:int, diabetes:bool, smoker:bool):

		self.age = age
		self.ldl = ldl
		self.cholesterol = cholesterol
		self.hdl = hdl
		self.diastolic = diastolic
		self.systolic = systolic
		self.diabetes = diabetes
		self.smoker = smoker

		self.risk = False
		self.comparative = False

	def age_risk(self):

		if 30 <= self.age <= 34:
			self.comparative = 3
			return -1
		elif 35 <= self.age <= 39:
			self.comparative = 5
			return 0
		elif 40 <= self.age <= 44:
			self.comparative = 7
			return 1
		elif 45 <= self.age <= 49:
			self.comparative = 11
			return 2
		elif 50 <= self.age <= 54:
			self.comparative = 14
			return 3
		elif 55 <= self.age <= 59:
			self.comparative = 16
			return 4
		elif 60 <= self.age <= 64:
			self.comparative = 21
			return 5
		elif 65 <= self.age <= 69:
			self.comparative = 25
			return 6
		elif 70 <= self.age <= 74:
			self.comparative = 30
			return 7

	def ldl_risk(self):

		if self.ldl < 100:
			return -3
		elif 100 <= self.ldl <= 129:
			return 0 
		elif 130 <= self.ldl <= 159:
			return 0 
		elif 160 <= self.ldl < 190:
			return 1
		else:
			return 2

	def cholesterol_risk(self):

		if self.cholesterol < 160:
			return -3
		elif 160 <= self.cholesterol <= 199:
			return 0 
		elif 200 <= self.cholesterol <= 239:
			return 1
		elif 240 <= self.cholesterol < 279:
			return 2
		else:
			return 3

	def hdl_risk(self):

		if self.hdl < 35:
			return 2
		elif 35 <= self.hdl <= 44:
			return 1
		elif 45 <= self.hdl <= 49:
			return 0
		elif 50 <= self.hdl < 59:
			return 0
		else:
			return -1

	def pressure_risk(self):

		if self.diastolic < 80:
			if self.systolic < 130:
				return 0
			elif 130 <= self.systolic <= 139:
				return 1
			elif 140 <= self.systolic <= 159:
				return 2
			else:
				return 3

		elif 80 <= self.diastolic <= 84:
			if self.systolic < 130:
				return 0
			elif 130 <= self.systolic <= 139:
				return 1
			elif 140 <= self.systolic <= 159:
				return 2
			else:
				return 3

		elif 85 <= self.diastolic <= 89:
			if self.systolic < 140:
				return 1
			elif 140 <= self.systolic <= 159:
				return 2
			else:
				return 3

		elif 90 <= self.diastolic <= 99:
			if self.systolic < 160:
				return 2
			else:
				return 3

		else:
			return 3

	def diabetes_risk(self):

		if self.diabetes:
			return 2
		else:
			return 0

	def smoker_risk(self):

		if self.smoker:
			return 2
		else:
			return 0

	def calculate_risk(self):

		points = self.age_risk() + self.ldl_risk() + self.cholesterol_risk() + self.hdl_risk() + self.pressure_risk() + self.diabetes_risk() + self.smoker_risk()

		if points == -3:
			self.risk = 1
		elif points == -2:
			self.risk = 2
		elif points == -1:
			self.risk = 2
		elif points == 0:
			self.risk = 3
		elif points == 1:
			self.risk = 4
		elif points == 2:
			self.risk = 4
		elif points == 3:
			self.risk = 5
		elif points == 4:
			self.risk = 7
		elif points == 5:
			self.risk = 9
		elif points == 6:
			self.risk = 11
		elif points == 7:
			self.risk = 14
		elif points == 8:
			self.risk = 18
		elif points == 9:
			self.risk = 22
		elif points == 10:
			self.risk = 27
		elif points == 11:
			self.risk = 33
		elif points == 12:
			self.risk = 40
		elif points == 13:
			self.risk = 47
		else:
			self.risk = 56

		print(f"10 year CHD risk: {self.risk}%")
		print(f"Average for {self.age}: {self.comparative}")

		return {"risk" : self.risk, "average" : self.comparative}


obj = calculate(
	age = 66, # 6
	ldl = 160, #
	cholesterol = 101,
	hdl = 44,
	diastolic = 90,
	systolic = 133,
	diabetes = True,
	smoker = False
)

obj.calculate_risk()