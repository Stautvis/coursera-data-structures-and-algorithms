# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        if self.size == 0: #if buffer is zero, then failed
            return Response(True, -1) 

        while len(self.finish_time) > 0:
            if self.finish_time[0] <= request.arrived_at:
                self.finish_time.pop(0)
            else:
                break

        if self.size == len(self.finish_time):
            return Response(True, -1) # if buffer is full, then failed
        elif len(self.finish_time) == 0:
            self.finish_time = [request.arrived_at + request.time_to_process]
            return Response(False, request.arrived_at)

        response = Response(False, self.finish_time[-1])
        self.finish_time.append(self.finish_time[-1] + request.time_to_process)
        return response


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at)


if __name__ == "__main__":
    main()
