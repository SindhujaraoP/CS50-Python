def main():
    type = input("File name: ").strip().lower().split(".")[-1]
    ext(type)

def ext(n):
    if n == 'gif' or n ==  'jpg' or n == 'jpeg' or n == 'png':
        print("image/"+n)
    elif n == 'pdf' or n == 'zip':
        print("application/"+n)
    elif n == 'txt':
        print("text/plain")
    else:
        print("application/octet-stream")


main()


