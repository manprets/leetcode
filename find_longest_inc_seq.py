# python code for Longest Increasing Sequence

mylist = [10, 9, 2, 5, 3, 7, 101, 18, 19]

def find_LIS(ip_list = mylist):
    print('mylist: ', mylist)
    curr = None
    lenlist = len(mylist)
    max_lengths=[1]*lenlist

    for idx in range(lenlist):
        curr = mylist[idx]
        for jdx in range(idx):
            prev = mylist[jdx]
            if prev<curr and max_lengths[idx]<max_lengths[jdx]+1:
                max_lengths[idx] += 1
            else:
                pass
        print('lengths: {}'.format(max_lengths))

    









if __name__ == '__main__':
    find_LIS()

