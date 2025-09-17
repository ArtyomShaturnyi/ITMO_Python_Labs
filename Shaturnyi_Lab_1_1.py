ESC = "\033"           # ANSI escape character
flag_height = 32       # Height of the square flag in rows
start_row = 1          # Starting row for drawing the flag
start_col = 1          # Starting column for drawing the flag
h_ratio = 2            # Horizontal stretch factor to compensate for terminal character proportions

def draw_flag():
    red = 41           # ANSI background color code for red
    white = 47         # ANSI background color code for white

    margin = flag_height // 6        # Margin from the edges of the flag
    thickness = flag_height // 6 + 2 # Thickness of the cross arms
    center = flag_height // 2        # Center of the flag

    # Loop over each row of the flag
    for i in range(flag_height):
        line = ""  # Initialize a string for the current row
        # Loop over each column of the flag
        for j in range(flag_height):
            color = red  # Default background color is red

            # Horizontal arm of the cross
            if center - thickness // 2 <= i <= center + thickness // 2 and margin <= j <= flag_height - margin - 1:
                color = white

            # Vertical arm of the cross
            if center - thickness // 2 <= j <= center + thickness // 2 and margin <= i <= flag_height - margin - 1:
                color = white

            # Add the colored "pixel" to the current row
            line += f"{ESC}[{color}m" + ' ' * h_ratio

        # Print the entire row at the correct position with ANSI codes
        print(f"{ESC}[{start_row + i};{start_col}H{line}{ESC}[0m", flush=True)

if __name__ == "__main__":
    # Clear the screen
    print(f"{ESC}[2J", end="", flush=True)
    # Hide the cursor while drawing
    print(f"{ESC}[?25l", end="")
    # Draw the flag
    draw_flag()
    # Show the cursor after drawing
    print(f"{ESC}[?25h", end="")
