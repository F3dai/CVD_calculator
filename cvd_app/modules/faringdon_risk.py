class Calculate:

        def __init__(self, sex, age, smoker, systolic, cholesterol, hdl, treatment):

                self.sex = self._is_int(sex)
                self.age = self._is_int(age)
                self.cholesterol = self._is_int(cholesterol)
                self.hdl = self._is_int(hdl)
                self.systolic = self._is_int(systolic)
                self.smoker = self._is_int(smoker)
                self.treatment = self._is_int(treatment)

        ## Validation Checks ##

        def _is_int(self, item):
                try:
                        return int(item)
                except:
                        raise ValueError(f"{item} is not an integer.")
        
        def _is_sex(self, item):
                assert item in ["male", "female"]
                return item

        def _is_bool(self, item):
                if item == "True":
                        return True
                elif item == "False":
                        return False
                else:
                        raise ValueError(f"{item} is not a boolean.")

        ## Calculator ##

        def average(self):
                score = [1, 1, 4, 4, 8, 10, 13, 20, 22, 25]
                return score[self.age]

        def age_risk(self):
                score = [-9, -4, 0, 3, 6, 8, 10, 11, 12, 13, -7, -3, 0, 3, 6, 8, 10, 12, 14, 16]
                return score[self.age + (self.sex * 10)]


        def cholesterol_risk(self):
                score = [0, 4, 7, 9, 11, 0, 4, 8, 11, 13, 0, 4, 7, 9, 11, 0, 4, 8, 11, 13, 0, 3, 5, 6, 8, 0, 3, 6, 8, 10, 0, 3, 5, 6, 8, 0, 3, 6, 8, 10, 0, 2, 3, 4, 5, 0, 2, 4, 5, 7, 0, 2, 3, 4, 5, 0, 2, 4, 5, 7, 0, 1, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 1, 2, 3, 0, 1, 2, 3, 4, 0, 0, 0, 1, 1, 0, 1, 1, 2, 2, 0, 0, 0, 1, 1, 0, 1, 1, 2, 2]
                return score[self.cholesterol + (self.sex * 5) + (self.age * 10)]


        def smoker_risk(self):
                score = [8, 9, 8, 9, 5, 7, 5, 7, 3, 4, 3, 4, 1, 2, 1, 2, 1, 1, 1, 1]
                if self.smoker == 1:
                        return score[self.sex + (self.age * 2)]
                else:
                        return 0

        def hdl_risk(self):
                return self.hdl
        
        def systolic_risk(self):
                score = [0, 0, 1, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 2, 3, 0, 3, 4, 5, 6]
                if (self.systolic + (self.sex * 5) + (self.treatment * 10)) >= 0:
                        return score[self.systolic + (self.sex * 5) + self.treatment * 10]
                else:
                        return 0

        def calculate_risk(self):
                score = ['1', '1', '1', '1', '1', '2', '2', '3', '4', '5', '6', '8', '10', '12', '16', '20', '25', '<1', '<1', '<1', '<1', '<1', '<1', '<1', '<1', '<1', '<1', '1', '1', '1', '1', '2', '2', '3', '4', '5', '6', '8', '11', '14', '17', '22', '27', '>=30']

                total = self.age_risk() + self.cholesterol_risk() + self.smoker_risk() + self.hdl_risk() + self.systolic_risk()
                if (total >= 17 and self.sex == 0) or (total >= 25 and self.sex == 1):
                        result = '>=30'
                elif total < 0:
                        result = '<1'
                else:
                        result = score[total + (self.sex * 18)]

                return {"status" : "successful", "message" : {"risk" : result, "average" : self.average()}}