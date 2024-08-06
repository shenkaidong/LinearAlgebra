from playLA.Vector import Vector
if __name__ == '__main__':
    vec = Vector([5,2])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    vec2 = Vector([3,1])
    print("{} + {} = {}".format(vec, vec2, vec-vec2))

    print("{} * 2 = {}".format(vec, vec*2))

    print("2 * {} = {}".format(vec, 2 * vec))

    zero2 = Vector.zero(2)
    print("{} + {} = {}".format(vec, zero2, vec+zero2))