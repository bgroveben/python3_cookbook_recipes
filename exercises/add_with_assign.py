################################################################################
# This little file will help me to better understand how Python bytecode works.
################################################################################
import dis

def add_with_assign(a, b):
    x = a + b
    return x

dis.dis(add_with_assign)
