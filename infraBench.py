# coding: utf-8

import re
import os

class infraBench(object):
    def __init__(self):
        self.engines = []
        self.values = []


    def loadConfig(self, file):
        for line in open(file, 'r').readlines():
            line = line.strip()
            print line

            m = re.match('(\w+)\s*\(\s*([^\)]*)\)', line)
            if m == None:
                continue

            args = {}
            name = m.group(1)
            exec('from modules import ' + name)
            module = eval('%(name)s.%(name)s()' % {'name' : name})
            for arg in re.split('\s*,\s*', m.group(2)):
                k,v = re.split('\s*=\s*', arg)

                args[k] = eval(v)

            self.engines.append({
                    'command' : line,
                    'module'  : module,
                    'args'    : args
                    })


    def _process(self, name, values):
        for engine in self.engines:
            values.append('%s : %s' % (name, engine['command']))

            f = eval('engine["module"].'+name)
            values = f(engine['args'], values)

        return values


    def run(self):
        values = []
        for p in ['preProcess', 'process', 'postProcess']:
            values = self._process(p,values)

        for value in values:
            print value


if __name__ == '__main__':
    ib = infraBench()
    ib.loadConfig(os.path.join(os.path.dirname(__file__), 'config.txt'))
    ib.run()
