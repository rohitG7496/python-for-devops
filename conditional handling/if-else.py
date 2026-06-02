import sys

type = sys.argv[1]

if type in ["t2.micro", "t2.small"]:
    print("eligable for free tier launching instance")
elif type in ["t4g.small"]:
    print("this is graviton based instance not available in free tier")
else:
   print("instance type is not supported in free tier")