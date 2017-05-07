# python code for Longest Increasing Sequence

mylist = [10, 9, 2, 5, 3, 7, 101, 18, 19]

def find_LIS(ip_list = mylist):
    print('mylist: ', mylist)
    curr = None
    lenlist = len(mylist)
    
    for idx in range(lenlist):
        seq = []
        start = mylist[idx]
        curr = start
        prev = None
        seq.append(curr)
        # print(curr)
        length = 1
        for jdx in range(idx+1, len(mylist)):
            next = mylist[jdx]
            if curr<next:
                seq.append(next)
                prev = curr
                curr = next
                length += 1
            else:
                pass
        print('start: {}, seq: {}, length: {}'.format(start,seq,length))

    









if __name__ == '__main__':
    find_LIS()

