from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('square', help='squares a given number', type=int, default=0, nargs='?')
parser.add_argument('-v', '--verbose', 
                    help='Provide a verbose description. Use -vv for extra verbose', 
                    action='count',)

args: Namespace = parser.parse_args()

result: int = args.parse_args ** 2

if args.verbose == 1:
    print(f'The result is : {result}')
elif args.verbose == 2:
    print(f'The square of {args.square} is {result}')
else:
    print(result)


print(args.square**2)