from Gun import *


class Player:
    """
    Player with some parameters
    """

    def __init__(self, score=0, shots=0):
        """
        Some information about player (Score, Username, number of shots)
        :param score:
        :param shots: number of shots
        """
        self.score = score
        self.shots = shots


def clear_massive(mapa):
    """
    Delete element of massive
    :param mapa: map that contains number of elements that should be deleted after updating of screen
                    and massive of elements
    """
    if mapa['remove ind'] == -1:
        pass
    else:
        mapa['massive'].remove(mapa['massive'][mapa['remove ind']])
    mapa['remove ind'] = -1


def generate_targets(number_of_targets):
    """
    Generation of targets, put them in massive
    :param number_of_targets:set number of targets
    """
    for i in range(number_of_targets):
        targets_mass['massive'].append(BallTarget(velocity_x=randint(-10, 10), target_type=randint(1, 2)))


finished = False


def game():
    """
    Game session process
    Move tanks using WASD
    You can switch to another Tank using M
    """
    global finished
    finished = False
    generate_targets(10)
    counter = 0
    new_gun = Gun(activation=True, number=1)
    another_new_gun = Gun(x=880, y=700, number=2)
    finished_session = False
    new_player = Player()
    element_mass['massive'].clear()
    see_results = False

    while not finished_session:

        clock.tick(FPS)
        if not see_results:
            myfont = pygame.font.SysFont('Times New Roman', 30)
            scoretext = myfont.render((str(new_player.shots)), True, BLACK)
            screen.blit(scoretext, (screensize[0] // 8, 30))
        if see_results:
            myfont2 = pygame.font.SysFont('Times New Roman', 30)
            finish_session_text = myfont2.render(("Вы уничтожили все цели за: " + str(new_player.shots) + " выстрелов"),
                                                 True, BLACK)
            screen.blit(finish_session_text, (screensize[0] // 3.5, screensize[1] // 3))
            counter += 1
            if counter == 150:
                finished_session = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if new_gun.activation:
                        new_gun.activation = False
                        another_new_gun.activation = True
                    else:
                        new_gun.activation = True
                        another_new_gun.activation = False

            if event.type == pygame.QUIT:
                finished = True
                finished_session = True
            if new_gun.activation:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_gun.fire2_start()
                elif event.type == pygame.MOUSEBUTTONUP:
                    new_gun.fire2_end()
                    if not see_results:
                        new_player.shots += 1
            if another_new_gun.activation:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    another_new_gun.fire2_start()
                elif event.type == pygame.MOUSEBUTTONUP:
                    another_new_gun.fire2_end()
                    if not see_results:
                        new_player.shots += 1

        new_gun.print_health(position=(screensize[0] // 8, 80))
        another_new_gun.print_health(position=(screensize[0] // 8, 120))

        if new_gun.is_alive:
            new_gun.draw_gun()
        if another_new_gun.is_alive:
            another_new_gun.draw_gun()

        if new_gun.activation and new_gun.is_alive:
            new_gun.motion()
            new_gun.targeting()
            new_gun.power_up()

        if another_new_gun.activation and another_new_gun.is_alive:
            another_new_gun.motion()
            another_new_gun.targeting()
            another_new_gun.power_up()

        for i in range(len(targets_mass['massive'])):
            targets_mass['massive'][i].move_target()
            if targets_mass['massive'][i].attack:
                bombs_massive['massive'].append(Ball(coord_x=targets_mass['massive'][i].coord_x, radius=10,
                                                     coord_y=targets_mass['massive'][i].coord_y, color=BLACK,
                                                     velocity_x=0, velocity_y=0, time_of_live=100))
                targets_mass['massive'][i].attack = False

        for k in range(len(bombs_massive['massive'])):
            bombs_massive['massive'][k].move_ball()
            new_gun.hit_tank(bombs_massive['massive'][k])
            another_new_gun.hit_tank(bombs_massive['massive'][k])
            if not bombs_massive['massive'][k].is_alive:
                bombs_massive['remove ind'] = k

        for j in range(len(element_mass['massive'])):
            element_mass['massive'][j].move_ball()

            if new_gun.is_alive:
                new_gun.hit_tank(element_mass['massive'][j])
            if another_new_gun.hit_tank(element_mass['massive'][j]):
                another_new_gun.hit_tank(element_mass['massive'][j])
            if len(bombs_massive['massive']) > j:
                if new_gun.is_alive:
                    new_gun.hit_tank(bombs_massive['massive'][j])
                if another_new_gun.is_alive:
                    another_new_gun.hit_tank(bombs_massive['massive'][j])

        for i in range(len(targets_mass['massive'])):
            for j in range(len(element_mass['massive'])):
                if not element_mass['massive'][j].is_alive:
                    element_mass['remove ind'] = j
                if not targets_mass['massive'][i].is_alive:
                    targets_mass['remove ind'] = i
                targets_mass['massive'][i].hit_enemy(element_mass['massive'][j], new_player)

        clear_massive(targets_mass)
        clear_massive(element_mass)
        clear_massive(bombs_massive)

        if not targets_mass['massive']:
            see_results = True

        pygame.display.update()
        screen.fill(WHITE)


while not finished:
    game()

pygame.quit()
