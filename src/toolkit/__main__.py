import typer

from toolkit.calculator import calculator
from toolkit.converter import converter
from toolkit.errors import INPUT_ERROR, NO_NUMBERS, NO_SIGNS

app = typer.Typer()

@app.command(context_settings={"ignore_unknown_options": True})
def calc(expr: str = typer.Argument(..., help="введите арифметическое выражение")):
    result = calculator(expr)
    if result == -1:
        typer.echo(NO_NUMBERS, err=True)
        raise typer.Exit(code=2)

    elif result == -2:
        typer.echo(NO_SIGNS, err=True)
        raise typer.Exit(code=2)
    
    elif result == -3:
            typer.echo(INPUT_ERROR, err=True)
            raise typer.Exit(code=2)

    else:
        print(result)

@app.command(context_settings={"ignore_unknown_options": True})
def convert(
    value: float = typer.Argument(..., help="введите значение, которое хотите конвертировать"),
                                                         # если подавать отрицательное число, то будет ошибка, тк это будет восприниматься опцией.
                                                         # value: int = typer.Option(..., "--value", help="значение") так бы работало, но нарушало условие задания
                                                         # тк  ввод требует именно python -m toolkit convert, а не python -m toolkit convert --value
                                                         # прописала @app.command(context_settings={"ignore_unknown_options": True}), 
                                                         # чтобы эта ошибка игнорировалась 
    from_: str = typer.Option(..., "--from", help="введите исходную единицу"),
    to: str = typer.Option(..., "--to", help="введите целевую единицу")):
    result = converter([value, from_, to])
    errors = {
        "неверное числовое значение",
        "ниже абсолютного нуля",
        "данный тип не поддерживается",
        "ошибка, введено недостаточно данных",
    }
    if result in errors:
        typer.echo(result, err=True)
        raise typer.Exit(code=2)
    
    print(result)


if __name__ == "__main__":
    app()
