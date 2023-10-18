"""Console script for ${{ values.project_name }}."""

{%- if values.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys

{%- if values.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for ${{ values.project_name }}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "${{ values.project_name }}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
