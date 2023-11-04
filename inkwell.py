import click
import subprocess
from app.core.inkwell.secretkeygenerate import create_or_load_secret_key

@click.command()
def secretgenerate():
	"""
	Command to generate a secret key for a given application
	"""
	generate = create_or_load_secret_key()
	# click.echo("Generating secret key for application: " + generate)


@click.group()
def cli():
	pass

cli.add_command(secretgenerate)


if __name__ == "__main__":
	cli()