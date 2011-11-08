# coding: utf-8

import os
import shutil
import moduleBase

class fileCopy(moduleBase.moduleBase):
    def preProcess(self, args, values):
        if os.path.exists(args['src']):
            shutil.rmtree(args['src'])

        if os.path.exists(args['dest']):
            shutil.rmtree(args['dest'])

        os.makedirs(args['src'])

        for f in range(args['count']):
            fname = os.path.join(args['src'], '%04d.txt' % f)
            moduleBase.generateFile(fname, args['size'])

        return values

                
    def process(self, args, values):
        fnames = []
        for f in range(args['count']):
            fnames.append('%04d.txt' % f)

        os.makedirs(args['dest'])

        result = moduleBase.benchResult()
        for f in fnames:
            s = os.path.join(args['src'], f)
            d = os.path.join(args['dest'], f)

            print s, '=>' , d
            shutil.copyfile(s,d)

        result.finish()

        values.append(unicode(result))

        return values


    def postProcess(self, args, values):
        if os.path.exists(args['src']):
            shutil.rmtree(args['src'])

        if os.path.exists(args['dest']):
            shutil.rmtree(args['dest'])

        return values
