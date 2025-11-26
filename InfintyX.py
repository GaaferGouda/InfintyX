import math
import pygame


def rotate_pt(p, c, theta):
    """Rotate point p around point c by angle theta"""
    sin = math.sin(theta)
    cos = math.cos(theta)
    return (
        cos * (p[0] - c[0]) - sin * (p[1] - c[1]) + c[0],
        sin * (p[0] - c[0]) + cos * (p[1] - c[1]) + c[1]
    )


def scale_segment(p0, p1, u):
    """Return new segment of length u going in same direction as p0 to p1"""
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = (x1 - x0), (y1 - y0)
    d = math.sqrt(dx * dx + dy * dy)
    return p0, (x0 + dx / d * u, y0 + dy / d * u)


def lem_curve(t, u, c):
    """
    Generate lemniscate (x,y) at angle t in radians of size u, centered at point c
    See parameterized section: https://mathworld.wolfram.com/Lemniscate.html
    """
    den = 1.0 + math.sin(t) ** 2
    n1 = u * math.cos(t)
    return n1 / den + c[0], n1 * math.sin(t) / den + c[1]


class PointHistory(object):
    """Class to keep track of last n points - a kind of queue"""
    
    def __init__(self, n=20):
        self.pts = []
        self.n = n
    
    def add(self, p):
        """Add point, but if over n, drop oldest one"""
        self.pts.append(p)
        if len(self.pts) > self.n:
            self.pts.pop(0)
        return self.pts.copy()


def interpolate_color(color1, color2, t):
    """Interpolate between two colors"""
    return tuple(int(c1 + (c2 - c1) * t) for c1, c2 in zip(color1, color2))


def anim():
    pygame.init()
    game_clock = pygame.time.Clock()
    width, height = 1200, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lemniscate Animation")
    
    # Infinity X logo colors: dark blue to light blue gradient
    dark_blue = (0, 52, 89)      # Dark navy blue
    mid_blue = (25, 85, 140)     # Medium blue
    light_blue = (120, 150, 180) # Light grayish blue
    
    line_pts = PointHistory(50)  # number of points to display each step (length of tail)
    t = 0.0  # angle that controls animation
    
    while True:
        screen.fill((255, 255, 255))  # white background like the logo
        pts = line_pts.add(lem_curve(t, width / 3, (width / 2, height / 2)))  # add new point
        
        if len(pts) > 1:
            # draw segments with gradient color
            for i in range(len(pts) - 1):
                # Calculate color based on position in the trail
                progress = i / len(pts)
                if progress < 0.5:
                    color = interpolate_color(dark_blue, mid_blue, progress * 2)
                else:
                    color = interpolate_color(mid_blue, light_blue, (progress - 0.5) * 2)
                
                pygame.draw.line(screen, color, pts[i], pts[i + 1], 12)
            
            # calculate and draw arrow head with light blue color
            p0, p1 = pts[-2:]  # use last two points for vector direction
            a, b = scale_segment(p1, p0, 70)  # scale segment in backward direction of last two pts
            left = rotate_pt(b, a, math.pi / 8)  # rotate it for side 1
            right = rotate_pt(b, a, -math.pi / 8)  # rotate for side 2
            
            pygame.draw.line(screen, light_blue, left, p0, 12)  # draw arrow side 1
            pygame.draw.line(screen, light_blue, right, p0, 12)  # draw arrow side 2
        
        t += 1 / 20  # advance angle of tip segment
        
        pygame.display.update()
        game_clock.tick(60)
        
        if pygame.event.peek(pygame.QUIT):
            break
    
    pygame.quit()


if __name__ == '__main__':
    anim()
