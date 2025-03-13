import click
from cli.nl import nl
from cli.tail import tail
from cli.wc import wc


@click.group()
def cli():
    pass


cli.add_command(nl)
cli.add_command(tail)
cli.add_command(wc)

if __name__ == "__main__":
    cli()
