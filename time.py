def Get_time(time,minutes):
    
    Persons=int(input("Enter the number of persons"))
    tickets=[]
    
    for ticket in range(Persons):
        ticket=int(input("Enter the tickets"))
        tickets.append(ticket)
    completion_time=[0]*Persons
    remaining_time=tickets
    current_time=0
    while sum(remaining_time)>0:
        for i in range(Persons):
            if remaining_time[i]<=0:
                continue 
            if remaining_time[i]<=time:
                current_time+=remaining_time[i]
                remaining_time[i]=0
                
            else:
                current_time+=time
                remaining_time[i]-=time
                
            if remaining_time[i]==0:
                completion_time[i]=current_time
    new_completion_time=[ct*minutes for ct in completion_time]
    return new_completion_time
