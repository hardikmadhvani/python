import sys
if len(sys.argv)!=3:
    print 'usage: ./a.out filename log '
else:

    try:
        fh=open(sys.argv[1],'r')
        fg=open(sys.argv[2],'r')
        search=[]
        final_list=[]
        for line in fg.readlines():
            search.append(line)
    #    print search
        for i in search:
            final_list.append(i.strip())    #for removing '\n'
        print final_list

   #     sarch_str=['hello','sensor_get_cur_chromatix_name']
        found=[]
        for line in fh:
            if any(word in line for word in final_list):
                found.append(line)
        print' '.join(found)
        fh.close()
    except  IOError:
        print 'file not present'


