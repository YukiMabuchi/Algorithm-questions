file_size_MB = int(input('Plese enter the size of the file(MB) : '))
 
def generate_file(filename, size_MB):
    import os
    
    #MB to byte
    size_b = size_MB*1024*1024*1024

    #to hex
    file_size_hex = format(size_b, 'x') 

    with open(filename, 'wb') as f:
        f.write(os.urandom(int(file_size_hex, 16)))

if __name__ == '__main__':
    generate_file("test_file", file_size_MB)
