# OpenClaw to Manus Skills Conversion

All 53 OpenClaw skills converted into Manus-compatible format. Each skill follows the Manus SKILL.md specification with proper YAML frontmatter (`name` + `description`) and concise markdown instructions optimized for the Manus sandbox environment (Ubuntu 22.04, shell, browser, Python 3.11, Node.js 22).

## Quick Start

Copy any skill directory into `/home/ubuntu/skills/` on your Manus instance:

```bash
cp -r oc-weather /home/ubuntu/skills/
```

## Skills Index (53 Total)

### Productivity & Notes
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-local-notes` | Manage local markdown notes | apple-notes |
| `oc-note-taking` | Create and manage notes via CLI | bear-notes |
| `oc-notion` | Manage Notion workspaces via API | notion |
| `oc-obsidian` | Manage Obsidian vaults on disk | obsidian |
| `oc-google-tasks-and-reminders` | Manage tasks and reminders | apple-reminders |
| `oc-things-3-unsupported` | Things 3 reference (macOS-only) | things-mac |
| `oc-trello` | Manage Trello boards via REST API | trello |

### Communication & Messaging
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-discord` | Discord API integration | discord |
| `oc-slack` | Slack API integration | slack |
| `oc-bluebubbles` | iMessage via BlueBubbles | bluebubbles |
| `oc-imessage` | iMessage integration reference | imsg |
| `oc-wacli` | WhatsApp messaging via CLI | wacli |
| `oc-voice-call` | Voice calls via Twilio/Telnyx/Plivo | voice-call |

### Development & Code
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-coding-agent` | Delegate coding tasks to AI agents | coding-agent |
| `oc-github` | GitHub CLI operations | github |
| `oc-github-issues` | Auto-fix GitHub issues with agents | gh-issues |
| `oc-skill-creator` | Create new Manus skills | skill-creator |
| `oc-interactive-shell-sessions` | Manage interactive shell sessions | tmux |

### Media & Content
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-openai-image-gen` | Generate images via OpenAI API | openai-image-gen |
| `oc-openai-whisper-api` | Transcribe audio via Whisper API | openai-whisper-api |
| `oc-openai-whisper` | Local Whisper transcription | openai-whisper |
| `oc-video-frames` | Extract frames from video via ffmpeg | video-frames |
| `oc-songsee` | Audio spectrograms and visualizations | songsee |
| `oc-gifgrep` | Search and download GIFs | gifgrep |
| `oc-nano-banana-pro` | Generate presentation slides | nano-banana-pro |
| `oc-nano-pdf` | Generate PDF documents | nano-pdf |
| `oc-canvas` | Display HTML content on nodes | canvas |

### AI & LLM Tools
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-gemini` | Google Gemini CLI for Q&A | gemini |
| `oc-oracle` | Multi-model AI consultation | oracle |
| `oc-sag` | Sub-agent orchestration | sag |
| `oc-model-usage-analysis` | Analyze LLM token usage | model-usage |
| `oc-summarize` | Summarize URLs and content | summarize |

### Smart Home & IoT
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-openhue` | Philips Hue light control | openhue |
| `oc-sonos-cli` | Sonos speaker control | sonoscli |
| `oc-blucli` | BluOS/NAD player control | blucli |
| `oc-eightctl` | Eight Sleep mattress control | eightctl |
| `oc-camsnap` | RTSP/ONVIF camera snapshots | camsnap |

### Utilities & Services
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-weather` | Weather forecasts via wttr.in | weather |
| `oc-1password` | 1Password CLI integration | 1password |
| `oc-blogwatcher` | RSS/Atom feed monitoring | blogwatcher |
| `oc-food-order` | Foodora order management | food-order |
| `oc-ordercli` | Order CLI operations | ordercli |
| `oc-goplaces` | Location/places search | goplaces |
| `oc-himalaya` | Email management via CLI | himalaya |
| `oc-spotify-player` | Spotify playback control | spotify-player |
| `oc-sherpa-onnx-tts` | Text-to-speech synthesis | sherpa-onnx-tts |
| `oc-xurl` | X (Twitter) API integration | xurl |

### Google Workspace
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-google-workspace` | Gmail and Calendar via MCP | gog |

### System & Meta
| Skill | Description | Source |
|-------|-------------|--------|
| `oc-healthcheck` | System health monitoring | healthcheck |
| `oc-session-logs` | Session log management | session-logs |
| `oc-skill-management` | Skill discovery and management | clawhub |
| `oc-mcporter` | MCP server management | mcporter |
| `oc-linux-gui-automation` | Linux GUI automation via xdotool | peekaboo |

## Conversion Methodology

Each OpenClaw skill was converted following these principles:

1. **Frontmatter**: Stripped to Manus-compatible `name` + `description` only
2. **Environment**: Adapted from macOS/local-first to Ubuntu 22.04 sandbox
3. **Tools**: Replaced OpenClaw-specific tools with Manus equivalents
4. **Conciseness**: All skills under 500 lines
5. **Validation**: All 53 skills pass `quick_validate.py` with zero errors

## License

Original OpenClaw skills are MIT licensed. Converted skills maintain the same license.
