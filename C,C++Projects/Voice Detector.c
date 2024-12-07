#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SAMPLE_RATE 44100
#define FRAME_SIZE 512
#define HOP_SIZE 256

double calculate_spectral_centroid(double *frame, int frame_size) {
    double spectral_centroid = 0.0;
    double total_energy = 0.0;

    for (int i = 0; i < frame_size; i++) {
        double magnitude = frame[i];
        spectral_centroid += magnitude * i;
        total_energy += magnitude;
    }

    if (total_energy > 0.0) {
        spectral_centroid /= total_energy;
    }

    return spectral_centroid;
}

int main() {
    FILE *file;
    char *file_path = "path/to/audio/file.raw";
    short buffer[FRAME_SIZE];
    double spectral_centroid, sum_spectral_centroids = 0.0;
    int frames_count = 0;

    // Open raw audio file
    file = fopen(file_path, "rb");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Process audio frames
    while (fread(buffer, sizeof(short), FRAME_SIZE, file) == FRAME_SIZE) {
        double frame[FRAME_SIZE];
        for (int i = 0; i < FRAME_SIZE; i++) {
            frame[i] = (double)buffer[i] / 32768.0; // Convert to range [-1, 1]
        }
        spectral_centroid = calculate_spectral_centroid(frame, FRAME_SIZE);
        sum_spectral_centroids += spectral_centroid;
        frames_count++;
    }

    // Close file
    fclose(file);

    // Calculate mean spectral centroid
    double mean_spectral_centroid = sum_spectral_centroids / frames_count;

    // Set a threshold for voice detection
    double threshold = mean_spectral_centroid * 1.5;

    // Check if voice is detected
    if (mean_spectral_centroid > threshold) {
        printf("Voice detected!\n");
    } else {
        printf("No voice detected.\n");
    }

    return 0;
}
