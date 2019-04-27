class SetlXClass(object):
    
    def __str__(self):
        try:
            return self.f_str()
        except NameError:
            return super().__str__()