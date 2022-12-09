from Operand import Operand
op = Operand(2147651233243422341134141241241242412341234211232131231223112341232311231231231221123 * 10)
op2 = Operand(2147651233243422341134141241241242412341234211232131231223112341232311231231231221123 * 10 ** 210)
print(op)
print(op2)
print(op.mul(op2))
def large_method():
    return 1/0

try:
    large_method()
except my_handled_exception as e:
    print(e)
except Exception as e:
    print("code failed: " + e)
