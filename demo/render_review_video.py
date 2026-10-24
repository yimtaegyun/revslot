"""Render a captioned review film from real, inspected Playwright captures.

Requires Pillow, ffmpeg and Inkscape. This is not the eligible live-model take.
Usage: python demo/render_review_video.py /absolute/output/directory
"""
from pathlib import Path
import subprocess
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
SHOTS = ROOT / "demo/screenshots"
FONT = Path("/usr/share/fonts/truetype/dejavu")
BG, INK, MUTED, GREEN = "#f7f8f4", "#23382d", "#5c6d55", "#456b45"


def font(size, bold=False, serif=False):
    name = "DejaVuSerif" if serif else "DejaVuSans"
    return ImageFont.truetype(str(FONT / (name + ("-Bold" if bold else "") + ".ttf")), size)


def wrapped(draw, xy, value, face, fill, width, spacing=11):
    x, y = xy
    for paragraph in value.split("\n"):
        line = ""
        for word in paragraph.split():
            candidate = (line + " " + word).strip()
            if line and draw.textlength(candidate, font=face) > width:
                draw.text((x, y), line, font=face, fill=fill)
                y += face.size + spacing
                line = word
            else:
                line = candidate
        draw.text((x, y), line, font=face, fill=fill)
        y += face.size + spacing + 7
    return y


architecture = OUT / "architecture.png"
subprocess.run(["inkscape", str(ROOT / "docs/architecture.svg"),
                "--export-type=png", f"--export-filename={architecture}",
                "--export-width=1400"], check=True, capture_output=True)

# Crop coordinates only select regions of genuine captures; no UI values are redrawn.
scenes = [
    (10, "01 / THE PROBLEM", "Cancelled time\nexpires to zero.",
     "An $80 appointment. Three hours left. An empty hour that can never be stored.",
     "01-merchant-ready.png", (255, 495, 1410, 1075), "Beauty & wellness appointments"),
    (15, "02 / THE TRIGGER", "One cancellation.\nA complete loop.",
     "The merchant cancels. The real application evaluates demand, prices and policy, then publishes an offer.",
     "02-agent-first-offer.png", (250, 340, 1415, 1090), "$80 at risk · $64 first shared offer"),
    (20, "03 / THE PRICE TOOL", "Calculated prices.\nEnforced limits.",
     "Eight candidate discounts. Expected revenue = price × fill probability. The selected $64 price respects the $50 floor.",
     "02-agent-first-offer.png", (250, 1090, 1415, 1520), "A deterministic tool sets the price"),
    (15, "04 / RUNTIME HONESTY", "Live inference\nis still a gate.",
     "Nebius/NVIDIA and optional Tavily adapters are implemented. No keys are connected in this recording. It uses the labeled rules preview.",
     "09-integrations.png", (250, 245, 1415, 1005), "Preview evidence ≠ verified provider usage"),
    (15, "05 / THE FIRST OFFER", "One slot.\nOne shared price.",
     "Twelve opted-in synthetic profiles match within 3 km. Only notification priority changes. Sandbox inbox records replace real messages.",
     "02-agent-first-offer.png", (900, 495, 1415, 1090), "$64 · 20% off · 12 eligible profiles"),
    (20, "06 / OBSERVE AND REPLAN", "Still unsold?\nUpdate the strategy.",
     "After 20 simulated minutes, the loop re-evaluates. Price becomes $56; reach expands to 6 km and 24 eligible profiles.",
     "03-reprice.png", (250, 340, 1415, 1090), "The demo clock is explicitly accelerated"),
    (15, "07 / MERCHANT CONTROL", "Autonomy, within\nyour boundaries.",
     "$50 minimum price. 40% maximum discount. Approval above 35%. Low support requires review. Approval never overrides the floor.",
     "07-guardrails.png", (250, 245, 1415, 890), "Opt-out · same price · revision checks · audit"),
    (15, "08 / THE OUTCOME", "$56 recovered.\n70% of slot value.",
     "A consumer confirms the current sandbox reservation. The booking changes real application state and merchant metrics. No money is collected.",
     "05-recovered.png", (250, 340, 1415, 635), "Synthetic business data · 20 demo minutes to fill"),
    (20, "09 / MEASURABLE, WITH LIMITS", "Compare the policy.\nKeep the bad news.",
     "Across 1,000 synthetic scenarios: $53.17 per cancelled slot vs $48.70 at fixed 20%. Average discount is higher; unnecessary discount is 100% for both.",
     "06-analytics.png", (250, 970, 1415, 1370), "Reproducible simulation, not proven market uplift"),
    (15, "10 / THE ARCHITECTURE", "A stateful workflow.\nInspectable actions.",
     "Planning, pricing, policy, matching, observation and booking have explicit roles. Deterministic tools protect every published offer.",
     "architecture", None, "Next.js · FastAPI · LangGraph · deterministic tools"),
    (10, "11 / NEXT: LIVE VERIFICATION", "Cancelled time.\nRecovered value.",
     "The implemented recovery loop passes browser verification. Live Nebius/NVIDIA, hosting authorization and the final submission take remain open.",
     "05-recovered.png", (250, 340, 1415, 635), "github.com/yimtaegyun/revslot"),
]

elapsed = 0
concat = []
for i, (duration, label, title, body, shot, crop, caption) in enumerate(scenes):
    im = Image.new("RGB", (1920, 1080), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((64, 57, 115, 108), 13, fill=GREEN)
    d.arc((74, 67, 105, 98), 60, 350, fill="#ffffff", width=3)
    d.text((132, 53), "revslot.", font=font(42, True), fill=INK)
    d.rounded_rectangle((1365, 62, 1856, 104), 11, fill="#e8eddf")
    d.text((1386, 72), "REVIEW WALKTHROUGH / PREVIEW", font=font(17, True), fill=GREEN)
    d.line((64, 140, 1856, 140), fill="#dce3d5", width=2)
    d.text((64, 188), label, font=font(19, True), fill=GREEN)
    y = wrapped(d, (64, 244), title, font(47, True, True), INK, 600, 9)
    y = wrapped(d, (68, y + 27), body, font(27), MUTED, 567, 13)
    d.rounded_rectangle((64, 823, 652, 932), 12, fill="#eaf0e1")
    wrapped(d, (85, 842), caption, font(21, True), GREEN, 542, 6)
    source = Image.open(architecture if shot == "architecture" else SHOTS / shot).convert("RGB")
    if crop:
        source = source.crop(crop)
    fitted = ImageOps.contain(source, (1120, 712), Image.Resampling.LANCZOS)
    d.rounded_rectangle((704, 182, 1859, 939), 15, fill="#dfe5d8")
    d.rounded_rectangle((698, 176, 1853, 933), 15, fill="#ffffff", outline="#d2dcc8", width=2)
    im.paste(fitted, (715 + (1120 - fitted.width) // 2, 199 + (712 - fitted.height) // 2))
    d.text((64, 989), "SYNTHETIC DATA  /  SANDBOX BOOKING  /  LIVE PROVIDERS NOT CONNECTED", font=font(18, True), fill=MUTED)
    d.text((1710, 989), f"{elapsed//60:02}:{elapsed%60:02} / 02:50", font=font(18), fill=MUTED)
    d.rectangle((0, 1072, int(1920 * (elapsed + duration) / 170), 1080), fill="#7f9f61")
    path = OUT / f"scene-{i:02}.png"
    im.save(path)
    concat.extend([f"file '{path}'", f"duration {duration}"])
    elapsed += duration
assert elapsed == 170
concat.append(f"file '{path}'")
(OUT / "frames.txt").write_text("\n".join(concat) + "\n")
subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0",
                "-i", str(OUT / "frames.txt"), "-t", "170", "-r", "24", "-c:v", "libx264",
                "-preset", "veryfast", "-tune", "stillimage", "-crf", "23", "-pix_fmt", "yuv420p",
                "-movflags", "+faststart", str(OUT / "revslot-review.mp4")], check=True)
print(OUT / "revslot-review.mp4")
