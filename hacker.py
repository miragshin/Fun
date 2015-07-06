import os
# Generating Links Magazine before 2013

f = open('out.txt', 'w')

def generate():
    list = []
    y=1999
    while y <= 2012:
        for i in range(1,13):
            list.append("https://xakep.ru/wp-content/uploads/2014/08/xa_%02d_%d_low.pdf" %(i,y))
        y = y +1
# Generating links after 2013
    z=2013
    while z <= 2015:
        for x in range(1,13):
            list.append("https://xakep.ru/wp-content/uploads/%02d/%02d/xakep_%02d_%d.pdf" %(z,x,z,x))
        z = z + 1
    for url in list:
        print >>f, url
    f.close()
def command():
    os.system('wget -i out.txt')

def main():
    generate()
    command()

main()
