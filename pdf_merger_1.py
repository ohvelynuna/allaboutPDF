from PyPDF2 import PdfMerger
import os
folder_path = input(rf"enter folder path: ").strip()

pdf_merger = PdfMerger()
list_file = os.listdir(folder_path)
list_file = [x for x in list_file if x.lower().endswith('.pdf')]
print(list_file)
choice_1 = input("enter Y if you want to merge all files in list, else enter N \n[Y/N]: ")
run = True
while run:
    if choice_1.upper() == 'N':
        while run:
            try:
                remove = input("enter the file names that you don't want to merge, separated with comma if there are multiple files\n(you can copy the listed file names directly, funciton will strip ' and space)\n> ")
                print(remove.split(','))
                for fname in remove.split(','):
                    fname = fname.strip(" '")
                    if fname.lower().endswith('.pdf'):
                        list_file.remove(fname)
                        print("removed " + fname + " from merge list")
                    else:
                        for x in list_file:
                            if x.startswith(fname):
                                list_file.remove(x)
                        print("removed " + x + " from merge list")
                run = False
                break
            except:
                print('please try again')
    elif choice_1.upper() == 'Y':
        run = False
        break
    else:
        print('try again, Y/N')
        choice_1 = input("enter Y if you want to merge all files in list, else enter N \n[Y/N]: ")
for filename in list_file:
    if filename.lower().endswith('.pdf'):
        print(filename)
        pdf_path = os.path.join(folder_path, filename)
        pdf_merger.append(pdf_path)
filename_merged = input('enter your desired filename for the merged file \n> ')
pdf_merger.write(os.path.join(folder_path, filename_merged))
print("file merged")
pdf_merger.close()