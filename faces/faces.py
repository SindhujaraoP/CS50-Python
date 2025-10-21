def main():
    command = input("Give an input ")
    print(convert(command))

def convert(n):
    return n.replace(':)','🙂').replace(':(','🙁')

main()
