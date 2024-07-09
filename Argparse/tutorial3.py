from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('square', help='squares a given number', type=int)
parser.add_argument('-v', '--verbose', help='Provide a verbose description', action='store_true',required=True) # required for the verbose flag to be used compulsory

args: Namespace = parser.parse_args()

if args.verbose:
    print(f'The square of {args.square} is {args.square**2}')
else:
    print(args.square**2)