"""Console script for ${{ cookiecutter.project_name }}."""

{%- if cookiecutter.command_line_interface == 'argparse' %}
import argparse
{%- endif %}
import sys

{%- if cookiecutter.command_line_interface == 'argparse' %}
def main():
    """Console script for ${{ cookiecutter.project_name }}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "${{ cookiecutter.project_name }}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
