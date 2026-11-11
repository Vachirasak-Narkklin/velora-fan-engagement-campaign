# VELORA Fan Engagement Campaign

Data-driven launch plan for **VELORA**, a fictional T-pop girl group, using YouTube data from 8 real T-pop girl groups.

> **Fictional artist — concept project.** VELORA, its members and its album are made up for this portfolio. All market data comes from public YouTube data.

## Summary

I collected 8,079 videos from 8 T-pop girl group channels and used them to answer three launch questions for VELORA's debut single.

| Question | Answer |
|---|---|
| When should the debut MV come out? | **Thursday 19:00.** Release day and time have only a small effect on views, so I picked a safe slot with less competition |
| What content should VELORA post? | **MV for reach, Shorts for fan engagement, and more dance videos.** MVs are 0.5% of uploads but 35% of views. Shorts get 76% of likes. Dance practice videos do well but almost no group makes them |
| When should Shorts be posted? | **19:30-20:00 on weekdays, 18:00 on weekends.** Fans comment most between 20:00 and 22:00 |

The three results fit together: the MV goes up at 19:00, one hour before fans are most active.

## Data

- **Source:** YouTube Data API v3
- **Groups:** 4EVE, PiXXiE, Pretzelle, ALALA, MXFRUIT, VIIS, EMPRESS, FELIZZ
- **Collected:** 10 November 2026
- **Size:** 8,079 videos, 2,745 comment times (after cleaning)

MXFRUIT posts its videos on its label's channel (TADA LABELS), so only videos with "MXFRUIT" in the title are kept.

Only comment **times** are saved. No usernames or comment text.

## 1. Release timing

**Notebook:** [`release_timing.ipynb`](notebooks/release_timing.ipynb)

YouTube only gives total views today, not views in the first 24 hours. So each MV is scored by **views per day**, compared with the other MVs of the same group (score 1.0 = normal for that group).

![Release day](reports/figures/release_day.png)
![Release hour](reports/figures/release_hour.png)

**The first result did not hold up.** With all groups, Thursday (1.39) and 18:00 (1.51) looked best. But 4EVE has 33 of the 69 MVs. Without 4EVE, both results go away:

| | All groups | Without 4EVE |
|---|---|---|
| Thursday | 1.39 (n=21) | 1.03 (n=10) |
| 18:00 | 1.51 (n=9) | 0.80 (n=3) |
| Friday | 0.91 (n=14) | 0.86 (n=9) |
| 19:00 | 0.94 (n=23) | 1.12 (n=6) |
| 20:00 | 1.00 (n=19) | 1.00 (n=19) |

The only stable results are that Friday is a little below normal and 19:00-20:00 is about normal. Since timing does not add many views, I chose the slot with less competition: Thursday 19:00 has 5 competing MVs, compared with 10 on Wednesday 19:00.

**Hypothesis check:** the artist brief guessed that Friday evening would be best. The data does not support this.

## 2. Content mix

**Notebook:** [`shorts_vs_mv.ipynb`](notebooks/shorts_vs_mv.ipynb)

Videos from the last 2 years (4,898 videos) are split into Shorts (60 seconds or less), MVs, dance practice, live and other.

![Content type](reports/figures/content_type.png)

Every group is mainly a Shorts channel (73-94% of uploads). But each content type does a different job:

| Type | % of uploads | % of views | % of likes |
|---|---|---|---|
| Short | 86.9% | 49.4% | 76.2% |
| MV | 0.5% | 34.7% | 9.3% |
| Dance practice | 0.8% | 3.6% | 1.9% |

- **MV = reach.** One MV gets about 140x the daily views of a normal video, but has the lowest engagement rate (1.4-1.8%)
- **Shorts = fan engagement.** Highest engagement rate (7.0-7.4%)
- **Dance practice = a gap in the market.** About 4x the daily views of a normal video, but only 0-2% of uploads for every group

Per-video results are the same without 4EVE.

**Plan for VELORA:** 1 MV per single, Shorts as daily content (around 80-85% of uploads), and 2-3 dance videos per single to support the "No Filter" dance challenge.

## 3. Fan active hours

**Notebook:** [`comment_hours.ipynb`](notebooks/comment_hours.ipynb)

Comment times from up to 100 recent videos per group. Comments in the first 48 hours after a video is posted are removed, because they only show when the video came out. Each group counts the same.

![Comment hours](reports/figures/comment_hours.png)

- Busiest hours: **20:00 (7.5%), 21:00 (7.4%), 22:00 (6.5%)**. If comments were spread evenly, each hour would have about 4.2%
- 18:00-23:00 has 38% of comments in only 6 hours
- Same without 4EVE, and 3 of 4 groups peak at 20:00-21:00 (VIIS peaks at 09:00)
- Weekdays have a sharp peak at 20:00 (8.9%). Weekends are flatter, with 18:00-23:00 all around 6-7%

## Checks and limitations

**Robustness check:** 4EVE is much bigger than the other groups, so every result was also checked without 4EVE. This changed the release timing result.

**Limitations:**
- Views per day is not the same as views in the first 24 hours
- PiXXiE, VIIS and ALALA post their MVs on other channels, so the release timing analysis uses only 5 groups
- Shorts are guessed by length. YouTube also changed how Shorts views are counted in 2025, so likes are used as a second check
- Content type is based on the video title, so some videos may be in the wrong type
- Comment time is not the same as watch time, and some fans live outside Thailand
- Only 4 groups have enough comments for the comment hours analysis

## Project structure

```
velora-fan-engagement-campaign/
├── notebooks/
│   ├── get_youtube_data.ipynb   # collect channel and video data
│   ├── release_timing.ipynb     # best day and time to release an MV
│   ├── shorts_vs_mv.ipynb       # content type performance
│   └── comment_hours.ipynb      # when fans are active
├── reports/figures/             # charts used in this README
├── src/test_connection.py       # check that the API key works
├── data/                        # not included (see below)
└── requirements.txt
```

## How to run

Data is not included. Run the notebooks with your own API key to download it.

1. Get a YouTube Data API v3 key from Google Cloud Console
2. Set up the project:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project folder:
   ```
   YOUTUBE_API_KEY=your_key_here
   ```
4. Run the notebooks in this order: `get_youtube_data` → `release_timing` → `shorts_vs_mv` → `comment_hours`

Results will be a little different from this README because view counts change every day.

## Tools

Python, pandas, matplotlib, YouTube Data API v3, Jupyter

## Next

- Campaign blueprint: launch timeline, pre-order tiers with margin, and KPI plan
- Key visuals and social media designs for VELORA
