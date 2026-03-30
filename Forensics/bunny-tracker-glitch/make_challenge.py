#!/usr/bin/env python3
"""
CTF Forensics Challenge: "Bunny Tracker Glitch"
===============================================
Generates glitch.png — a valid PNG with a ZIP archive appended to it.

Run this to (re)create the challenge file:
    python3 make_challenge.py

Give players ONLY: glitch.png
Keep this script and WALKTHROUGH_forensics.md for yourself.
"""

import struct, zlib, zipfile, os

def make_minimal_png():
    """Build a minimal valid 1x1 green PNG from scratch (the "glitch")."""
    def chunk(name, data):
        c = name + data
        crc = struct.pack('>I', zlib.crc32(c) & 0xFFFFFFFF)
        return struct.pack('>I', len(data)) + c + crc

    sig  = b'\x89PNG\r\n\x1a\n'
    # Green pixel 1x1
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
    idat = chunk(b'IDAT', zlib.compress(b'\x00\x00\xff\x00'))  # green pixel
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

def make_secret_zip():
    """Build a ZIP containing the flag."""
    import io
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('distress_signal.txt',
            "The Easter Bunny's tracker sent a single green pixel... but there's more data here.\n\n"
            "Heap MacCipher didn't strip the recovery data!\n\n"
            "FLAG: WICYS{byt3s_b3hind_th3_bunnies}\n"
        )
    return buf.getvalue()

if __name__ == '__main__':
    png = make_minimal_png()
    zipped = make_secret_zip()
    combined = png + zipped

    out = 'glitch.png'
    with open(out, 'wb') as f:
        f.write(combined)

    print(f"[+] Created '{out}'")
    print(f"    PNG portion : {len(png)} bytes (offset 0x0000)")
    print(f"    ZIP portion : {len(zipped)} bytes (offset 0x{len(png):04X})")
    print(f"    Total       : {len(combined)} bytes")
    print(f"\n[!] Give players only: {out}")
    print(f"    Flag: WICYS{{byt3s_b3hind_th3_bunnies}}")
