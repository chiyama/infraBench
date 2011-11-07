# coding: utf-8

import time
import progressbar

class benchResult(object):
    def __init__(self):
        self.stime = time.time()
        self.etime = None

        self.sclock = time.clock()
        self.eclock = None


    def finish(self):
        self.etime = time.time()
        self.eclock = time.clock()


    def getResult(self):
        return (self.etime - self.stime, self.eclok - self.sclock)


    def __repr__(self):
        return "%.3f - %.3f ( %.3f s ), %.3f - %.3f ( %.3f cycle )" % (
            self.etime,
            self.stime,
            self.etime - self.stime,
            self.eclock,
            self.sclock,
            self.eclock - self.sclock)


    def __str__(self):
        return self.__repr__()


def generateFile(path, size):
    ret = 0

    data = '0xDEADBEEF'
    s = len(data)+4

    widgets = ['generateFile(' + path + '): ', progressbar.Percentage(), progressbar.Bar()]

    fp = open(path, 'w')

    if size != 0:
        pbar = progressbar.ProgressBar(maxval=size, widgets=widgets).start()
        for i in range(size / s):
            fp.write('%s%04d' % (data, i%1000))
            ret += s
            pbar.update(ret)

        fp.write((data+('%04d' % (size/s)))[:(size-ret)])
        ret += size-ret
        pbar.update(ret)

        pbar.finish()

    fp.close()

    return ret


class moduleBase(object):
    def preProcess(self, args, values):
        return values


    def process(self, args, values):
        return values


    def postProcess(self, args, values):
        return values
