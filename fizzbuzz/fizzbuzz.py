import click
import sys


def is_positive_integer(n):
    """Returns True if n is a positive integer"""
    return n>0


def process(n):
    """Returns the string representation of integer n unless:
       - n is evenly divisible by 3 (returns 'Fizz')
       - n is evenly divisible by 5 (returns 'Buzz')
       - n is evenly divisible by both 3 and 5 (returns 'FizzBuzz')"""
    outString = ""
    if n%3==0:
        outString+="Fizz"
    if n%5==0:
        outString+="Buzz"
    if outString=="":
        outString = str(n)
    return outString


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(n):

    # Validate input
    if not is_positive_integer(n):
        print("the value of n must be a positive, non-zero integer")
        sys.exit()

    # Iterate from 1 to n inclusive and print FizzBuzz
    for i in range(1, n+1):
        print(process(i))


if __name__ == '__main__':
    main()
