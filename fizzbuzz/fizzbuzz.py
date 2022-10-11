"""it's fizzbuzz, what do you expect"""
import sys
import click


def is_positive_integer(number):
    """Returns True if n is a positive integer"""
    return number>0


def process(number):
    """Returns the string representation of integer n unless:
       - n is evenly divisible by 3 (returns 'Fizz')
       - n is evenly divisible by 5 (returns 'Buzz')
       - n is evenly divisible by both 3 and 5 (returns 'FizzBuzz')"""
    out_string = ""
    if number%3==0:
        out_string+="Fizz"
    if number%5==0:
        out_string+="Buzz"
    if out_string=="":
        out_string = str(number)
    return out_string


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(number):
    """it's the main function, what do you expect?"""
    # Validate input
    if not is_positive_integer(number):
        print("the value of n must be a positive, non-zero integer")
        sys.exit()

    # Iterate from 1 to n inclusive and print FizzBuzz
    for i in range(1, number+1):
        print(process(i))


if __name__ == '__main__':
    main(15)
