from Console import Console
from Error import Error

def main():
    console = Console.Console()
    console.printLine()
    error = Error.Error()
    error.printLine()

if __name__ == '__main__':
    main()
