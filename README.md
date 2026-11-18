# Verrouillage

A daily order-deduction game for Reddit, built on [Devvit Web](https://developers.reddit.com/).

The chest wears four chained padlocks (brass, iron, silver, shadow). The tag gives
a few order facts - "the brass lock opens before the iron lock", "the silver lock
is the third to open", "the shadow lock is not the first" - and the puzzle is
generated so the opening order is unique.

## How to play

1. Read the tag.
2. Tap the locks in the order you pull them (Undo to step back).
3. Tap Pull all when the four are queued.

One chest per day, the same for everyone; streaks stored per user in Redis.

## Stack

- React 19 + Tailwind 4 + Vite (client inside a Reddit post)
- Hono server on Devvit (`/api/init`, `/api/submit`), Redis persistence
- Deterministic daily generation (UTC seed), uniqueness brute-forced (24 orders),
  unit-tested

## Development

```bash
npm install
npm run dev
npm test
npm run type-check
npm run build
```

## Submission (Reddit's Game of the Day Hackathon)

- App listing: `developers.reddit.com/apps/gameday-verrouillage` (private until judging ends)
- Demo post: public test subreddit, post running the game
