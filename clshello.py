class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = " world"

class Hello(Greeting):
    def say_hello(self):
        print(self.msg + self.target)

hello = Hello()
hello.say_hello()
