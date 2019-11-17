class ArgumentsDemo(object):
    def print_it(self, *args):
        print(args)

    def do(self):
        a_list = [1, 'python', 'helloworld', 'test']
        self.print_it(*a_list)
        self.print_it(a_list)
        self.print_it([1, 'python', 'helloworld', 'test'])

        a_tuple = (2, 'python', 'helloworld', 'test')
        self.print_it(*a_tuple)
        self.print_it(a_tuple)
        self.print_it(2, 'python', 'helloworld', 'test')

