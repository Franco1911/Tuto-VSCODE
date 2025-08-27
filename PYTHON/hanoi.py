def resultHanoi(disk, source, middle, destination):
    if disk >= 1:
        resultHanoi(disk-1, source, destination, middle)
        print("Mover disco de Torre", source, "a", destination)
        resultHanoi(disk-1, middle, source, destination)
resultHanoi(3,1,2,3)