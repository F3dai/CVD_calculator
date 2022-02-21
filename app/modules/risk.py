
class calculate:

        def __init__(self, sex:str, age:int, smoker:bool, systolic:int, cholesterol:int, hdl:int):

                self.sex = self._is_sex(sex)
                self.age = self._is_int(age)
                self.smoker = self._is_bool(smoker)
                self.systolic = self._is_int(systolic)
                self.cholesterol = self._is_int(cholesterol)
                self.hdl = self._is_int(hdl)

                self.age_index = False


        ## Validation Checks ##

        def _is_int(self, item):
                try:
                        return int(item)
                except:
                        raise ValueError(f"{item} is not an integer.")
        
        def _is_sex(self, item):
                if item in ["male", "female"]:
                        return item
                else:
                        raise ValueError(f"{item} is not a valid sex.")

        def _is_bool(self, item):
                if item == "True":
                        return True
                elif item == "False":
                        return False
                else:
                        raise ValueError(f"{item} is not a boolean.")


        def age_risk(self):

                index = False

                # Points for each sex, index
                sex_points = {
                        "male": [-9, -4, 0, 3, 6, 8, 10, 11, 12, 13],
                        "female" : [-7, -3, 0, 3, 6, 8, 10, 12, 14, 16]
                }

                # Return index
                if 30 <= self.age <= 34:
                        self.age_index =  0
                elif self.age <= 39:
                        self.age_index =  1
                elif self.age <= 44:
                        self.age_index =  2
                elif self.age <= 49:
                        self.age_index =  3
                elif self.age <= 54:
                        self.age_index =  4
                elif self.age <= 59:
                        self.age_index =  5
                elif self.age <= 64:
                        self.age_index =  6
                elif self.age <= 69:
                        self.age_index =  7
                elif self.age <= 74:
                        self.age_index =  8
                else:
                        return {"error" : f"Age out of range. Must be between 30 and 74"}

                return sex_points[self.sex][index]


        def cholesterol_risk(self):

                # Index for age and sex
                cholesterol_points = { 
                        "male" : [
                                # Age index
                                [0, 4, 7, 9, 11],
                                [0, 4, 7, 9, 11],
                                [0, 3, 5, 6, 8],
                                [0, 3, 5, 6, 8],
                                [0, 2, 3, 4, 5],
                                [0, 2, 3, 4, 5],
                                [0, 1, 1, 2, 3],
                                [0, 1, 1, 2, 3],
                                [0, 0, 0, 1, 1],
                                [0, 0, 0, 1, 1]
                        ],
                        "female" : [
                                # Age index
                                [0, 4, 8, 11, 13],
                                [0, 4, 8, 11, 13],
                                [0, 3, 6, 8, 10],
                                [0, 3, 6, 8, 10],
                                [0, 2, 4, 5, 7],
                                [0, 2, 4, 5, 7],
                                [0, 1, 2, 3, 4],
                                [0, 1, 2, 3, 4],
                                [0, 1, 1, 2, 2],
                                [0, 1, 1, 2, 2]
                        ]
                }

                if self.cholesterol < 160:
                        index = 0
                elif 160 <= self.cholesterol <= 199:
                        index = 1
                elif 200 <= self.cholesterol <= 239:
                        index = 2
                elif 240 <= self.cholesterol < 280:
                        index = 3
                else:
                        index = 4

                return cholesterol_points[self.sex][self.age_index][index]


        def smoker_risk(self):

                smoker = {
                        "male" : [
                                [0, 8],
                                [0, 8],
                                [0, 5],
                                [0, 5],
                                [0, 3],
                                [0, 3],
                                [0, 1],
                                [0, 1],
                                [0, 1],
                                [0, 1]
                        ], 
                        "female" : [
                                [0, 9],
                                [0, 9],
                                [0, 7],
                                [0, 7],
                                [0, 4],
                                [0, 4],
                                [0, 2],
                                [0, 2],
                                [0, 1],
                                [0, 1]
                        ]
                }

                if self.smoker:
                        return smoker[self.sex  ][self.age_index][self.smoker]
                else:
                        return 0


        def hdl_risk(self):

                hdl = [-1, 0, 1, 2] # keeping 1d array to be consistent

                if self.hdl < 40:
                        index = 3
                elif self.hdl <= 49:
                        index = 2
                elif self.hdl < 59:
                        index = 1
                else:
                        index = 0

                return hdl[index] # Sex irrelevant


        def pressure_risk(self):

                pressure = {
                        "male" : [0, 1, 2, 2, 3], 
                        "female" : [0, 3, 4, 5, 6]
                }

                if self.systolic < 120:
                        index = 0
                elif self.systolic <= 130:
                        index = 1
                elif self.systolic < 140:
                        index = 2
                elif self.systolic < 160:
                        index = 3
                else:
                        index = 4

                return pressure[self.sex        ][index]


        def calculate_risk(self):

                print("calculate_risk")

                risk = {
                        "male" : [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25],
                        "female" : [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 11, 14, 17, 22, 27]
                };

                points = self.age_risk() + self.cholesterol_risk() + self.hdl_risk() + self.pressure_risk() + self.smoker_risk()

                ten_year_risk = risk[self.sex][points]

                # print(f"10 year CHD risk: {ten_year_risk}%")
                

                print("risk")
                return {"risk" : ten_year_risk}



