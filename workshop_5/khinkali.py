
herbs = 1000

def make_khinkali(is_kalakuri = False):
    global herbs

    print("Prepare Dough")
    print("Prepare meat")
    if is_kalakuri:
        herbs -= 1
        print(f"Add herbs to meat ({herbs})")
    print("Place meat on dough")
    print("Wrap")
    

# for i in range(50):
make_khinkali()
make_khinkali(False)


