class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'
    def parent_method(self):
        print('Back in my day...')
# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.child_attribute = 'I am a child'
# Create instance of child
child = Child()
# Show attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()

class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = 'I am a parent'


# Create instance of child
child = Child()

# Show attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()


class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(B, C):
    pass


d = D()
d.x()
print(D.mro())

# Output
# x: B
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]



class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)