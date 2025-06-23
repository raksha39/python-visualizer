import pygame
import time

class Renderer:
    def __init__(self, array, width, height, mode="sorting"):
        self.array = array
        self.width = width
        self.height = height
        self.mode = mode
        self.bar_width = width // len(array)
        self.colors = {
            "background": (255, 255, 255),
            "bar": (0, 0, 255),
            "sorted": (0, 255, 0),
            "current": (255, 0, 0),
            "found": (0, 255, 0),
            "left": (255, 165, 0),
            "right": (255, 165, 0),
            "mid": (255, 0, 255),
            "text": (0, 0, 0),
            "text_white": (255, 255, 255)
        }
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 20)

    def draw_array(self, array, current_indices=None):
        self.screen.fill(self.colors["background"])
        
        for i, value in enumerate(array):
            color = self.colors["bar"]
            if current_indices and i in current_indices:
                color = self.colors["current"]
            
            # Calculate bar height and position
            bar_height = (value / max(array)) * (self.height - 100)
            x = i * self.bar_width
            y = self.height - bar_height - 50
            
            pygame.draw.rect(self.screen, color, (x, y, self.bar_width - 1, bar_height))
            
            # Draw value on top of bar for small arrays
            if len(array) <= 20:
                text = self.font.render(str(value), True, self.colors["text"])
                text_rect = text.get_rect()
                text_rect.centerx = x + self.bar_width // 2
                text_rect.bottom = y - 5
                self.screen.blit(text, text_rect)
        
        pygame.display.flip()

    def draw_search_array(self, step):
        self.screen.fill(self.colors["background"])
        array = step['array']
        algorithm = step['algorithm']
        target = step['target']
        
        for i, value in enumerate(array):
            color = self.colors["bar"]
            text_color = self.colors["text_white"]
            
            if algorithm == "Linear Search":
                if i == step['current_index']:
                    color = self.colors["current"]
                if step['found'] and i == step['current_index']:
                    color = self.colors["found"]
            
            elif algorithm == "Binary Search":
                if i == step.get('left', -1):
                    color = self.colors["left"]
                elif i == step.get('right', -1):
                    color = self.colors["right"]
                elif i == step.get('mid', -1):
                    color = self.colors["mid"]
                if step['found'] and i == step.get('mid', -1):
                    color = self.colors["found"]
            
            # Calculate bar height and position
            bar_height = max((value / max(array)) * (self.height - 150), 40)  # Minimum height for visibility
            x = i * self.bar_width
            y = self.height - bar_height - 100
            
            pygame.draw.rect(self.screen, color, (x, y, self.bar_width - 1, bar_height))
            
            # Always draw the number inside the bar for searching algorithms
            font_size = min(int(self.bar_width * 0.8), 24)  # Adjust font size based on bar width
            if font_size > 0:
                number_font = pygame.font.Font(None, font_size)
                text = number_font.render(str(value), True, text_color)
                text_rect = text.get_rect()
                text_rect.center = (x + self.bar_width // 2, y + bar_height // 2)
                
                # Make sure text fits within the bar
                if text_rect.width < self.bar_width - 4 and text_rect.height < bar_height - 4:
                    self.screen.blit(text, text_rect)
                else:
                    # Use smaller font if it doesn't fit
                    smaller_font = pygame.font.Font(None, max(font_size - 4, 12))
                    text = smaller_font.render(str(value), True, text_color)
                    text_rect = text.get_rect()
                    text_rect.center = (x + self.bar_width // 2, y + bar_height // 2)
                    if text_rect.width < self.bar_width - 4:
                        self.screen.blit(text, text_rect)
            
            # Draw index number below the bar
            index_text = self.small_font.render(str(i), True, self.colors["text"])
            index_rect = index_text.get_rect()
            index_rect.centerx = x + self.bar_width // 2
            index_rect.top = self.height - 90
            self.screen.blit(index_text, index_rect)
        
        # Draw algorithm info
        info_text = f"{algorithm} - Target: {target}"
        if step['found']:
            info_text += " - FOUND!"
        
        text_surface = self.font.render(info_text, True, self.colors["text"])
        self.screen.blit(text_surface, (10, 10))
        
        # Draw legend for binary search
        if algorithm == "Binary Search":
            legend_y = 50
            legend_items = [
                ("Left", self.colors["left"]),
                ("Mid", self.colors["mid"]),
                ("Right", self.colors["right"]),
                ("Found", self.colors["found"])
            ]
            
            x_offset = 10
            for label, color in legend_items:
                # Draw color box
                pygame.draw.rect(self.screen, color, (x_offset, legend_y, 20, 20))
                # Draw label
                label_text = self.small_font.render(label, True, self.colors["text"])
                self.screen.blit(label_text, (x_offset + 25, legend_y + 2))
                x_offset += 100
        
        pygame.display.flip()

    def visualize(self, steps):
        running = True
        step_index = 0
        
        while running and step_index < len(steps):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Draw current step
            self.draw_array(steps[step_index])
            time.sleep(0.1)  # Delay for visualization
            step_index += 1
            
            self.clock.tick(60)
        
        # Keep window open until closed
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()

    def visualize_search(self, steps):
        running = True
        step_index = 0
        
        while running and step_index < len(steps):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Pause/unpause with spacebar
                        paused = True
                        while paused:
                            for pause_event in pygame.event.get():
                                if pause_event.type == pygame.QUIT:
                                    running = False
                                    paused = False
                                elif pause_event.type == pygame.KEYDOWN:
                                    if pause_event.key == pygame.K_SPACE:
                                        paused = False
            
            if running:
                # Draw current step
                self.draw_search_array(steps[step_index])
                time.sleep(0.8)  # Slower delay for searching
                step_index += 1
            
            self.clock.tick(60)
        
        # Keep window open until closed
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()