# Find an Euclidean distance between (2, 3) and (10, 8)

def euclidean_distance(XA, YA, XB, YB):
    result = ((XA - XB) ** 2 + (YA - YB) ** 2) ** 0.5
    print(f"Euclidean distance between ({XA}, {YA}) and ({XB}, {YB}) is: {result:2f}")

euclidean_distance(2, 3, 10, 8)