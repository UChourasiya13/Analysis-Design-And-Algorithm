def schedule_jobs(jobs):
    # sort the jobs by their finishing time in ascending order
    jobs.sort(key=lambda x: x[1])
    
    # initialize variables
    n = len(jobs)
    schedule = []
    current_time = 0
    
    # loop over all jobs
    for i in range(n):
        start_time, finish_time, value = jobs[i]
        
        # check if the job can be scheduled
        if start_time >= current_time:
            schedule.append(i)
            current_time = finish_time
    
    return schedule
