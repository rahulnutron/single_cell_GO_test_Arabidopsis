import os
import subprocess
import time
# Install https://github.com/tanghaibao/goatools
# place go-basic.obo in the current working directory
def Go_test(marker_file = r"PATH/markers_seurat.csv",fc = 1,p_val_adj = 0.05):
    dic = {}

    os.mkdir(marker_file.split('.')[0]+"_GOTest")
    package = input('Enter package (seurat or monocle):')
    if package == 'seurat':
        fr = open(marker_file,'r')
        for i,line in enumerate(fr):
            if i>0:
                line = line.replace('"','')
                s = line.split(',')
                dic[s[6]] = []
        fr.close()
        
        fr = open(marker_file,'r')
        for i,line in enumerate(fr):
            if i>0:
                line = line.replace('"','')
                s = line.split(',')
                if float(s[2])>=fc and float(s[5])<=p_val_adj:
                    dic[s[6]].append(s[7].strip('\n'))
        fr.close()
        for c in dic:
            fw = open(marker_file+'_temp',"w")
            for g in dic[c]:
                fw.write(g+'\n')
            fw.close()

            
            
            subprocess.Popen([r"PATH\Scripts\find_enrichment.py",
                  marker_file+'_temp',
                  r"PATH/goatools-main/goatools-main/data/population.txt",
                  r"PATH/goatools-main/goatools-main/data/association.txt",
                  r"--pval=0.05", r"--method=fdr_bh",r"--pval_field=fdr_bh",
                  r"--outfile="+marker_file.split('.')[0]+"_GOTest"+"/"+c+".xlsx"],shell=True)
            
            time.sleep(3)
    else:
        fr = open(marker_file,'r')
        for i,line in enumerate(fr):
            if i>0:
                line = line.replace('"','')
                s = line.split(',')
                dic[s[3]] = []
        fr.close()
        
        fr = open(marker_file,'r')
        sp = input('Enter specificity:')
        for i,line in enumerate(fr):
            if i>0:
                line = line.replace('"','')
                s = line.split(',')
                if float(s[7])>=float(sp) and float(s[10].strip('\n'))<=p_val_adj:
                    dic[s[3]].append(s[1].strip('\n'))
        fr.close()
        for c in dic:
            fw = open(marker_file+'_temp',"w")
            for g in dic[c]:
                fw.write(g+'\n')
            fw.close()

            
            
            subprocess.Popen([r"PATH\Scripts\find_enrichment.py",
                  marker_file+'_temp',
                  r"PATH/goatools-main/goatools-main/data/population.txt",
                  r"PATH/goatools-main/goatools-main/data/association.txt",
                  r"--pval=0.05", r"--method=fdr_bh",r"--pval_field=fdr_bh",
                  r"--outfile="+marker_file.split('.')[0]+"_GOTest"+"/"+c+".xlsx"],shell=True)
            
            time.sleep(3)

    #os.remove(marker_file+'_temp')


    
    return dic
