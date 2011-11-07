# coding: utf-8

import os
import shutil
import moduleBase

class fileStat(moduleBase.moduleBase):
    def preProcess(self, args, values):
        if os.path.exists(args['path']):
            shutil.rmtree(args['path'])

        os.makedirs(args['path'])

        for f in range(args['count']):
            fname = os.path.join(args['path'], '%04d.txt' % f)
            moduleBase.generateFile(fname, args['size'])

        return values

                
    def process(self, args, values):
        fnames = []
        for f in range(args['count']):
            fnames.append(os.path.join(args['path'], '%04d.txt' % f))

        result = moduleBase.benchResult()
        for f in fnames:
            st = os.stat(f)
        result.finish()

        values.append(unicode(result))

        return values


    def postProcess(self, args, values):
        if os.path.exists(args['path']):
            shutil.rmtree(args['path'])

        return values
