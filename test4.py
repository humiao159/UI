import sys
print(sys.argv)
input_list=sys.argv

if "ui" in input_list:
    a=input_list.remove("ui")
    print(a)
