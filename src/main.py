import typer

from src.power import power_function
from src.constants import SAMPLE_CONSTANT

app = typer.Typer()


@app.command()
def main(name: str = typer.Argument(..., help="QWEKQWEOPQWKE")):
    power_function(1, 2)
    print(f'Hello {name}')
    

if __name__ == "__main__":
    app()
