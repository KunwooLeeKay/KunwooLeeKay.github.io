# reduce video file size

import os
import cv2
import numpy as np

def downsize_video(input_path, output_path, target_width=640, fps_multiplier=1.0):
    # Open the input video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {input_path}")
        return

    # Get original video properties
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) * fps_multiplier
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Calculate new dimensions
    aspect_ratio = original_height / original_width
    target_height = int(target_width * aspect_ratio)

    # Create VideoWriter object
    out = cv2.VideoWriter(output_path, fourcc, fps, (target_width, target_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame
        resized_frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_AREA)

        # Write resized frame to output video
        out.write(resized_frame)

    # Release resources
    cap.release()
    out.release()
    print(f"Downsized video saved to {output_path}")


if __name__ == "__main__":
    input_video_path = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/emg2qwerty_figures/demo.mov'
    output_video_path = input_video_path.replace('.mov', '_downsized.mp4')
    downsize_video(input_video_path, output_video_path, target_width=640, fps_multiplier=1.0)