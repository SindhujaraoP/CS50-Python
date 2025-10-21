def main():
    command = input("Give an input ")
    convert(command)

def convert(n):
    return n.replace(':)','🙂').replace(':(','🙁')

main()
