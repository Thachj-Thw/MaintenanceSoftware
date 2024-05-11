from Maintenance import clean


for f in clean.clean_temp():
    print(f.filepath, f.size, f.message)