"""Generates the favicon set from the Rumstar star. Run once: python3 src/make_icons.py"""
import os
from PIL import Image, ImageDraw

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ICONS = os.path.join(ROOT, "assets", "icons")
GOLD, NAVY = (255, 199, 77, 255), (7, 9, 18, 255)
# The brand star: four cubic curves through the tips, in a 32 unit box
SEGMENTS = [((16, 1), (17.5, 11), (21, 14.5), (31, 16)), ((31, 16), (21, 17.5), (17.5, 21), (16, 31)),
            ((16, 31), (14.5, 21), (11, 17.5), (1, 16)), ((1, 16), (11, 14.5), (14.5, 11), (16, 1))]


def star_points(scale, offset):
    pts = []
    for p0, p1, p2, p3 in SEGMENTS:
        for i in range(40):
            t = i / 40
            x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
            y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
            pts.append((offset + x * scale, offset + y * scale))
    return pts


def icon(size, bg=None, pad=0.0, radius=0.0):
    ss = 4  # supersample for smooth edges
    big = size * ss
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if bg:
        d.rounded_rectangle([0, 0, big - 1, big - 1], radius=int(big * radius), fill=bg)
    inner = big * (1 - 2 * pad)
    d.polygon(star_points(inner / 32, big * pad), fill=GOLD)
    return img.resize((size, size), Image.LANCZOS)


os.makedirs(ICONS, exist_ok=True)
icon(180, NAVY, pad=0.2).save(os.path.join(ICONS, "apple-touch-icon.png"))
icon(192, NAVY, pad=0.18, radius=0.22).save(os.path.join(ICONS, "icon-192.png"))
icon(512, NAVY, pad=0.18, radius=0.22).save(os.path.join(ICONS, "icon-512.png"))
icon(512, NAVY, pad=0.28).save(os.path.join(ICONS, "icon-maskable-512.png"))
icon(48, pad=0.02).save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
with open(os.path.join(ICONS, "icon.svg"), "w") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 1 C17.5 11 21 14.5 31 16 C21 17.5 17.5 21 16 31 C14.5 21 11 17.5 1 16 C11 14.5 14.5 11 16 1Z" fill="#ffc74d"/></svg>')
print("icons written")
