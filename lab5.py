class CallDetail:
    def __init__(self,sendphnumber,tophnumber,duration,calltype):
        self.sendphnumber=sendphnumber
        self.tophnumber=tophnumber
        self.duration=duration
        self.calltype=calltype


class Util:
    def __init__(self):
        self.list_of_call_objects=[]


    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            self.list_of_call_objects.append(CallDetail(i[0],i[1],i[2],i[3]))

    def printlistofobjects(self):
        for i in self.list_of_call_objects:
            print(i.sendphnumber,i.tophnumber,i.duration,i.calltype)
           

call='9990000001','9330000001',23,'STD'
call2='9990000001','9330000001',54,'Local'
call3='9990000001','9330000003',6,'ISD'

list_of_call_string=[call,call2,call3]
x=Util()
x.parse_customer(list_of_call_string)
x.printlistofobjects()
