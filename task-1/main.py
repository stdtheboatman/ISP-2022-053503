import argparse
from text_parser import TextParser


def init_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n", type=int, help="'n' for n-gram. Default: %(default)s", default=4, choices=range(1, 100))

    parser.add_argument(
        "--k", type=int,  help="top sort of k n-grams. Default: %(default)s", default=10, choices=range(1, 10**6))

    parser.add_argument("--input", type=str,
                        help="input file name. Default: %(default)s", default="input.txt")

    return parser


def main():
    parser = init_args_parser()
    args = parser.parse_args()

    tp = TextParser(args.n, args.k, args.input)
    tp.print_statistics()


main()
