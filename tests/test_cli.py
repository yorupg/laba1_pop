from typer.testing import CliRunner

from toolkit.__main__ import app
from toolkit.errors import NO_NUMBERS, NO_SIGNS

runner = CliRunner()


def test_calc_success():
    result = runner.invoke(app, ["calc", "2 + 2"])

    assert result.exit_code == 0
    assert result.stdout.strip() == "4.0"


def test_calc_no_numbers():
    result = runner.invoke(app, ["calc", "+-+"])

    assert result.exit_code == 2
    assert result.stderr.strip() == NO_NUMBERS


def test_calc_no_signs():
    result = runner.invoke(app, ["calc", "123"])

    assert result.exit_code == 2
    assert result.stderr.strip() == NO_SIGNS


def test_convert_success():
    result = runner.invoke(
        app,
        ["convert", "10", "--from", "km", "--to", "m"],
    )

    assert result.exit_code == 0
    assert result.stdout.strip() == "10000.0 m"


def test_convert_missing_to():
    result = runner.invoke(
        app,
        ["convert", "10", "--from", "km"],
    )

    assert result.exit_code == 2