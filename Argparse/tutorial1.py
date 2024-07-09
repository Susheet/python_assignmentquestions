from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('echo', help='echo the string you use here')

args: Namespace = parser.parse_args()

print(args)

print(args.echo)