class Student(object):

    def __init__(self, surname, forename, Id, modlist=[]):
        self.surname = surname
        self.forename = forename
        self.Id = Id
        self.modlist = modlist
        
    def add_module(self, b):
        self.modlist.append(b)
        
    def del_module(self, b):
        if b in self.modlist:
            self.modlist.remove(b)
        
    def print_details(self):
        print('ID: {}'.format(self.Id))
        print('Surname: {}'.format(self.surname))
        print('Forename: {}'.format(self.forename))
        print('Modules: {}'.format(' '.join(self.modlist)))
        

def main():

    student1 = Student('Murphy', 'Jimmy', 15234654)
    student1.add_module('CA117')
    student1.add_module('CA116')
    student1.add_module('CA114')
    student1.print_details()
    
    student2 = Student('Lannister', 'Cersei', 15876123, ['CA115', 'CA216'])
    student2.del_module('CA216')
    student2.del_module('CA117')
    student2.del_module('CA216')
    student2.add_module('CA117')
    student2.print_details()

if __name__ == '__main__':
    main()