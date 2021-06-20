def file_copy(src, dest):
    with open(str) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("untitiled0.py", "copy_untitiled0.py")
        with open('copy_untitiled0.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end='')
