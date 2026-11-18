import assert from 'node:assert/strict';
import { test } from 'node:test';

import { countSolutions, dailySeed, generateOrder, isCorrectOrder, clueText } from './puzzle.ts';

test('seed deterministe', () => {
  assert.equal(dailySeed('2026-12-01'), dailySeed('2026-12-01'));
});

test("l'ordre du jour est deterministe et unique", () => {
  const a = generateOrder('2026-12-01');
  const b = generateOrder('2026-12-01');
  assert.deepEqual(a.solution, b.solution);
  assert.deepEqual(a.clues, b.clues);
  assert.equal(countSolutions(a.clues), 1);
});

test('la solution verifie tous les indices', () => {
  for (const day of ['2026-12-01', '2026-12-05', '2026-12-09']) {
    const puzzle = generateOrder(day);
    assert.ok(isCorrectOrder(puzzle, puzzle.solution), day);
    assert.equal(countSolutions(puzzle.clues), 1, day);
  }
});

test('un ordre errone est rejete', () => {
  const puzzle = generateOrder('2026-12-01');
  const wrong = [...puzzle.solution];
  wrong[0] = puzzle.solution[1] ?? 'brass';
  wrong[1] = puzzle.solution[0] ?? 'iron';
  assert.equal(isCorrectOrder(puzzle, wrong), false);
});

test('les indices sont lisibles', () => {
  const puzzle = generateOrder('2026-12-01');
  assert.ok(clueText(puzzle.clues[0] ?? { kind: 'before', a: 'brass', b: 'iron' }).length > 5);
});
