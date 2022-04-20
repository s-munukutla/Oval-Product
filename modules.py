from temp import *
file = open('Product.xml', 'w')

def build_id(h):
    test_out = tst_id.format(data=h)
    file.writelines(test_out)
    file.write("\n")


def build_state(g):
    state_out = state_id.format(data=g)
    file.writelines(state_out)
    file.write("\n")


def build_jun_id(k):
    test_out_jun = tst_jun.format(data=k)
    file.writelines(test_out_jun)
    file.write("\n")

def build_state_jun(l):
    state_out_jun = state_jun.format(data=l)
    file.writelines(state_out_jun)
    file.write("\n")