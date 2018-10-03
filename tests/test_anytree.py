from anytree import NodeMixin, RenderTree

class MyClass(NodeMixin):
    def __init__(self, name, start, end, parent = None):
        super(MyClass, self).__init__()
        self.name = name
        self.start = start
        self.end = end
        self.parent = parent

    def __repr__(self):
        return f"({self.end-self.start:.2f}) - {self.name}"
def main():
    a = MyClass(start=1, end=2, name='one')
    b = MyClass(start = 3, end = 4, name='two', parent=a)
    print(RenderTree(a))

if __name__ == '__main__':
    main()