import math, copy
dane = [(1, math.sqrt(3)), (9, math.sqrt(3)), (5, math.sqrt(3) * 5), (40, 2)]
class geometry:
    def triangleFinder(dane):
        pointlist = []
        pointList = []
        for point1 in dane:
            print(point1)
            for point2 in dane:
                if point2 != point1:
                    length1 = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
                    for point3 in dane:
                        if point3 != point2 and point3 != point1:
                            length2 = (point2[0] - point3[0]) ** 2 + (point2[1] - point3[1]) ** 2
                            length3 = (point1[0] - point3[0]) ** 2 + (point1[1] - point3[1]) ** 2
                            if math.fabs(length1 - length2) <= 0.0001 and math.fabs(length3 - length2) <= 0.0001 and math.fabs(length3 - length1) <= 0.0001:
                                pointlist.append(point1)
                                pointlist.append(point2)
                                pointlist.append(point3)
                                pointlist.sort()
                                pointlist1 = copy.deepcopy(pointlist)
                                if pointList.count(pointlist1) == 0:
                                    pointList.append(pointlist1)
                                    pointlist.clear()
                                else:
                                    pointlist.clear()
                                pointlist.clear()
        print(pointList)
        return pointList

    def field(punkty, dane):
        garbagelist = []
        punktyStorage = punkty[:]
        for elements in punkty:
            point1 = elements[0]
            point2 = elements[1]
            point3 = elements[2]
            Field = 0.5 * abs((point1[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1])))
            for points in dane:
                field1 = 0.5 * abs((points[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - points[1]) + point3[0] * (points[1] - point2[1])))
                field2 = 0.5 * abs((point1[0] * (points[1] - point3[1]) + points[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - points[1])))
                field3 = 0.5 * abs((point1[0] * (point2[1] - points[1]) + point2[0] * (points[1] - point1[1]) + points[0] * (point1[1] - point2[1])))
                if abs(Field - (field1 + field2 + field3)) <= 0.001 and field3 != 0 and field2 != 0 and field1 != 0:
                    punktyStorage.remove(elements)
        if len(punktyStorage) != 0:
            print("True")
            return True
        else:
            print("False")
            return False


geometry.field(geometry.triangleFinder(dane), dane)



