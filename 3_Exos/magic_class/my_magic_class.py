class   Dummy:
    
    list = []

    def __init__(self, *args, **kwargs):
        
        # Set desc = instance magic by default
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
    def __len__(self):
        return len(self.list)