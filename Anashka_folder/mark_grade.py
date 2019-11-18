name = input("Enter your name :")
mark = int(input("Enter your mark : "))

if mark>90:
    print("{} got A grade".format(name))
elif mark>80:
    print("{} got B grade".format(name))
elif mark>70:
    print("{} got C grade".format(name))
else:
    print("{} got D grade".format(name))