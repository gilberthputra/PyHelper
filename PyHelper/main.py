import argparse
import PyHelper

def main():
    # Map command names to functions
    commands = {
        'create_ml_dir': PyHelper.create_ml_dir,
    }

    parser = argparse.ArgumentParser()

    # Add a positional argument for the command name
    parser.add_argument('command', choices=commands.keys())

    # Add an optional argument for the command parameter
    parser.add_argument('param', nargs='?')

    args = parser.parse_args()

    # Call the function associated with the chosen command
    if args.param:
        commands[args.command](args.param)
    else:
        commands[args.command]()

if __name__ == "__main__":
    main()