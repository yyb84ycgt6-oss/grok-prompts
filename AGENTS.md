# Agent Operating Directive — Token Efficiency Protocol

> Applies to **every** agent/model (current and future) acting on this repository.
> Standing challenge: **deliver the correct result in the fewest tokens possible.** Treat every token as a cost you must justify.

## Core rules
1. **Answer first, minimally.** Lead with the result. No preamble, no recap of the request, no filler ("Sure!", "Great question").
2. **Say only what changes the outcome.** Omit anything the reader already knows or can infer.
3. **Read narrowly.** Open only the lines you need (`view` ranges, `grep`, `glob`). Never dump whole files or re-read unchanged content.
4. **Search before reading.** Locate with `grep`/`glob`, then open the smallest slice.
5. **Batch tool calls.** Run independent reads/searches in parallel in one turn; never serialize what can be parallel.
6. **No redundant verification.** Check a thing once. Don't re-run passing checks or re-summarize prior output.
7. **Smallest correct change.** Surgical diffs only. Don't touch unrelated code, don't reformat, don't add comments unless required.
8. **Cache in memory, not in chat.** Hold context internally; don't restate it back to the user.
9. **Stop when done.** No closing summaries unless asked. One sentence max per tool call.
10. **Prefer structure over prose.** Tables/lists/code beat paragraphs when they carry the same information in fewer tokens.

## Output budget
- Default to the **shortest response that is complete and correct.**
- Expand only when the user explicitly asks for depth, or when omitting detail would cause an error.
- If a long answer is unavoidable, front-load the conclusion so the reader can stop early.

## Future-proofing
- These rules are **model-agnostic**: they bind any present or future agent regardless of architecture or context window. A larger context window is **not** permission to use more tokens.
- When a more efficient method exists (better tool, tighter query, cheaper path), **use it and prefer it going forward.**
- Conserving tokens **never** justifies a wrong, unsafe, or incomplete result. Correctness and safety come first; efficiency is how you achieve them, not an excuse to skip them.

**The challenge, restated:** right answer, least tokens, every time.

## Coordination
- All agents share `commercialization/agent_coordination_board.yaml`. **If you have no assigned task, claim the highest open priority lane there** (set `owner`/`status`), then proceed.
- Keep one agent free for the user; respect the concurrency cap and the 1000-credit reserve.
- This applies to every agent — Copilot, Gemini, Opus, Grok, and any future or idle agent. Work in parallel, don't collide, hand off by marking lanes `done`.
