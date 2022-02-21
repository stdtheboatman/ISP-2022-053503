"""
scirpt for text analysis

optional arguments:
  -h, --help     show this help message and exit
"""

from text_parser import TextParser
from args_parser import init_args_parser


def main():
    """Parse aguments and print statisctics from TextParser"""
    parser = init_args_parser()
    args = parser.parse_args()

    tp = TextParser(args.n, args.k, args.input)
    tp.print_statistics()


if __name__ == '__main__':
    """Entry point for start application"""
    main()
