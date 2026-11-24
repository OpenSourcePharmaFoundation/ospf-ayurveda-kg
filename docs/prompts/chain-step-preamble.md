# Chain Step Preamble

Standard constraints for every `./ospf chain` step. Anything that generates a
chain plan file (a skill template, or Claude writing one ad hoc) must copy the
block between the BEGIN/END markers **verbatim** as the first thing in each
step's prompt body, after the step's `## heading` and any metadata lines
(`model:`, `effort:`, `permissions:`, `preflight:`), before the step's task
text.

Constraint 3 (the closing `result:` line) is what lets `./ospf chain` detect that
a step finished. A background agent's state is inferred from the wording of its
last message; a bare `result:` line on the last line is the one shape that
resolves deterministically to "done".

This file is deliberately named without the `-prompt.md` suffix so the
`./ospf chain` picker does not list it as a runnable chain.

<!-- BEGIN CHAIN-STEP-PREAMBLE -->
**Standard chain-step constraints — follow these before and during the task below:**

1. **Read `CLAUDE.md` and the plan doc first.** Read `CLAUDE.md` in full and
   obey it throughout. If this step (or the chain) references a plan, outline
   or to-do doc (usually under `docs/` or `data/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
3. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.
<!-- END CHAIN-STEP-PREAMBLE -->
