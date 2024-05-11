from Maintenance import clean


for out in clean.clean_prefetch():
    print(out.filepath)
    print(out.message)