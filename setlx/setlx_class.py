class SetlXClass(object):

    def __str__(self):
        try:
            return self.f_str()
        except NameError:
            return super().__str__()

    def __hash__(self):
        """ when the hash of two objects are the same, python uses the __eq__ function as a fallback.
        since we cannot hash classes in a general way, we use the __eq__ function instead. In order 
        to trick python into doing this we return the value 0 for all classes.
        """
        return 0

    def __eq__(self,other):
        """ compares the members of the class that are not a function """
        self_vars = [v for v in self.__dict__.values() if not callable(v)]
        other_vars = [v for v in other.__dict__.values() if not callable(v)]
        return self_vars == other_vars