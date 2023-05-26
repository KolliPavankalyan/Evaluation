class Number: 
    def add_digit(self,num):
        while num > 9:
            sum = 0
            while num>0:
                r = num%10
                sum += r
                num = num//10
            num = sum
        return sum
obj  = Number()
print(obj.add_digit(6821))