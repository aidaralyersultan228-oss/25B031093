import os
import pygame


def run_player():
    pygame.init()
    pygame.mixer.init()

    WIDTH = 800
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")

    font = pygame.font.SysFont("arial", 30)
    small_font = pygame.font.SysFont("arial", 22)
    clock = pygame.time.Clock()

    base_path = os.path.dirname(__file__)
    music_folder = os.path.join(base_path, "music", "sample_tracks")

    playlist = []
    if os.path.exists(music_folder):
        for file in os.listdir(music_folder):
            if file.endswith(".mp3") or file.endswith(".wav"):
                playlist.append(os.path.join(music_folder, file))

    playlist.sort()
    current_index = 0
    is_playing = False
    start_ticks = 0

    def play_current():
        nonlocal is_playing, start_ticks
        if not playlist:
            return
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        is_playing = True
        start_ticks = pygame.time.get_ticks()

    def stop_music():
        nonlocal is_playing
        pygame.mixer.music.stop()
        is_playing = False

    def next_track():
        nonlocal current_index
        if not playlist:
            return
        current_index = (current_index + 1) % len(playlist)
        play_current()

    def previous_track():
        nonlocal current_index
        if not playlist:
            return
        current_index = (current_index - 1) % len(playlist)
        play_current()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play_current()
                elif event.key == pygame.K_s:
                    stop_music()
                elif event.key == pygame.K_n:
                    next_track()
                elif event.key == pygame.K_b:
                    previous_track()
                elif event.key == pygame.K_q:
                    running = False

        screen.fill((240, 240, 240))

        title = font.render("Music Player", True, (0, 0, 0))
        screen.blit(title, (30, 30))

        if playlist:
            current_name = os.path.basename(playlist[current_index])
        else:
            current_name = "No tracks found"

        track_text = font.render(f"Track: {current_name}", True, (0, 0, 255))
        screen.blit(track_text, (30, 100))

        status = "Playing" if is_playing else "Stopped"
        status_text = font.render(f"Status: {status}", True, (200, 0, 0))
        screen.blit(status_text, (30, 150))

        if is_playing:
            elapsed = (pygame.time.get_ticks() - start_ticks) // 1000
        else:
            elapsed = 0

        position_text = font.render(f"Position: {elapsed} sec", True, (0, 120, 0))
        screen.blit(position_text, (30, 200))

        controls = [
            "P = Play",
            "S = Stop",
            "N = Next",
            "B = Previous",
            "Q = Quit"
        ]

        y = 270
        for line in controls:
            text = small_font.render(line, True, (0, 0, 0))
            screen.blit(text, (30, y))
            y += 28

        if not playlist:
            warning = small_font.render("Add .mp3 or .wav files to music/sample_tracks", True, (255, 0, 0))
            screen.blit(warning, (30, 350))

        pygame.display.flip()
        clock.tick(30)

    pygame.mixer.music.stop()
    pygame.quit()