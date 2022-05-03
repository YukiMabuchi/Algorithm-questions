#https://gist.github.com/ilivessevili/8338697d75a26240b20e
#下のほうがいい
#https://www.bswen.com/2018/04/python-How-to-generate-random-large-file-using-python.html

# import os

# #３回かけるとMBのサイズになる
# MB1 = 1024*1024*1024
# with open('large_file', 'wb') as fout:
#     fout.write(os.urandom(MB1)) 

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


#   import os 
#     with open('%s'%filename, 'wb') as fout:
#         fout.write(os.urandom(size)) #1
#     print ('big random binary file with size %f generated ok'%size)
#     pass

    # print ('big random binary file with size %f generated ok'%int(file_size_hex, 16))

