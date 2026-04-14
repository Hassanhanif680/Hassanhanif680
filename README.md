# 🤖 AI Marketing Automation

> **Automate your digital marketing workflows with AI.** Generate social media captions, hashtags, and ad copies in seconds — from the command line.

Built for **freelancers** and **marketing agencies** who want to save time and boost productivity.

---

## ✨ Features

| Feature | Offline | API (OpenAI) |
|---|---|---|
| Social media captions | ✅ | ✅ |
| Hashtag generation | ✅ | ✅ |
| Advertising copy | ✅ | ✅ |

- **Offline mode** — works without an API key using built-in templates
- **API mode** — leverages OpenAI for unique, high-quality AI-generated content
- **Simple CLI** — run tasks directly from the terminal
- **Output saving** — persist generated content to the `outputs/` directory

---

## 📁 Project Structure

```
.
├── cli.py                     # Command-line interface
├── scripts/
│   ├── api_client.py          # OpenAI API integration
│   ├── caption_generator.py   # Social media caption generation
│   ├── hashtag_generator.py   # Hashtag generation
│   └── ad_copy_generator.py   # Ad copy generation
├── data/
│   └── templates/
│       ├── captions.json      # Caption templates
│       ├── hashtags.json      # Hashtag collections by category
│       └── ad_copies.json     # Ad copy templates
├── outputs/                   # Generated content (auto-created)
├── tests/                     # Unit tests
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variable template
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- (Optional) An [OpenAI API key](https://platform.openai.com/api-keys) for AI-powered generation

### Installation

```bash
# Clone the repository
git clone https://github.com/Hassanhanif680/Hassanhanif680.git
cd Hassanhanif680

# Install dependencies
pip install -r requirements.txt
```

### Set Up API Key (optional)

Copy the example environment file and add your OpenAI API key:

```bash
cp .env.example .env
# Edit .env and replace "your-api-key-here" with your actual key
```

> **Note:** The `--offline` flag lets you use the tool without an API key.

---

## 💻 Usage

### Generate a Social Media Caption

```bash
# Offline (uses built-in templates)
python cli.py caption "AI tools for freelancers" --offline --tone casual

# With OpenAI API
python cli.py caption "AI tools for freelancers" --tone professional
```

### Generate Hashtags

```bash
# Offline
python cli.py hashtags "digital marketing" --offline --count 10

# With OpenAI API
python cli.py hashtags "digital marketing" --platform twitter --count 15
```

### Generate Ad Copy

```bash
# Offline
python cli.py adcopy "Marketing Dashboard" --offline --style playful --audience "small business owners"

# With OpenAI API
python cli.py adcopy "Marketing Dashboard" --platform facebook --style persuasive --audience "small business owners"
```

### Save Output to File

Add the `--save` flag to any command to persist the result in the `outputs/` directory:

```bash
python cli.py caption "product launch" --offline --save
```

---

## 📋 CLI Reference

```
python cli.py {caption,hashtags,adcopy} [options]
```

| Command | Required Arg | Key Options |
|---|---|---|
| `caption` | `topic` | `--tone`, `--platform`, `--offline`, `--save` |
| `hashtags` | `topic` | `--count`, `--platform`, `--offline`, `--save` |
| `adcopy` | `product` | `--style`, `--audience`, `--platform`, `--offline`, `--save` |

Run `python cli.py <command> --help` for full details on each sub-command.

---

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

---

## 💡 Example Use Cases

### Freelance Social Media Manager
Generate a week's worth of Instagram captions and hashtags in minutes:
```bash
python cli.py caption "Monday motivation" --offline --tone inspirational --save
python cli.py hashtags "fitness" --offline --count 15 --save
```

### Marketing Agency — Client Ad Campaigns
Quickly draft ad copy variations for A/B testing:
```bash
python cli.py adcopy "Organic Skincare Line" --style persuasive --audience "women 25-40" --save
python cli.py adcopy "Organic Skincare Line" --style playful --audience "women 25-40" --save
```

### Content Creator — Batch Hashtag Research
Find trending hashtags across multiple niches:
```bash
python cli.py hashtags "technology" --offline --count 10
python cli.py hashtags "design" --offline --count 10
python cli.py hashtags "business" --offline --count 10
```

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).
