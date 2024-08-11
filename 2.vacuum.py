def main():
    rooms = {'A' : 0, 'B' : 0}
    cost = 0
    
    print("\t\t---------------VACUUM CLEARNER WORLD---------------\n")
    print("[1] FOR DIRTY\n[2] FOR CLEAN\n")
    
    for i in rooms.keys():
        rooms[i] = int(input(f"ENTER THE STATUS OF {i} : "))
    print()
    
    for i in rooms.keys():
        if(rooms[i] == 1):
            print(f"[-] ROOM {i} IS DIRTY... CLEANING...")
            rooms[i] = 0
            
            print(f"[*] ROOM {i} IS NOW CLEANED.")
            cost += 1
            
        else:
            print(f"[!] ROOM {i} IS ALREADY CLEAN.")
            
    print(f"TOTAL COST = {cost}", end="\n\n")
    
    
if __name__ == "__main__":
    main()