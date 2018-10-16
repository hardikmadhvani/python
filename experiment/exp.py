import sys
if len(sys.argv)!=2:
    print 'usage: ./a.out filename '
else:

    try:
        fh=open('data','r')
        sarch_str=['hello','sensor_get_cur_chromatix_name']
        found=[]
        for line in fh:
            if any(word in line for word in sarch_str):
                found.append(line)
        print' '.join(found)
        fh.close()
    except  IOError:
        print 'file not present'

