export const LOCKS = ['brass', 'iron', 'silver', 'shadow'] as const;
export type Lock = (typeof LOCKS)[number];

export type Clue =
  | { kind: 'before'; a: Lock; b: Lock }
  | { kind: 'position'; lock: Lock; position: number }
  | { kind: 'notPosition'; lock: Lock; position: number };

export type OrderPuzzle = {
  day: string;
  clues: Clue[];
  solution: Lock[];
};

export const dayKeyUTC = (now: Date = new Date()): string => now.toISOString().slice(0, 10);

export const dailySeed = (day: string): number => {
  let hash = 2166136261;
  const input = 'verrouillage:' + day;
  for (let i = 0; i < input.length; i++) {
    hash ^= input.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
};

export const mulberry32 = (seed: number): (() => number) => {
  let a = seed >>> 0;
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
};

export const clueHolds = (clue: Clue, order: Lock[]): boolean => {
  const positionOf = (lock: Lock): number => order.indexOf(lock);
  switch (clue.kind) {
    case 'before':
      return positionOf(clue.a) >= 0 && positionOf(clue.b) >= 0 && positionOf(clue.a) < positionOf(clue.b);
    case 'position':
      return positionOf(clue.lock) === clue.position;
    case 'notPosition':
      return positionOf(clue.lock) !== clue.position;
  }
};

export const countSolutions = (clues: Clue[]): number => {
  const order: Lock[] = [];
  let total = 0;
  const used = new Set<Lock>();
  const walk = (): void => {
    if (order.length === LOCKS.length) {
      if (clues.every((clue) => clueHolds(clue, order))) total++;
      return;
    }
    for (const lock of LOCKS) {
      if (used.has(lock)) continue;
      used.add(lock);
      order.push(lock);
      walk();
      order.pop();
      used.delete(lock);
    }
  };
  walk();
  return total;
};

const randomClue = (rand: () => number, solution: Lock[]): Clue => {
  const a = LOCKS[Math.floor(rand() * LOCKS.length)] ?? 'brass';
  const b = LOCKS[Math.floor(rand() * LOCKS.length)] ?? 'iron';
  const position = solution.indexOf(a);
  const kind = Math.floor(rand() * 3);
  if (kind === 0 && a !== b) {
    const first = position < solution.indexOf(b) ? a : b;
    const second = first === a ? b : a;
    return { kind: 'before', a: first, b: second };
  }
  if (kind === 1) return { kind: 'position', lock: a, position };
  return { kind: 'notPosition', lock: a, position: (position + 1 + Math.floor(rand() * 3)) % LOCKS.length };
};

export const generateOrder = (day: string): OrderPuzzle => {
  const rand = mulberry32(dailySeed(day));
  const solution = [...LOCKS].sort(() => rand() - 0.5);
  const clues: Clue[] = [];
  let count = countSolutions(clues);
  for (let round = 0; round < 60 && count > 1; round++) {
    let best: Clue | null = null;
    let bestCount = count;
    for (let trial = 0; trial < 10; trial++) {
      const candidate = randomClue(rand, solution);
      if (!clueHolds(candidate, solution)) continue;
      if (clues.some((clue) => JSON.stringify(clue) === JSON.stringify(candidate))) continue;
      const next = countSolutions([...clues, candidate]);
      if (next >= 1 && next < bestCount) {
        best = candidate;
        bestCount = next;
        if (next === 1) break;
      }
    }
    if (!best) break;
    clues.push(best);
    count = bestCount;
  }
  return { day, clues, solution };
};

export const isCorrectOrder = (puzzle: OrderPuzzle, order: Lock[]): boolean =>
  puzzle.solution.every((lock, i) => order[i] === lock);

export const clueText = (clue: Clue): string => {
  const name = (lock: Lock): string => `the ${lock} lock`;
  switch (clue.kind) {
    case 'before':
      return `${name(clue.a)} opens before ${name(clue.b)}.`;
    case 'position':
      return `${name(clue.lock)} is the ${ordinal(clue.position)} to open.`;
    case 'notPosition':
      return `${name(clue.lock)} is not the ${ordinal(clue.position)} to open.`;
  }
};

const ordinal = (position: number): string => {
  const names = ['first', 'second', 'third', 'fourth'];
  return names[position] ?? `${position + 1}th`;
};
