from Balls import *


class Gun:
    """
    Class of Cannon
    """
    def __init__(self, x=40, y=700, color=BLACK, length=70, angle=0,
                 shooting_mode=False, power=0, activation=False, number=1):
        """
        :param x: coordinate x
        :param y: coordinate y
        :param color: color
        :param length: gun barrel length
        :param angle: angle with the horizon
        :param shooting_mode:
        :param power: power of shot
        :param number: number of tank
        """
        self.x = x
        self.y = y
        self.velocity_x = 2
        self.velocity_y = 2
        self.color = color
        self.body_color = GREEN
        self.tank_tower_color = DARKGREEN
        self.length = length
        self.angle = angle
        self.shooting_mode = shooting_mode
        self.power = power
        self.maxlength = length*1.5
        self.activation = activation
        self.size = 50
        self.health = 500
        self.is_alive = True
        self.number = number

    def fire2_start(self):
        """
        Starts shooting mode
        """
        self.shooting_mode = True

    def print_health(self, position):
        """
        Prints health of tank
        :param position: set position
        """
        if self.health <= 0:
            self.health = 0
        new_gun_health_myfont = pygame.font.SysFont('Times New Roman', 30)
        scoretext = new_gun_health_myfont.render((str(self.number) + ") Health: " + str(self.health)), True, BLACK)
        screen.blit(scoretext, position)

    def motion(self):
        """
        Move gun using WASD
        """
        if pygame.key.get_pressed()[pygame.K_d]:
            if self.x >= screensize[0] - 20:
                pass
            else:
                self.x += self.velocity_x
        if pygame.key.get_pressed()[pygame.K_a]:
            if self.x <= 20:
                pass
            else:
                self.x -= self.velocity_x
        if pygame.key.get_pressed()[pygame.K_s]:
            if self.y >= screensize[1] - 20:
                pass
            else:
                self.y += self.velocity_y
        if pygame.key.get_pressed()[pygame.K_w]:
            if self.y <= 20:
                pass
            else:
                self.y -= self.velocity_y

    def fire2_end(self):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball(color=COLORS[randint(0, 5)])
        new_ball.radius = 15

        new_ball.velocity_x = self.power * math.cos(self.angle) * 0.5
        new_ball.velocity_y = self.power * math.sin(self.angle) * 0.5
        new_ball.coord_x = self.x + self.length * math.cos(self.angle)
        new_ball.coord_y = self.y - self.length * math.sin(self.angle)

        element_mass['massive'].append(new_ball)
        self.power = 0
        self.length = 70
        self.color = BLACK
        self.shooting_mode = False

    def draw_gun(self):
        """
        Draws Gun
        """
        pygame.draw.rect(screen, self.body_color, (self.x - 45, self.y, 90, self.size - 10))
        pygame.draw.rect(screen, BLACK, (self.x - 45, self.y, 90, self.size - 10), width=2)
        pygame.draw.line(screen, self.color, (self.x, self.y),
                         (self.x + self.length * math.cos(self.angle),
                          self.y - self.length * math.sin(self.angle)), width=7)
        pygame.draw.circle(screen, self.tank_tower_color, (self.x, self.y), 20)

    def targeting(self):
        """
        Process of targeting (depends on mouse position)
        """
        x0, y0 = pygame.mouse.get_pos()
        if x0 == self.x:
            if y0 > self.y:
                self.angle = -1.57
            if y0 <= self.y:
                self.angle = 1.57
        else:
            if x0 < self.x:
                self.angle = 3.14 - math.atan((y0 - self.y) / (x0 - self.x))
            else:
                self.angle = - math.atan((y0 - self.y) / (x0 - self.x))
        if self.shooting_mode:
            self.color = RED
            if self.length >= self.maxlength:
                pass
            else:
                self.length += 1
        else:
            self.color = BLACK
        if not self.activation:
            self.draw_gun()

    def hit_tank(self, obj):
        """
        Checking of tank hitting
        :param obj: Sells, bombs
        """
        if (self.x - obj.coord_x) ** 2 + (self.y - obj.coord_y) ** 2 <= (self.size + obj.radius) ** 2:
            self.health -= 20
            obj.is_alive = False
            if self.health <= 0:
                self.is_alive = False

    def power_up(self):
        """
        Gains power of shot
        """
        if self.shooting_mode:
            if self.power < 100:
                self.power += 0.5
            self.color = RED
        else:
            self.color = BLACK
