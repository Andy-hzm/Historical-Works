class Polynomial:
    def __init__(self, poly):
        monomial_minus = poly.split("-") # to get each monmial with parameter
        monomials = []
        for m in monomial_minus:
            monomial_plus = m.split("+")
            monomial_plus[0] = "-" + monomial_plus[0]
            for p in monomial_plus:
                monomials.append(p)
        if poly.startswith("-"):
            monomials.remove(monomials[0])
        else:
            monomials[0] = monomials[0][1:]
        try:
            eval(poly)
            variable = ""
        except:
            for i in poly:
                if i.isalpha():
                    variable = i
                    break

        self.monomials = monomials
        self.variable = variable

    def differentiate(self):
        if self.variable != "":    
            monomials = self.monomials[:]
            dif = ""
            for i in range(len(monomials)): # eliminate the monomial that is constant
                if self.variable not in monomials[i]:
                    monomials.remove(monomials[i])
                    break
            for mon in monomials:
                var_pos = mon.index(self.variable)
                if var_pos == 0: # get the parameter of the monomial
                    parameter = 1
                elif var_pos == 1:
                    parameter = -1
                else:
                    parameter = eval(mon[:var_pos - 1])

                if var_pos == len(mon)-1: # get the degree of the monomial 
                    degree = 1
                else:
                    degree = eval(mon[var_pos + 2:])

                new_para = parameter * degree
                degree -= 1
                if degree == 0: # prepare the degree after differentiation
                    deg = ""
                elif degree == 1:
                    deg = self.variable
                else:
                    deg = self.variable + "^" + str(degree)

                if new_para == 1:
                    if degree == 0:
                        new_para = "+1"
                    else:
                        new_para = "+"
                elif new_para == -1:
                    if degree == 0:
                        new_para = "-1"
                    else:
                        new_para = "-"
                else:
                    if degree != 0:
                        if str(new_para).startswith("-"):
                            new_para = str(new_para) + "*"
                        else:
                            new_para = "+" + str(new_para) + "*"
                    else:
                        if str(new_para).startswith("-"):
                            new_para = str(new_para)
                        else:
                            new_para = "+" + str(new_para)

                new_mon = new_para + deg
                dif += new_mon
            if dif.startswith("+"):
                dif = dif[1:]
        else:
            dif = 0
        return dif

def main():
    poly = input("Please input your polynomial: ")
    poly = Polynomial(poly)
    print(poly.differentiate())

main()       