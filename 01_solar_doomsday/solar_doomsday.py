def solution(area):
    result = []
    while area > 0:
        square = int(area ** 0.5) ** 2
        area -= square
        result.append(square)

    return result
