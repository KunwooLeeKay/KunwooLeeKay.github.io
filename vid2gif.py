import cv2
import imageio

def video_to_gif(input_path, output_path, max_frames=None):
    """
    Convert video (mp4/mov) into a looping GIF using OpenCV + imageio.mimsave.
    Keeps the original playback speed and fps.
    """
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file {input_path}")

    # Get original FPS
    fps = cap.get(cv2.CAP_PROP_FPS)

    # get width and height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Video resolution: {width}x{height}, FPS: {fps}")

    frames = []
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Convert BGR → RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frames.append(frame_rgb)

        count += 1
        if max_frames and count >= max_frames:
            break

    frames = frames[::4] # downsample
    fps = fps / 3 # adjust fps accordingly

    cap.release()

    # duration per frame = 1/fps (in seconds)
    duration = 1 / fps 

    # Save GIF (loop=0 → infinite looping)
    imageio.mimsave(output_path, frames, loop=0)
    print(f"Saved looping GIF to {output_path} with original FPS ({fps:.2f})")


# Example usage:
source ="/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/cmlh_figures/qualitative_demo.mov"
# source = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/emg2qwerty_figures/demo.mov'
# source = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/3p_tracking_figures/3p_tracking_squat.mov'
# source = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/3p_tracking_figures/3p_tracking_SLH.mov'
# source = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/3p_tracking_figures/thumbnail.mp4'
# source = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/cmlh_figures/calibration.mov'
source = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/benchmark_figures/walking.mov'
source = '/Users/kunwoomac/CodeSpace/KunwooLeeKay.github.io/projects/emg2qwerty_figures/demo_thumbnail.mov'
out = source.replace(".mov", ".gif")
# out = source.replace(".mp4", ".gif")

video_to_gif(source, out)