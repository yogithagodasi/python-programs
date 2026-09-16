def job_scheduling(jobs):
    jobs.sort(key=lambda x:x[2],reverse=True)
    max_deadline(job[i] for job in jobs)
    slots=[false]*max_deadline
    result=[none]*max_deadline
    total_profit=0
    for job in jobs:
        job_id,deadline,profit 
    for i in range(min(max_deadline,deadline)-1,-1,-1):
        if slots[i]:
            slots[i]=True
            result[i]=job_id 
            total_profit+=profit 
            break 
   return result,total_profit 
n = int(input("enter thr no of jobs"))
jobs=[]
for i in range(n):
      job_id=int(input("enter the job id"))
      deadline=int(input("enter the deadline id"))
      profit=int(input("enter the profit"))
      jobs.append(job_id,deadline,profit )
schedule,profit=job_scheduling(jobs)
print("schedule jobs")
for job in schedule:
        if job:
            print(job)
    print("total profit:",profit)