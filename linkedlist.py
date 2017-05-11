class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class List:
    def __init__(self):
        self.head = Node(0);
        self.current = self.head;
        self.last = self.current;

    def push(self, d):
        self.last.next = d;
        self.last = d;

    def traverse(self):
        c = 1;
        while self.current != None:
            print "Element " + str(c) + ":" + str(self.current.data) + "\n";
            self.current = self.current.next;
            c += 1;


l = List();
l.push(Node(2));
l.push(Node(3));
l.push(Node(4));
l.push(Node(5));
l.traverse();
