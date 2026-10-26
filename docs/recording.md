# Screen recording and evidence capture

## Simple capture: macOS

Press **Shift-Command-5**, choose a selected portion or app window, set a private save location, and record only the steps needed to show the behavior. Apple's [screen recording guide](https://support.apple.com/en-us/102618) covers controls and shortcuts. Check macOS Screen & System Audio Recording permission for the chosen app. Make a short test clip first.

## Repeatable capture: OBS Studio

Install OBS from its [official macOS guide](https://obsproject.com/kb/mac-installation). Create a scene with **macOS Screen Capture** for the relevant window or display, plus optional microphone only if narration helps. Start with 1920×1080 at 30 fps and MKV recording; OBS can remux MKV to MP4 after a clean stop. Use a private folder excluded from Git. Keep notifications closed and other apps out of frame.

**Local verification on 2026-10-26:** Screen Recording permission for OBS was enabled in macOS Settings, a macOS Screen Capture source showed a live Retina display preview, and microphone/system audio sources were muted. The observed OBS recording settings still showed **Hybrid MOV** and **1280×720 output**; the 1080p/MKV settings above are recommendations to apply in OBS before recording if that format is required. No saved test clip was inspected, so verify the chosen output path, format, resolution, and playback with a short private clip before using video as evidence.

Suggested scene order:

1. A short title card with test date, program/CTF identifier, role, and a **redacted** target label.
2. Baseline behavior with the expected authorized account or state.
3. One clear request/response or UI change that demonstrates the finding.
4. A brief result view. End the recording before unrelated browsing.

Keep HTTP evidence as a redacted request/response pair as well as video. A video cannot substitute for exact request fields or role labels. When video contains tokens, cookies, passwords, personal data, or private program details, redact a copy and retain the original locally under the program's rules. Do not upload raw Caido project files or recordings to the public workbench.

Use consistent filenames such as `finding-01-role-a-redacted.mkv` and record SHA-256 hashes in a private evidence ledger. Mark redactions honestly; do not alter the response in a way that changes what the evidence demonstrates.
