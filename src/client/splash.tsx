import './index.css';

import { context, requestExpandedMode } from '@devvit/web/client';
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

export const Splash = () => {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-3 bg-[#191423] px-6 text-center text-[#e6dcf5]">
      <div className="text-3xl">⛓️</div>
      <h1 className="text-3xl font-black tracking-[0.25em] text-[#c4a7ff]">VERROUILLAGE</h1>
      <p className="max-w-[240px] text-[13px] leading-snug text-[#8d7bb0]">
        Four chained padlocks, one valid order. Hi {context.username ?? 'burglar'}.
      </p>
      <button
        onClick={(e) => requestExpandedMode(e.nativeEvent, 'game')}
        className="mt-2 rounded-full bg-[#c4a7ff] px-8 py-2.5 text-sm font-black uppercase tracking-widest text-[#191423] transition-transform active:scale-[0.98]"
      >
        Work the locks
      </button>
    </div>
  );
};

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Splash />
  </StrictMode>
);
