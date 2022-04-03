import sys

n = int(sys.argv[1])

if n == 10:
	f = open("/home/training/HW/result/ten_strings.txt", "w")

elif n == 100:
	f = open("/home/training/HW/result/hundred_strings.txt", "w")

elif n == 1000:
	f = open("/home/training/HW/result/thousand_strings.txt", "w")

for i in range(1, n+1):
	f.write("%d\n"%i)

f.close()


