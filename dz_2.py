import os
 
def print_docs(directory):
	all_files = os.walk(directory)
	for catalog in all_files:
            print(f'Папка {catalog[0]} содержит:')
            dir_1=[i for i in catalog[1]]
            print(f'Директории: {", ".join(dir_1)}')
            dir_2=[i for i in catalog[2]]
            print(f'Файлы: {", ".join(dir_2)}')       
print_docs("C:/Users/k13st/Desktop/Работа с прицепами")

