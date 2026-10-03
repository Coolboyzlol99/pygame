import pygame

pygame.init()

SCREEN_WIDTH = 500 
SCREEN_HEIGHT = 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Image to Screen")

background_image = pygame.transform.scale(pygame.image.load("heetler.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

text = pygame.font.Font(None, 36).render("Hello, World!", True, (0, 0, 0))

text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game_loop()