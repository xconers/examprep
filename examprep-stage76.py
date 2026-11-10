# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ExamPrep
def handle_keyboard_interrupt():
    import sys

    if 'app' in dir():
        app.shutdown()
        sys.exit(0)
    elif 'cli' in dir() and callable(getattr(cli, 'exit', None)):
        cli.exit(0)
    else:
        print()
        print('Interrupted. See you next time.')
        sys.exit(0)

def main():
    try:
        handle_keyboard_interrupt()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()

if __name__ == '__main__':
    main()
