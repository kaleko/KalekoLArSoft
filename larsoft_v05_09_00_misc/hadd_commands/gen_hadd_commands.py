import os
basedir = '/pnfs/uboone/scratch/users/kaleko/kaleko_beamfilter_reco_neutrion2016_samdef_fullsample_newtar_ALL_larlite_out/v05_09_00/'
dirlist = os.listdir(basedir)
dirranges = range(1,302,30)
for x in xrange(1,len(dirranges),1):
    f = open('hadd%d_command.txt'%x,'w')
    filenums = [ int(blah[9:]) for blah in dirlist if int(blah[9:]) < dirranges[x] and int(blah[9:]) >= dirranges[x-1] ]
    line = 'llhadd /uboone/data/users/kaleko/data_5e19_bnbfilter_allreco/file%d.root'%x
    for filenum in filenums:
        line += ' %s*_%d/*opreco*.root' % (basedir,filenum)
    f.write(line)
    f.close()
