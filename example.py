def count():
    num = 0
    def incrementer():
        nonlocal num
        num += 2
        return num
    return incrementer
        

count()