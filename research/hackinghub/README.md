# HackingHub public-post extraction

This directory preserves the output of a separate research task completed on **2026-10-14**, linked to the [HackingHub LinkedIn feed](https://www.linkedin.com/company/hackinghub/posts/). The extraction is **not** an all-time archive and does not include the complete text or media of every post.

The original task processed **315 distinct feed entries** until the feed stopped loading and **90 separately indexed post pages** with overlap. It summarized **115 tips**, **44 tools/utilities**, and **26 websites/learning resources**. It inspected **31 images**, **7 video posters**, and selected frames from **3 demos**. These counts describe the research sample, not all HackingHub content or unique posts across both sources.

| File | Purpose |
|---|---|
| `hackinghub-guide.md` | Human-readable synthesis with source and coverage qualifications |
| `tips.csv` | Source-labeled paraphrased tips and testing leads |
| `tools-and-websites.csv` | Mentioned tools/resources and evidence labels |
| `post-index.csv` | Post metadata and coverage status |
| `outbound-links.csv` | Extracted external links and recovery status |
| `video-coverage.csv` | Which video content was or was not inspected |

An author caption, an inspected frame, and an analyst's code-review observation are distinct evidence types in these files. Many videos were not transcribed; image coverage is partial. A title promising a technique does not establish missing steps. Source links can change or require a LinkedIn account. Verify the current original post before attributing a technical claim or recommending a tool.

The extraction is useful for prioritizing application understanding, targeted recon, documentation review, HTTP parsing differences, and careful impact validation. It does not establish that any named target is currently in scope or vulnerable.
