#!/usr/bin/env python
from pprint import pprint
import time
import sys
from cluster import Cluster
from server import Server

def sum_server(server):
    return sum(server.values())

def instance_sort_cmp(instanceA, instanceB):
    return cmp(instanceA[1], instanceB[1])

def server_sort_cmp(serverA, serverB):
    return cmp(sum_server(serverA[1]), sum_server(serverB[1]))

def make_list(elements, comparator):
    result_list = list(elements.items())
    result_list.sort(cmp=comparator)
    return result_list
    

a = Server('server1')
b = Server('server2')
c = Server('server3')

s = Cluster()
print(a, a.CalcLoad())
print(a)
a.AddInstance("tomcat4")
a.AddInstance("tomcat1")
a.AddInstance("tomcat2")
a.AddInstance("tomcat3")
a.UpdateInscanceLoad("tomcat1", 2)
a.UpdateInscanceLoad("tomcat2", 4)
a.UpdateInscanceLoad("tomcat3", 1)
a.UpdateInscanceLoad("tomcat4", 7)

b.AddInstance("tomcat2")
b.UpdateInscanceLoad("tomcat2", 5)

a.RemoveInstance("tomcat2")

s.AddServer(a)
s.AddServer(b)
s.AddServer(c)
print("**********")
for i in s.GetServers():
    print(i, i.GetInstances())
    #print(i, i.CalcLoad())


bad_count = 0
bad = False
while s.GetWarningServers():
    print("Bad: ", bad_count)
    if bad:
        bad_count += 1
        bad = False
    else:
        bad_count = 0

    print("**********")
    for i in s.GetServers():
        print(i, i.GetInstances())
    print("Warn: ", s.GetWarningServers())
    for i in s.GetWarningServers():
        bad = True
        print(i,":")
        print("Instances: ", i.GetInstances())
        minimal = i.GetInstances()[0]
        print("Min: ", minimal)
        if minimal[1] > s.warn_level:
            continue
        for first_free in s.GetServers():
            print("Sprawdzam pierwszy wolny: ", first_free)
            if not first_free.HasInstance(minimal[0]):
                i.RemoveInstance(minimal[0])
                first_free.AddInstance(minimal[0])
                break

    time.sleep(1)
             
        



print("**********")
for i in s.GetServers():
    print(i, i.GetInstances())
    
sys.exit(0)
    
    

servers = {}

#servers['app1'] = {'tomcat1': 1, 'tomcat2': 4, 'tomcat5': 4}
#servers['app2'] = {'tomcat1': 1, 'tomcat3': 2}
#servers['app3'] = {}
#servers['app4'] = {'tomcat3': 6, 'tomcat5': 1}

servers['app1'] = {'tomcat1': 1, 'tomcat2': 6}
servers['app2'] = {'tomcat2': 7}



pprint(servers)

finish = False

while not finish:
    print("******")
    finish = True
    server_list = make_list(servers, server_sort_cmp)
    print("server_list")
    pprint(server_list)
    print("-")
    for i in server_list:
        if sum_server(i[1]) > 6:
            print("ten serwer ma wiecej niz 6")
            print(i[0], sum_server(i[1]))
            print("-")
            instances = make_list(i[1], instance_sort_cmp)
            print("po kalulacjach:")
            pprint(instances)
            print("-")
            first_free_found = False
            for first_free in server_list:
                print("Sprawdzam czy", first_free," jest wolny")
                print("Szukam ", instances[0][0])
                if  instances[0][0] not in first_free[1]:
                    print("jest wolny")
                    first_free_found = True
                    break
            if first_free_found:
                print("BBB", first_free)
                print("CCC", i)
                print("DDD", instances[0][0])
    
                servers[first_free[0]][instances[0][0]]= servers[i[0]].pop(instances[0][0])
                #TODO: zabieranie z obciazonego i dodawanie do wolnego.
                #Trzeba to zrobic na zrodlowym slowniku
            finish = False
            break
    time.sleep(1)

pprint(servers)
