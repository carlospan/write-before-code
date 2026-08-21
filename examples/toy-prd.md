# EXAMPLE ONLY — not a real product

**[English](toy-prd.md)** · **[中文](toy-prd.zh-CN.md)**

Toy PRD for a fictional **Sticky Notes CLI**. Use for template demos only.

---

## Positioning

A local CLI for personal sticky notes: add, list, delete by id. Single-user; no accounts or sync.

## Out of scope

Cloud sync, multi-user, rich formatting, GUI.

## Features

### F-1 Add note

- **What**: Create a note from text; assign a stable id.
- **Acceptance**: WHEN the user runs `notes add "buy milk"` THEN a new note with an id is stored and echoed.

### F-2 List notes

- **What**: Print all notes (id + text).
- **Acceptance**: WHEN the user runs `notes list` THEN every stored note appears, one per line.

### F-3 Delete by id

- **What**: Remove one note by id.
- **Acceptance**: WHEN the user runs `notes delete <id>` for an existing id THEN that note is gone; unknown id → clear error, no change.

## Constraints

- Client: CLI · Storage: local file · Auth: none
- Success: all three commands work on a fresh install without network.
