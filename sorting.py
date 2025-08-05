songs=["Heartshaker","Crown","ForU","StealMyGirl","View","Fever","LoveSickGirls"];
n=len(songs);#sorted some of my favourite songs by their name length using bubble sort
for i in range(n):
    for j in range(0,n-i-1):
        if len(songs[j])>len(songs[j+1]):
           songs[j],songs[j+1]=songs[j+1],songs[j];
print("Songs sorted by length:",songs);
                          
