import argparse
from text_parser import TextParser


def positive_integer(value: int) -> int:
    ivalue = int(value)

    if ivalue < 1:
        raise argparse.ArgumentTypeError(
            f"{value} is invalid. Value must be positive integer.")

    return ivalue


def init_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n", type=positive_integer, help="'n' for n-gram. n > 0. Default: %(default)s", default=4)

    parser.add_argument(
        "--k", type=positive_integer,  help="top sort of k n-grams. k > 0. Default: %(default)s", default=10)

    parser.add_argument("--input", type=str,
                        help="input file name. Default: %(default)s", default="input.txt")

    return parser


def main():
    parser = init_args_parser()
    args = parser.parse_args()

    tp = TextParser(args.n, args.k, args.input)
    tp.print_statistics()


main()
