import click
import os

# r - Used for reading generic text files
# rb - Used for reading in binary

@click.command()
@click.option("--f", help="Path of the file to get bytes count")
def count(f: str) -> None:
    # Check if the file exists
    if not checkFileExist(c):
        return
    
    # Get the byte count of the file
    with open(f, "rb") as f:
        print("Byte count: " + str(len(f.read())))

@click.command() 
@click.option("--f", help="Path of the file to get line count")
def line(f: str) -> None: 
    # Check if the file exists
    if not checkFileExist(f):
        return
    
    # Get the byte count of the file
    with open(f, "r") as f:
        for count, line in enumerate(f):
            pass
    
    print("Line count: " + str(count + 1))

@click.command()
@click.option("--f", help="Path of the file to get the word count")
def word(f: str) -> None:
    if not checkFileExist(f):
        return

    words = 0
    with open(f, "r") as f:
        # * Reads the content of the file, and stores it in another sep variable
        data = f.read()

        # * Split the data into separate lines and returning it
        lines = data.split()
        words += len(lines);

    print("Word count: " + str(words))

@click.command()
@click.option("--f", help="Path of the file to get the character count")
def char(f: str) -> None:
    if not checkFileExist(f):
        return
    
    characters = 0
    with open(f, "r", encoding='utf-8') as f:
        for line in f:

            # Increase count of char 
            characters += len(line)
        
    print("Character count: " + str(characters));



def checkFileExist(filePath: str) -> bool:
    # Check if the file exists
    if not os.path.exists(os.getcwd() + "/" + filePath):
        print("File does not exist")
        return False; 

    return True;