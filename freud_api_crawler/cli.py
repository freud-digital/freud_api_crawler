"""Console script for freud_api_crawler."""
import sys
import click

from . import freud_api_crawler as frd


@click.command()
@click.argument('user', envvar='FRD_USER')
@click.argument('pw', envvar='FRD_PW')
@click.option('-m', default='a10e8c78-adad-4ca2-bfcb-b51bedcd7b58', show_default=True)
def cli(user, pw, m):
    """Console script for freud_api_crawler."""
    frd_manifestation = frd.FrdManifestation(
        user=user,
        pw=pw,
        manifestation_id=m
    )
    xml = frd_manifestation.make_xml()
    click.echo(
        click.style(
            f"processed Manifestation\n###\n {frd_manifestation.md__title}\
            {frd_manifestation.manifestation_id}\n###", fg='green'
        )
    )
