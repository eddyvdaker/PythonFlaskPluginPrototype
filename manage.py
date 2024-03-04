from src.cli import cli

if __name__ == "__main__":
    cli()
else:
    from src.app import create_app
    app = create_app()
