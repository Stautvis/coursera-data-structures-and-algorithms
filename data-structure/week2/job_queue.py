import heapq

class Worker:
    def __init__(self, id, release_time = 0):
        self.id = id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.id < other.id
        else:
            return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.id > other.id
        else:
            return self.release_time > other.release_time

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    worker_queue = [Worker(i) for i in range(n_workers)]
    for job in jobs:
        worker = heapq.heappop(worker_queue) #gets lowest worker(min time or id) from heap

        result.append((worker.id, worker.release_time)) #store result
        worker.release_time += job #adds more processing time
        heapq.heappush(worker_queue, worker) #puts to heap

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
