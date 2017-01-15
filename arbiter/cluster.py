from server import Server
class Cluster:
    def __init__(self):
        self.servers = set()
        self.warn_level = 6

    def GetServers(self):
        def comp(serverA, serverB):
            return cmp(serverA.CalcLoad(), serverB.CalcLoad())
        result = list(self.servers)
        result.sort(cmp=comp)
        return result

    def AddServer(self, server):
        if server in self.servers:
            raise KeyError
        self.servers.add(server)

    def GetWarningServers(self):
        return filter(lambda x: x.CalcLoad()>self.warn_level, self.GetServers())
