# FlairTimerModMail

FlairTimerModMail is a Reddit bot designed to monitor new posts in a specified subreddit for a particular flair. When a post receives the target flair, the bot starts a timer. If the flair remains on the post for a configurable number of hours, the bot sends a modmail notification to the subreddit moderators. This tool is useful for subreddits that use flairs to track posts requiring moderator attention or follow-up.

## Features
- Monitors new posts in a subreddit for a specific flair
- Tracks how long a post has had the flair
- Sends a modmail notification after a configurable time period
- Configurable via environment variables or a config file
- Supports running natively with Python or in Docker (standalone or with Docker Compose)

## Requirements
- Python 3.8+
- Reddit API credentials (see below)

## Configuration
The bot can be configured using a `config/config.py` file or via environment variables. When running in Docker, environment variables are recommended and can be managed with a `.env` file.

### Required Configuration Values
- `USERNAME`: Reddit username
- `PASSWORD`: Reddit password
- `CLIENT_ID`: Reddit API client ID
- `CLIENT_SECRET`: Reddit API client secret
- `USER_AGENT`: User agent string for Reddit API
- `SUBREDDIT`: Subreddit to monitor
- `FLAIR_TEXT`: Flair text to track (case sensitive)
- `INTERVAL`: How often to scan (seconds)
- `HOURS`: How many hours before sending notification
- `MESSAGETITLE`: Title for the modmail message
- `SEARCHLIMIT`: How many posts to scan (max 1000)

## Installation & Usage

### 1. Python (Native)
1. Clone the repository:
   ```sh
   git clone https://github.com/slfhstd/FlairTimerModMail.git
   cd FlairTimerModMail
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Copy `example.env` to `.env` and fill in your Reddit credentials and settings, or edit `config/config.py` directly.
4. Run the bot:
   ```sh
   python flairtimermodmail.py
   ```

### 2. Docker Run
1. Copy `example.env` to `.env` and fill in your values.
2. Run the bot with Docker:
   ```sh
   docker run --env-file .env -v $(pwd)/config:/app/config ghcr.io/slfhstd/flairtimermodmail:latest
   ```

### 3. Docker Compose
1. Clone the repository:
   ```sh
   git clone https://github.com/slfhstd/FlairTimerModMail.git
   cd FlairTimerModMail
   ```
2. Copy `example.env` to `.env` and fill in your values.
3. Start the bot with Docker Compose:
   ```sh
   docker-compose up -d
   ```

## Notes
- The bot will auto-generate a config file from environment variables if one does not exist.
- Make sure your Reddit account has the necessary permissions and API credentials.
- For production use, keep your credentials secure and do not commit `.env` files with real secrets to version control.

## License
This project is provided as-is under the MIT License.
