import click


@click.command()
@click.argument("filename", required=False)
def nl(filename):
    cnt = 1
    if filename:
        with open(filename, "r") as file:
            while True:
                try:
                    line = file.readline()
                    if not line:
                        break
                    # терминал (bash, zsh) добавляет автоформатирование,
                    # поэтому число пробелов в строчке ниже считаю некритичным
                    print(f"    {cnt}  {line}")
                    cnt += 1
                except EOFError:
                    break
    else:
        while True:
            try:
                line = input()
                print(f"    {cnt}  {line}")
                cnt += 1
            except EOFError:
                break
