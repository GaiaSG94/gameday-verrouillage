import './index.css';

import { useCallback, useEffect, useState } from 'react';
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { clueText } from '../shared/puzzle';
import type { Clue, Lock } from '../shared/puzzle';

type Init = {
  day: string;
  username: string;
  streak: number;
  solvedToday: boolean;
  startedAt: number;
  locks: Lock[];
  clues: Clue[];
};

type Result = { won: boolean; streak: number; elapsedMs: number };

const EMOJI: Record<Lock, string> = {
  brass: '🟡',
  iron: '⚫',
  silver: '⚪',
  shadow: '🕶️',
};

const App = () => {
  const [init, setInit] = useState<Init | null>(null);
  const [order, setOrder] = useState<Lock[]>([]);
  const [result, setResult] = useState<Result | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [seconds, setSeconds] = useState(0);

  const load = useCallback(async () => {
    try {
      const res = await fetch('/api/init');
      const data = await res.json();
      if (data.status === 'error') throw new Error(data.message);
      setInit(data);
      setOrder([]);
      setResult(null);
      setSeconds(0);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'load failed');
    }
  }, []);

  useEffect(() => {
    void load();
  }, [load]);

  useEffect(() => {
    const timer = setInterval(() => setSeconds((s) => s + 1), 1000);
    return () => clearInterval(timer);
  }, []);

  const tap = (lock: Lock) => {
    setOrder((current) => (current.includes(lock) ? current : [...current, lock]));
  };

  const undo = () => setOrder((current) => current.slice(0, -1));

  const submit = async () => {
    try {
      const res = await fetch('/api/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ order, startedAt: Date.now() - seconds * 1000 }),
      });
      const data = await res.json();
      if (data.status === 'error') throw new Error(data.message);
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'submit failed');
    }
  };

  if (error) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#191423] text-[#e6dcf5]">
        <p>{error}</p>
      </div>
    );
  }
  if (!init) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#191423] text-[#8d7bb0]">
        <p className="animate-pulse">Wrapping the chains…</p>
      </div>
    );
  }

  const clock = `${String(Math.floor(seconds / 60)).padStart(2, '0')}:${String(seconds % 60).padStart(2, '0')}`;

  return (
    <div className="flex min-h-screen flex-col items-center gap-4 bg-[#191423] px-4 py-6 text-[#e6dcf5]">
      <header className="flex w-full max-w-md items-center justify-between">
        <h1 className="text-xl font-black tracking-[0.3em] text-[#c4a7ff]">VERROUILLAGE</h1>
        <div className="text-sm font-semibold text-[#8d7bb0]">
          <span className="mr-3">{clock}</span>
          <span>🔥 {result ? result.streak : init.streak}</span>
        </div>
      </header>
      <p className="max-w-md text-center text-[13px] leading-snug text-[#8d7bb0]">
        The chest wears four padlocks chained together. There is exactly one order that
        frees them all. Tap the locks in that order.
      </p>
      <div className="w-full max-w-md rounded-xl border-2 border-[#32284a] bg-[#221a33] p-3 text-center text-sm">
        {order.length === 0 ? (
          <span className="text-[#8d7bb0]">no lock pulled yet</span>
        ) : (
          order.map((lock, i) => (
            <span key={lock} className="mx-1 font-bold text-[#c4a7ff]">
              {i + 1}. {lock}
            </span>
          ))
        )}
      </div>
      <div className="flex w-full max-w-md justify-between gap-2">
        {init.locks.map((lock) => {
          const done = order.indexOf(lock);
          return (
            <button
              key={lock}
              onClick={() => tap(lock)}
              disabled={done >= 0}
              className="flex flex-1 flex-col items-center gap-1 rounded-xl border-2 border-[#32284a] bg-[#221a33] p-3 disabled:opacity-40"
            >
              <span className="text-2xl">{EMOJI[lock]}</span>
              <span className="text-[11px] font-bold capitalize text-[#e6dcf5]">{lock}</span>
              <span className="text-[11px] font-black text-[#c4a7ff]">
                {done >= 0 ? `#${done + 1}` : '?'}
              </span>
            </button>
          );
        })}
      </div>
      <ul className="w-full max-w-md space-y-1.5 rounded-xl border-2 border-[#32284a] bg-[#221a33] p-4 text-[13px]">
        {init.clues.map((clue, i) => (
          <li key={i} className="flex items-start gap-2">
            <span className="inline-block h-1.5 w-1.5 rounded-full bg-[#c4a7ff] mt-1.5" />
            {clueText(clue)}
          </li>
        ))}
      </ul>
      {!result ? (
        <div className="flex w-full max-w-md gap-2">
          <button
            onClick={undo}
            disabled={order.length === 0}
            className="w-28 rounded-full border-2 border-[#c4a7ff] py-3 text-sm font-black uppercase tracking-widest text-[#c4a7ff] disabled:opacity-40"
          >
            Undo
          </button>
          <button
            onClick={() => void submit()}
            disabled={order.length < init.locks.length}
            className="flex-1 rounded-full bg-[#c4a7ff] py-3 text-base font-black uppercase tracking-widest text-[#191423] transition-transform active:scale-[0.98] disabled:opacity-40"
          >
            Pull all ({order.length}/{init.locks.length})
          </button>
        </div>
      ) : (
        <div className="flex w-full max-w-md flex-col items-center gap-3 rounded-xl border-2 border-[#32284a] bg-[#221a33] p-5 text-center">
          <p className="text-2xl font-black tracking-widest">
            {result.won ? 'CHEST OPEN' : 'STILL CHAINED'}
          </p>
          <p className="text-sm text-[#8d7bb0]">
            {result.won
              ? `Freed in ${clock} — streak 🔥 ${result.streak}. Four new padlocks tomorrow.`
              : 'A link snapped. Try a different order.'}
          </p>
          <button
            onClick={() => setResult(null)}
            className="rounded-full border-2 border-[#c4a7ff] px-6 py-2 text-sm font-bold uppercase tracking-widest text-[#c4a7ff]"
          >
            Back to the chest
          </button>
        </div>
      )}
    </div>
  );
};

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
