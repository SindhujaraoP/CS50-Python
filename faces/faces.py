def main():
    command = input("Give an input ")
    convert(command)

def convert(str):
    return str.replace(':)','🙂').replace(':(','🙁')

main()
