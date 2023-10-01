from just_count import square
import click

@click.command()
@click.option(
    "-n",
    "--number",
    default=5,
    type = float,
    help="Number to square.",
    show_default=True,  # show default in help
)
@click.option(
    "-sr",
    "--square_root/--square",
    is_flag = True,
    help = "Calculate the square root instead"
)
def main(number, square_root):
    if square_root:
        print(f"The square root of {number} is {square.square_root(number)}")
    else:
        print(f"The square of {number} is {square.square(number)}")

if __name__ == '__main__':
    main()