import argparse as ar
from eventos import user, get_events

parse = ar.ArgumentParser()

comando = parse.add_subparsers(dest='comando')

add = comando.add_parser('get')
add.add_argument('usuario')

args = parse.parse_args()

if args.comando == 'get':
    n = user(args.usuario)
    print(n)
    if n:
        get_events(n)

