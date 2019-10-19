def reader(filename):
    n = 0
    file_Object = open(filename,'r')
    while n <10:
      my_str =  file_Object.readline()
      n += 1
    file_Object.close()
    return my_str

if __name__ == "__main__":
    print(reader('helloworld.txt'))
