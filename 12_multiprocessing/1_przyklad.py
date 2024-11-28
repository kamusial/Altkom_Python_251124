import multiprocessing as mp
import time


def worker(name):
    print('Worker {} started'.format(name))
    time.sleep(2)
    print('Worker {} finished'.format(name))

if __name__ == '__main__':
    process1 = mp.Process(target=worker, args=('A'))
    process2 = mp.Process(target=worker, args=('B'))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Done')