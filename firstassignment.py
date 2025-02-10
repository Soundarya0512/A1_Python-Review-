def main():
    get_gene()
    gene_exp()
def get_gene():
    f=open("drosphila_data.csv","r")
    content=f.readlines()
    #content=content.rstrip('\n').split(',')
    #print(content)
    i=0
    list1=[]
    Dm_Ds=[]
    while i<=len(content)-1:
        list1=content[i].split(',')
        if "Drosophila melanogaster" in list1[0] or "Drosophila simulans" in list1[0]:
            Dm_Ds.append(list1[2])
        #print(list1)
        i=i+1
    print(Dm_Ds)
    f.close()
def gene_exp():
    f=open("drosphila_data.csv","r")
    content=f.readlines()
    list2=[]
    #print(content)
    i=0
    while i<=len(content)-1:
        list2=content[i].split(',')
        #print(list2)
        d=(list2[1].count("a")+list2[1].count("t"))/len(list2[1])
        #print(d)
        if d>0.65:
            print(f"{list2[2]} has high AT Content")
        elif d<0.45:
            print(f"{list2[2]} has low AT Content")
        else:
            print(f"{list2[2]} has medium AT Content")
        i=i+1
main()
