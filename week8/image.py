import matplotlib.image as im
import csv
I=im.imread("/home/p/Downloads/WhatsApp Image 2024-03-08 at 4.35.48 PM.jpeg")
r=I[::1]
b=I[::2]
g=I[::3]
redOutputFile = open('red.csv',"w")
greenOutputFile = open('green.csv',"w")
blueOutputFile = open('blue.csv',)
csv.writer(redOutputFile,r)
csv.writer(greenOutputFile, g)
csv.writer(blueOutputFile, b)
