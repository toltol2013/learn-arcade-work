class Dog():
    def __init__(self):
        """ Constructor """
        self.name = ""
        print("A new dog is born!")


def main():
    # This creates the dog
    my_dog = Dog()
    print(f"The dog's name is: {my_dog.name}")


main()
