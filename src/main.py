from visual import main_dialog


def main():
    main_dialog.run_windows()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()