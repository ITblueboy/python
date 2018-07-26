# coding:utf-8
class AddrBookEntry(object):
    def __init__(self, name, phone):
        self.Name = name
        self.Phone = phone


class AddrBook(object):
    def __init__(self, title):
        self.data = []
        self.title = title

    def Add(self, entry):
        self.data.append(entry)

    def Show(self):
        print self.title
        for entry in self.data:
            print entry.Name + '\t' + entry.Phone


addr_book = AddrBook('Skye addr book')
addr_book.Add(AddrBookEntry('tangzhong', '10086'))
addr_book.Add(AddrBookEntry('litao', '1008611'))
addr_book.Show()
