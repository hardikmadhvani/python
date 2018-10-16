import sys
if len(sys.argv)!=2:
    print 'usage: ./a.out filename'
else:

    try:
        fh=open('data','r')  
        found=[]
        for line in fh.readlines():
            if 'module_sensor_offload_init_config' in line:
                found.append(line)
        print ' '.join(found)
        fh.close()
    except ioerror:
        print 'file not present'

