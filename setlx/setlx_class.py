class SetlXClass(object):

    def __str__(self):
        try:
            return self.f_str()
        except NameError:
            return super().__str__()

    def __hash__(self):
        return 0

    def __eq__(self,other):
        self_vars = [v for v in self.__dict__.values() if not callable(v)]
        other_vars = [v for v in other.__dict__.values() if not callable(v)]
        return self_vars == other_vars