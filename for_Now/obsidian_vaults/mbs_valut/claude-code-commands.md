# Claude Code Slash Commands Reference

A comprehensive guide to all slash commands widely used in Claude Code.

## Session Management
- **`/clear [name]`** - Start a new conversation with empty context. Aliases: `/reset`, `/new`
- **`/rename [name]`** - Rename the current session
- **`/resume [session]`** - Resume a previous conversation by ID or name
- **`/branch [name]`** - Create a branch of the current conversation. Alias: `/fork`
- **`/exit`** - Exit the CLI. Alias: `/quit`

## Model & Performance
- **`/model [model]`** - Set the AI model for the current session
- **`/effort [level|auto]`** - Set model effort level: `low`, `medium`, `high`, `xhigh`, `max`
- **`/fast [on|off]`** - Toggle fast mode
- **`/compact [instructions]`** - Free up context by summarizing conversation

## Code Review & Analysis
- **`/code-review [level] [--comment] [target]`** - Review diff for correctness bugs
- **`/review [PR]`** - Review a pull request locally
- **`/security-review`** - Analyze pending changes for security vulnerabilities
- **`/diff`** - Open interactive diff viewer
- **`/ultrareview [PR]`** - Deep multi-agent code review in cloud sandbox

## Context & Memory
- **`/memory`** - Edit memory files and manage auto-memory
- **`/init`** - Initialize project with a CLAUDE.md guide
- **`/context [all]`** - Visualize current context usage
- **`/rewind`** - Rewind conversation/code to previous point. Aliases: `/checkpoint`, `/undo`
- **`/recap`** - Generate one-line summary of session

## Planning & Workflow
- **`/plan [description]`** - Enter plan mode directly
- **`/batch <instruction>`** - Orchestrate large-scale changes in parallel
- **`/ultraplan <prompt>`** - Draft a plan in ultraplan session
- **`/goal [condition|clear]`** - Set a goal for Claude to work toward

## Parallel Work & Agents
- **`/agents`** - Manage agent configurations
- **`/background [prompt]`** - Detach session to run as background agent. Alias: `/bg`
- **`/tasks`** - List and manage background tasks. Also: `/bashes`
- **`/stop`** - Stop the current background session

## Development & Testing
- **`/run`** - Launch and drive your project's app
- **`/verify`** - Confirm code changes work by building and running
- **`/run-skill-generator`** - Teach `/run` and `/verify` how to build your project
- **`/loop [interval] [prompt]`** - Run a prompt repeatedly

## Remote & Web
- **`/remote-control`** - Make session available for remote control from claude.ai. Alias: `/rc`
- **`/teleport`** - Pull a web session into terminal. Alias: `/tp`
- **`/desktop`** - Continue session in Claude Code Desktop app. Alias: `/app`
- **`/autofix-pr [prompt]`** - Spawn web session that watches PR and pushes fixes
- **`/web-setup`** - Connect GitHub account to Claude Code on the web

## Configuration & Settings
- **`/config`** - Open Settings interface. Alias: `/settings`
- **`/permissions`** - Manage tool permissions. Alias: `/allowed-tools`
- **`/mcp`** - Manage MCP server connections and OAuth
- **`/hooks`** - View hook configurations
- **`/plugin`** - Manage Claude Code plugins
- **`/keybindings`** - Open keybindings configuration
- **`/theme`** - Change color theme (auto, light, dark, colorblind-accessible)
- **`/color [color|default]`** - Set prompt bar color
- **`/skills`** - List available skills with token count

## Utilities
- **`/usage`** - Show session cost and stats. Aliases: `/cost`, `/stats`
- **`/copy [N]`** - Copy last response to clipboard
- **`/export [filename]`** - Export conversation as plain text
- **`/btw <question>`** - Ask quick side question
- **`/help`** - Show help and available commands
- **`/status`** - Show version, model, account info

## Debugging & Troubleshooting
- **`/doctor`** - Diagnose and verify installation
- **`/debug [description]`** - Enable debug logging
- **`/heapdump`** - Write JavaScript heap snapshot
- **`/feedback [report]`** - Submit feedback or bug report. Aliases: `/bug`, `/share`

## Terminal & Display
- **`/tui [default|fullscreen]`** - Set terminal UI renderer
- **`/fullscreen`** - Toggle focus view
- **`/focus`** - Toggle focus view (fullscreen rendering only)
- **`/scroll-speed`** - Adjust mouse wheel scroll speed
- **`/statusline`** - Configure Claude Code's status line
- **`/terminal-setup`** - Configure terminal keybindings

## Automation & Scheduling
- **`/schedule [description]`** - Create/update/list routines. Alias: `/routines`
- **`/loop [interval] [prompt]`** - Run prompt repeatedly with optional interval

## Integration & Authentication
- **`/login`** - Sign in to Anthropic account
- **`/logout`** - Sign out from Anthropic account
- **`/ide`** - Manage IDE integrations
- **`/install-github-app`** - Set up Claude GitHub Actions app
- **`/install-slack-app`** - Install Claude Slack app
- **`/remote-env`** - Configure default remote environment

## Account & Community
- **`/voice [hold|tap|off]`** - Toggle voice dictation
- **`/chrome`** - Configure Claude in Chrome settings
- **`/mobile`** - Show QR code for mobile app. Aliases: `/ios`, `/android`
- **`/passes`** - Share free week of Claude Code
- **`/upgrade`** - Open upgrade page
- **`/usage-credits`** - Configure usage credits
- **`/stickers`** - Order Claude Code stickers
- **`/radio`** - Open Claude FM lo-fi radio

## Learning & Onboarding
- **`/powerup`** - Discover features through interactive lessons
- **`/insights`** - Generate report analyzing your sessions
- **`/team-onboarding`** - Generate team onboarding guide
- **`/claude-api [migrate|managed-agents-onboard]`** - Load Claude API reference
- **`/fewer-permission-prompts`** - Reduce permission prompts

## Cloud Providers
- **`/setup-bedrock`** - Configure Amazon Bedrock (requires `CLAUDE_CODE_USE_BEDROCK=1`)
- **`/setup-vertex`** - Configure Google Vertex AI (requires `CLAUDE_CODE_USE_VERTEX=1`)

## Miscellaneous
- **`/add-dir <path>`** - Add working directory for file access
- **`/reload-plugins`** - Reload active plugins
- **`/release-notes`** - View changelog
- **`/privacy-settings`** - View and update privacy settings (Pro/Max only)

## Tips
- Type `/` to autocomplete and filter commands
- Most commands work while Claude is responding
- Commands marked **[Skill]** are bundled prompts Claude can invoke automatically
- Create custom commands using skills
- Many commands have aliases (shortcuts)
- Type `/` followed by letters to filter available commands

---

**Last Updated:** 2026-05-22
**Source:** Claude Code Official Documentation
