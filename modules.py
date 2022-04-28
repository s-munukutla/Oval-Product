from temp import *
file = open('Product.xml', 'w')

def build_id(h):
    for i in h:
        test_out = tst_id.format(data=i)
        file.writelines(test_out)
        file.write("\n")


def build_state(g):
    for i in g:
        state_out = state_id.format(data=i)
        file.writelines(state_out)
        file.write("\n")


def build_jun_id(k):
    for i in k:
        test_out_jun = tst_jun.format(data=i)
        file.writelines(test_out_jun)
        file.write("\n")

def build_jun_state(l):
    for i in l:
        state_out_jun = state_jun.format(data=i)
        file.writelines(state_out_jun)
        file.write("\n")

def build_crt(d):
    for i in d:
        crt_out = crt_id.format(data=i)
        file.writelines(crt_out)
        file.write("\n")


