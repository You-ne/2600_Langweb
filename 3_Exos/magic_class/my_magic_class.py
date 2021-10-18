class   Dummy:
    
    list = None

    def __init__(self, *args, **kwargs):

        # Set desc = instance magic if desc is not a keyword arg
        if 'desc' in kwargs.keys():
            self.desc = kwargs['desc']
        else:
            self.desc = "instance magic"

        # Put keywords args in instance attributes
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
        # Put positionnals args in list to be used as a... list
        if args:
            self.list = args
        
    # Magic functions to use Dummy obj as list
    def __setitem__(self, i, item):
        self.list[i] = item
    def __getitem__(self, i):
        return self.list[i]