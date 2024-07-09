from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('square', help='squares a given number', type=int)
parser.add_argument('-v', '--verbose', help='Provide a verbose description', type=int, choices=[0,1,2])

args: Namespace = parser.parse_args()

if args.verbose == 0:
    print('option 0')
elif args.verbose == 1:
    print('option 1')
elif args.verbose == 2:
    print('option 2')


print(args.square**2)