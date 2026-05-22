import cv2

vid = cv2.VideoCapture('assets/original_cinematic.mp4')
fps = vid.get(cv2.CAP_PROP_FPS)
frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
duration = frames / fps

print(f"Video Stats:")
print(f"  Resolution: {w}x{h}")
print(f"  FPS: {fps}")
print(f"  Total Frames: {frames}")
print(f"  Duration: {duration:.2f} seconds")
vid.release()
