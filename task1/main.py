import heapq


def min_cost(cables_list):
    if not cables_list:
        return 0

    heapq.heapify(cables_list)

    total_cost = 0

    while len(cables_list) > 1:
        cable1 = heapq.heappop(cables_list)
        cable2 = heapq.heappop(cables_list)

        connection_cost = cable1 + cable2
        total_cost += connection_cost

        heapq.heappush(cables_list, connection_cost)

    return total_cost


def print_result(cables_list):
    print(f"Cables: {cables_list} with min cost: {min_cost(cables_list)}")


# Printing results
print_result([1, 2, 3, 4, 5, 6, 7])
print_result([3, 2, 1])
print_result([1, 1])
print_result([0])
print_result([3])
print_result([])
