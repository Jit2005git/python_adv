with open("fileHanlding\\input.txt",  "r+") as file:  # r+ read and write mode
    content = file.read()
    print(content)
    file.write("\nHello, World! added using r+ mode")
  #not need to close the file explicitly when using with statement, it automatically closes the file after the block is executed