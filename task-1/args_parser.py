"""Wrapper for argparse"""
import argparse


def positive_integer(value: int) -> int:
    """Type positive integer value for argparse"""
    ivalue = int(value)

    if ivalue < 1:
        raise argparse.ArgumentTypeError(
            f"{value} is invalid. Value must be positive integer.")

    return ivalue


def init_args_parser():
    """Return parser with added arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n", type=positive_integer, help="'n' for n-gram. n > 0. Default: %(default)s", default=4)

    parser.add_argument(
        "--k", type=positive_integer,  help="top sort of k n-grams. k > 0. Default: %(default)s", default=10)

    parser.add_argument("--input", type=str,
                        help="input file name. Default: %(default)s", default="input.txt")

    return parser
