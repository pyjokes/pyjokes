import os
import argparse
from pyjokes import pyjokes


def create_argparser():
    parser = argparse.ArgumentParser(
        description='One line jokes for programmers (jokes as a service)'
    )

    parser.add_argument(
        '-c', '--category',
        dest='category',
        choices=['neutral', 'chuck', 'all', 'twister'],
        default='neutral',
        help='Joke category.'
    )

    parser.add_argument(
        '-l', '--language',
        dest='language',
        choices=['en', 'de', 'es', 'gl', 'eu', 'it'],
        default='en',
        help='Joke language.'
    )

    return parser


def main():
    parser = create_argparser()

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as exc:
        print('Error parsing arguments.')
        parser.error(str(exc.message))
        exit(-1)

    try:
        joke = pyjokes.get_joke(language=args.language, category=args.category)
    except pyjokes.LanguageNotFoundError:
        print('No such language %s' % args.language)
        exit(-1)
    except pyjokes.CategoryNotFoundError:
        print('No such category %s' % args.category)
        exit(-1)

    print(joke)

if __name__ == '__main__':
    main()
