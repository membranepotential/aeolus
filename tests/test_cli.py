from typer.testing import CliRunner

from aeolus import AeolusContext
from aeolus.cli.cli import read_configs, app, ctx


def test_read_context(context):
    json = context.as_json()
    config = read_configs([], [json])
    assert AeolusContext.from_config(config)


def test_cli(context):
    json = context.as_json()

    @app.command()
    def test():
        assert ctx.job.id == context.job.id

    runner = CliRunner()
    runner.invoke(app, ["-j", json, "test"], catch_exceptions=True)
    runner.invoke(app, ["test", "-j", json], catch_exceptions=True)
