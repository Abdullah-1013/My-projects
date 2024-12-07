#include <stdio.h>

// Function to draw and fill a rectangle with a given color
void drawRectangle(int width, int height, char color) {
    // Loop to draw the rectangle row by row
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            printf("%c", color); // Print the character representing the color
        }
        printf("\n"); // Move to the next row
    }
}

// Function to draw the Palestinian flag in a box (stripes)
void drawPalestinianStripes(int boxWidth, int boxHeight) {
    // Calculate the height of each stripe
    int stripeHeight = boxHeight / 3;

    // Draw each stripe
    for (int i = 0; i < 3; i++) {
        if (i % 2 == 0) {
            drawRectangle(boxWidth, stripeHeight, '*'); // Black stripes
        } else {
            drawRectangle(boxWidth, stripeHeight, ' '); // White stripes
        }
    }
}

// Function to draw the Palestinian flag in a box (stars)
void drawPalestinianStars(int boxWidth, int boxHeight) {
    // Calculate the height for stars
    int starHeight = boxHeight * 7 / 13;

    // Calculate the width for stars
    int starWidth = 2 * 3 / 8 * 8; // 8 stars in total

    // Draw the box for stars
    drawRectangle(starWidth, starHeight, '*'); // Fill the box with stars (asterisks)
}

int main() {
    int boxWidth = 6; // Width of the box in inches
    int boxHeight = 4; // Height of the box in inches

    // Draw the box with white color (represented by space)
    drawRectangle(boxWidth * 8, boxHeight * 8, ' ');

    // Draw the Palestinian flag in the box (stripes)
    drawPalestinianStripes(boxWidth * 8, boxHeight * 8);

    // Draw the Palestinian flag in the box (stars)
    drawPalestinianStars(boxWidth * 8, boxHeight * 8);

    return 0;
}
