from Gun import *


class Player:

    def __init__(self, username='', score=0, shots=0):
        """
        Some information about player (Score, Username, number of shots)
        :param username:
        :param score:
        :param shots:
        """
        self.score = score
        self.username = username
        self.shots = shots


# class Amo(Ball):
#

def generate_targets(number_of_targets):
    """
    Generation of targets, put them in massive
    :param number_of_targets:set number of targets
    """
    for i in range(number_of_targets):
        targets_mass['massive'].append(BallTarget())


finished = False


def game():
    """
    Game session process
    """
    global finished, see_results
    generate_targets(5)
    counter = 0
    new_gun = Gun(activation=True)
    another_new_gun = Gun(x=40, y=50)
    finished_session = False
    see_results = False
    new_player = Player()
    element_mass['massive'].clear()

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

        new_gun.draw_gun()
        another_new_gun.draw_gun()

        if new_gun.activation:
            new_gun.motion()
            new_gun.targeting()
            new_gun.power_up()
        if another_new_gun.activation:
            another_new_gun.motion()
            another_new_gun.targeting()
            another_new_gun.power_up()

        targets_mass['remove ind'] = -1
        element_mass['remove ind'] = -1
        bombs_massive['remove ind'] = -1
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
            if len(bombs_massive['massive']) > j:
                new_gun.hit_tank(bombs_massive['massive'][j])
                another_new_gun.hit_tank(bombs_massive['massive'][j])

        for i in range(len(targets_mass['massive'])):
            for j in range(len(element_mass['massive'])):
                if not element_mass['massive'][j].is_alive:
                    element_mass['remove ind'] = j
                if not targets_mass['massive'][i].is_alive:
                    targets_mass['remove ind'] = i
                targets_mass['massive'][i].hit_enemy(element_mass['massive'][j], new_player)

        if targets_mass['remove ind'] == -1:
            pass
        else:
            targets_mass['massive'].remove(targets_mass['massive'][targets_mass['remove ind']])

        if element_mass['remove ind'] == -1:
            pass
        else:
            element_mass['massive'].remove(element_mass['massive'][element_mass['remove ind']])

        if bombs_massive['remove ind'] == -1:
            pass
        else:
            bombs_massive['massive'].remove(bombs_massive['massive'][bombs_massive['remove ind']])

        print(new_gun.health)
        if not targets_mass['massive']:
            see_results = True

        pygame.display.update()
        screen.fill(WHITE)


while not finished:
    game()

pygame.quit()
