your_library=[]
your_wishllist=[]
your_library.append(input("enter the name of a book you own : "))
your_library.append(input("enter the name of another book you own (or press 'Enter 'to skip ) : "))
print("your library: ",your_library)
your_wishllist.append(input("enter the name of a book you wish in the future : "))
your_wishllist.append(input("enter the name of another book you wish to have (or press enter to skip) : "))
print("your wish list: ",your_wishllist)
new=input("enter the name of a book from your wishlist that you have (or press'enter ' to skip ): ")
if new in your_wishllist:
    your_wishllist.remove(new)
    your_library.append(new)
    print("the updating your library : ",your_library)
    print("the updating your wishlist : ",your_wishllist)
donate=input("enter the name of a book from your library you wish to donate (or press'enter 'to skip): ")
if donate in your_library:
    your_library.remove(donate)
    print("final library after donations: ",your_library)
