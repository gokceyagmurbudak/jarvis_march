import matplotlib.pyplot as plt  
import random


class line_vector:
        def __init__(self,point1_point2):
            self.point1_point2 = [] # for line (point on Hull)
            
class point(line_vector):  
    _points_ = [] # all points


    def __init__(self, x, y):
        self.x = x
        self.y = y
        line_vector.__init__(self,[])

    def random_points(self, point):
        ''''used for random points'''
        self._points_.append(point)
        
    def leftmost_point(self):
        points = self._points_

        # get leftmost point
        start_point = points[0]
        minimum_x = start_point.x
        for p in points[1:]:
            if p.x < minimum_x:
                minimum_x = p.x
                start_point = p

        point = start_point
        self.point1_point2.append(point)
        return points,point,start_point
    def jarvis_march(self):
        '''
        Computes the points that make up the convex hull.
        :return:
        '''
        a=self.leftmost_point()
        points= a[0]
        point=  a[1]
        start=  a[2]
        
        far_point = None
        while far_point is not start:

            # Take the first point (first maximum) to be used to compare with others
            point1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    point1 = p
                    break

            far_point = point1

            for point2 in points:

                if point2 is point or point2 is point1:
                    continue
                else:
                    sign = (
            ((point2.x - point.x) * (far_point.y - point.y))
            - ((far_point.x - point.x) * (point2.y - point.y))
        )
                    if sign > 0:  # left point
                        far_point = point2 

            self.point1_point2.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points_ and not self.point1_point2:
            self.jarvis_march()

        return self.point1_point2
    
    def distance_between_two_points(self):

        for_x=([p.x for p in self._points_])
        
        for_y=([p.y for p in self._points_])
        

        for i in range(len(for_x)-1):                
            dist = ((for_x[i+1]- for_x[i])**2 + (for_y[i+1] - for_y[i])**2 )**(1/2)
            
            print(dist)
            

    def display_envelope(self):
        # all points
        x = [p.x for p in self._points_]
        y = [p.y for p in self._points_]
        plt.plot(x, y, marker='D', linestyle='None')

        # hull (line) points
        hx = [p.x for p in self.point1_point2]
        hy = [p.y for p in self.point1_point2]
        plt.plot(hx, hy)

        plt.title('Jarvis Convex Hull')
        plt.show()

        return x, y

def display_points():  
    x=0
    y=0
    ch = point(x,y)
    for _ in range(50):
        ch.random_points(point(random.randint(-100, 100), random.randint(-100, 100)))
    ch.distance_between_two_points()
    
    ch.get_hull_points()
    ch.display_envelope()


if __name__ == '__main__':  
    display_points()

