class Server:
    def __init__(self, name):
        self.name = name
        self.instances = {}

    def __repr__(self):
        return self.name

    def GetInstances(self):
        def comp(instanceA, instanceB):
            return cmp(instanceA[1], instanceB[1])
        result = self.instances.items()
        result.sort(cmp=comp)
        return result

    def AddInstance(self, name):
        if name in self.instances:
            raise KeyError
        self.instances[name] = 0
        pass

    def RemoveInstance(self, name):
        if name not in self.instances:
            raise KeyError
        del(self.instances[name]) 

    def UpdateInscanceLoad(self, name, load):
        if name not in self.instances:
            raise KeyError
        self.instances[name] = load

    def CalcLoad(self):
        return sum(self.instances.values())

    def HasInstance(self, name):
        return name in self.instances
