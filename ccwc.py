import click
import crud
from click_default_group import DefaultGroup


@click.group(cls=DefaultGroup, default='default', default_if_no_args=True)
def cli() -> None:
    pass

cli.add_command(crud.count)
cli.add_command(crud.line)
cli.add_command(crud.word)
cli.add_command(crud.char)

@cli.command()
@click.argument('file')
def default(file: str) -> None:
    if not crud.checkFileExist(file):
        return
    
    byteCount = 0
    wordCount = 0;
    
    # Else return all Bytes, Line, Words 
    with open(file, "r") as f:
        for count, line in enumerate(f):
            byteCount += len(line)
            words = line.split()
            wordCount += len(words)    
        

    print("Byte count: " + str(byteCount) + "\n")
    print("Line count: " + str(count + 1) + "\n")
    print("Word count: " + str(wordCount) + "\n")

