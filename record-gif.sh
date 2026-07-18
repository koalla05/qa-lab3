#!/usr/bin/env bash
# Record the AI agent run as a GIF (what the teacher asked for).
# Screen-records via ffmpeg while the agent drives the browser, then converts
# the video to a GIF. Works from any directory.
#
# First run will trigger a macOS "Screen Recording" permission prompt for your
# terminal — allow it, then run this script again.
set -e

PROJECT="/Users/olesiamykhailyshyn/Documents/KSE/SE660 Software Quality Assurance and Testing/Labs/qa-lab3"
AGENTS="$PROJECT/agents"
OUT_DIR="$PROJECT/lab4-olesia-screenshot"
MP4="$OUT_DIR/agent-run.mp4"
GIF="$OUT_DIR/agent-demo.gif"

# 1. ffmpeg required.
if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg not found. Install it:  brew install ffmpeg"
  exit 1
fi

mkdir -p "$OUT_DIR"

# 2. Detect the screen-capture device index for avfoundation.
SCREEN_IDX=$(ffmpeg -f avfoundation -list_devices true -i "" 2>&1 \
  | grep -i "Capture screen" | head -1 | sed -E 's/.*\[([0-9]+)\].*/\1/')
if [ -z "$SCREEN_IDX" ]; then
  echo "Could not find a screen capture device. Grant Screen Recording permission"
  echo "to your terminal in System Settings > Privacy & Security, then retry."
  exit 1
fi
echo "Recording screen device index: $SCREEN_IDX"

# 3. Start screen recording in the background (10 fps is plenty for a demo).
ffmpeg -y -f avfoundation -framerate 10 -i "${SCREEN_IDX}:none" \
  -pix_fmt yuv420p "$MP4" >/dev/null 2>&1 &
FFMPEG_PID=$!
sleep 2  # let ffmpeg warm up

# 4. Run the agent (foreground) — recording captures the whole run.
cd "$AGENTS"
source .venv/bin/activate
python end_to_end_runner-olesia.py || true

# 5. Stop recording.
kill -INT "$FFMPEG_PID" 2>/dev/null || true
wait "$FFMPEG_PID" 2>/dev/null || true

# 6. Convert MP4 -> GIF (800px wide, 10 fps).
echo "Converting to GIF..."
ffmpeg -y -i "$MP4" -vf "fps=10,scale=800:-1:flags=lanczos" "$GIF" >/dev/null 2>&1

echo "Done. GIF saved to: $GIF"
