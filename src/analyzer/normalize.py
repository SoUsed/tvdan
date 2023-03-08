def geomean(val1, val2):
    from math import sqrt
    return sqrt(val1*val2)

def normalize(reference, values):
    return [[entry[0]/reference[0], entry[1]/(geomean(max([v[1] for v in values]),reference[1]))] for entry in values]