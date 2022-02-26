import typer

app = typer.Typer(help="Um simples conversor de temperaturas")


@app.command()
def C_to_F(temp: float):
    """
    Celsius para Fahrenheit
    """
    typer.echo(f"{round((temp * 9 / 5) + 32, 2)}°F")


@app.command()
def F_to_C(temp: float):
    """
    Fahrenheit para Celsius
    """
    typer.echo(f"{round((temp - 32) * (5 / 9), 2)}°C")


@app.command()
def C_to_K(temp: float):
    """
    Celsius para Kelvin
    """
    typer.echo(f"{round(temp + 273.15, 2)}°K")


@app.command()
def K_to_C(temp: float):
    """
    Kelvin para Celsius
    """
    typer.echo(f"{round(temp - 273.15, 2)}°C")


@app.command()
def F_to_K(temp: float):
    """
    Fahrenheit para Kelvin
    """
    typer.echo(f"{round((temp - 32) * (5 / 9) + 273.15, 2)}°K")


@app.command()
def K_to_F(temp: float):
    """
    Kelvin para Fahrenheit
    """
    typer.echo(f"{round((temp - 273.15) * (9 / 5) + 32, 2)}°F")


if __name__ == "__main__":
    app()
