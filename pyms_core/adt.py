from itertools import chain

CLS_TYPE     = 0
CLS_ATTRIBS  = 1

ATT_NAME     = 0
ATT_TYPE     = 1
ATT_ITEM     = 2



class ShemaParser():
    def __init__(self, adt_class):
        self.shema = Adt._get_derivation_chain(adt_class)
        
    @property    
    def Attributes(self):
        return chain(*[x[CLS_ATTRIBS] for x in self.shema])

    @property
    def Classes(self):
        return chain([x[CLS_TYPE] for x in self.shema])

    @property    
    def Names(self):
        return ( attribute[ATT_NAME] for attribute in self.Attributes)

    @property    
    def Types(self):
         return ( attribute[ATT_TYPE] for attribute in self.Attributes) 

    

        
#class FormatRule():
#    def __init__(self, name):
#        self.name = name
#        
#    def format_value(name, value):
#        return value
#        
#        
#
#class AdtPrinter():
#    def __init__(self, adt_class, shema_parser = None):
#        if shema_parser is None:
#            shema_parser = ShemaParser(adt_class)
#        self.shema_parser = shema_parser
#        
#
#    def add_rule()



class Adt():
    def __init__(self):     
        parser = ShemaParser(self.__class__)
        for attribute in parser.Attributes:
            val = None           
            if attribute[ATT_TYPE] == AdtCollection:
                #if Adt collection => instantiate
                val = attribute[ATT_TYPE](attribute[ATT_ITEM])
            setattr(self, attribute[ATT_NAME], val)
                
    def get_shema(self):
        return  Adt._get_derivation_chain(self.__class__)
        
#    def get_shema(self):
#        if flat:
#            return (flat for shema_element in shema \
#                         for flat in shema_element[CLS_ATTRIBS])
        
    
        
    def _get_derivation_chain(cls):
        chain = []
        if cls != Adt:         
            chain = [(cls, cls.Schema)]        
            # Recursive: preprend schemas for all superclasses and                 
            for pcls in cls.__bases__:
                chain = Adt._get_derivation_chain(pcls) + chain    
        return chain
    
    
    
    
class AdtCollection():
    def __init__(self, item_template):
        pass

