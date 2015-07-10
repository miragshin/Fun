import os
import requests

def generate():
    list = ['https://xakep.ru/wp-content/uploads/2014/08/xa_01-02_2011_low.pdf','https://xakep.ru/wp-content/uploads/2014/08/xakep_05_2014.pdf','https://xakep.ru/wp-content/uploads/2014/09/xakep_06_2014.pdf','https://xakep.ru/wp-content/uploads/2014/09/xakep_07_2014.pdf']
    for year in range(1999,2016):
        for i in range(1,13):
            if year < 2009:
                list.append("https://xakep.ru/wp-content/uploads/2014/08/xa_%02d_%d_low.pdf" %(i,year))
            elif year == 2009:
                list.append("https://xakep.ru/wp-content/uploads/2014/08/XA_%02d_%d_low.pdf" %(i,year))
            elif year == 2010:
                year = year +1
            elif year ==2011:
                list.append("https://xakep.ru/wp-content/uploads/2014/08/xa_%02d_2011_low1.pdf" %i)
            elif year== 2014 and i>7:
                list.append("https://xakep.ru/wp-content/uploads/2015/06/xakep_%02d_%d.pdf" %(i,year))
            else:
                list.append("https://xakep.ru/wp-content/uploads/%d/06/xakep_%02d_%d.pdf" %(year,i,year))

    f = open('out.txt', 'w')
    for url in list:
        print >>f, url
    f.close()

def command():
    os.system('wget -i out.txt')

def main():
    generate()
    command()

main()
