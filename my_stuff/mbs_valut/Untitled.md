# Obsidian's Speed: Explained Simply

The short answer: **Obsidian is fast because it does almost nothing.** It reads plain text files off your disk, and that's basically it. OneNote and Word do an enormous amount of work behind the scenes that you never asked for. Let me break this down.

## The core difference: plain text vs. complex documents

When you save a note in Obsidian, it writes a `.md` file — a plain text file with a tiny bit of markup (like `# Heading` or `**bold**`). That's it. The file might be a few kilobytes.

When you save a Word document, you're saving a `.docx`, which is actually a **zipped folder full of XML files** describing fonts, styles, embedded objects, revision history, formatting rules, and dozens of other things. OneNote is even heavier — it stores notes in a proprietary binary format with sync metadata baked in.

Think of it like this: Obsidian is reading a handwritten sticky note. Word is reading a legal contract with footnotes, signatures, and a notary stamp. The sticky note is faster to read every single time.

## What's actually happening under the hood

A few architectural choices make Obsidian quick:

**It's a local-first app.** Obsidian reads and writes files directly on your computer's disk. There's no server call, no cloud round-trip, no "checking if someone else edited this." Your SSD can read a markdown file in microseconds. OneNote, by contrast, is built around constant syncing — it's always thinking about the cloud, even when you're just typing.

**It only loads what you're looking at.** Obsidian doesn't load your entire vault of 10,000 notes into memory. It opens the one note you clicked on. The rest just sit as files on disk until needed. Word loads and renders the whole document because a document is meant to be one continuous thing.

**The "database" is just an index.** Obsidian keeps a lightweight index of your notes and the links between them — basically a map of "which note connects to which." This index is small and lives in memory, so jumping between notes and showing the graph view feels instant. It's not querying a heavy database; it's looking at a cheat sheet it built once.

**Rendering markdown is cheap.** Turning `# Hello` into a big bold "Hello" is trivial computation. Word has to lay out precise pages — exact margins, where text wraps, how images flow, what the printed page looks like. That layout engine (WYSIWYG — "what you see is what you get") is genuinely expensive to run.

## The honest tradeoff

The reason Word and OneNote are "slow" is that they're doing things Obsidian deliberately refuses to do: pixel-perfect print layout, rich embedded media, real-time collaboration, deep formatting. Obsidian gains its speed by handing those responsibilities away. Your files are _just text_, so the app stays lean — but you also don't get a polished printable page out of the box.

It's worth noting Obsidian is built on **Electron** (a Chromium browser wrapped as a desktop app), which is usually considered a _heavy_ foundation. The fact that it still feels snappy comes down to the simplicity of what it's manipulating: text files and a small link index, rather than complex document objects.

---

Want me to go deeper on any piece — like how the link index / graph view actually works, or why markdown-based tools scale so well to thousands of notes?