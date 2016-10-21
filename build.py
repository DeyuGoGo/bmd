import argparse

parser = argparse.ArgumentParser(description='Oh Deyu.')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
parser.add_argument('-n','--number',help='numer', required=True)
args = parser.parse_args()
target = open(args.output, 'w')
with open(args.input) as fp:
    for line in fp:
        if line.strip()==0:
            target.write(line)
            continue
        b = (line.find(">",0,len(line)-4))
        if b == -1:
            target.write(line)
            continue
        # print (len(line))
        for i in range(2, 10, +1):
            numString = (line[b+1:b-len(line)+i])
            # print (numString)
            if numString.isnumeric() == 0:
                break
        if(i==2):
            target.write(line)
        else:
            a = line[:b-len(line)+1] + str(int(int(numString[:-1])*float(args.number))) + line[b+i-1:]
            target.write(a)
        # print (line)
target.close()
