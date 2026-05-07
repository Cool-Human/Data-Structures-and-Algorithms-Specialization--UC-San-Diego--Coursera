# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def assign_jobs_fast(n_workers, jobs):

    result = []

    # Heap stores:
    # (next_free_time, worker_id)
    heap = [(0, worker) for worker in range(n_workers)]

    # Convert list into a valid heap
    heapq.heapify(heap)

    for job in jobs:

        # Get worker who becomes free first
        free_time, worker = heapq.heappop(heap)

        # Assign current job
        result.append(AssignedJob(worker, free_time))

        # Push worker back with updated free time
        heapq.heappush(heap, (free_time + job, worker))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # assigned_jobs = assign_jobs(n_workers, jobs)

    # for job in assigned_jobs:
    #     print(job.worker, job.started_at)

    new_assigned_jobs = assign_jobs_fast(n_workers, jobs)

    for job in new_assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()