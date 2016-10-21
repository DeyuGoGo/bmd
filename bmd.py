import os
import argparse
import sys
baseSWSzie = 300

parser = argparse.ArgumentParser(description='Oh Deyu.')
parser.add_argument('-p','--path', help='app path name',required=True)
args = parser.parse_args()
path = str(args.path);
if not os.path.exists(path+'src/main/res/values'):
    print('Make sure you -p your moudle path')
    sys.exit()
for i in range(1, 20, +1):
    multiple = 1 + (i/10);
    swString = str(int(round(baseSWSzie * multiple)))
    if not os.path.exists(path+'src/main/res/values-sw'+ swString +'dp'):
        os.makedirs(path+'src/main/res/values-sw'+swString+'dp')
    os.system('python3 build.py -i '+path+'src/main/res/values/dimens.xml -o '+path+'src/main/res/values-sw'+swString+'dp'+'/dimens.xml -n '+str(multiple))

    
