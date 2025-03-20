name: Automate Weather Data Updates

on:
  schedule:
    - cron: '*/30 * * * *'  # Runs every 30 minutes
  workflow_dispatch:  # Allows manual triggering

jobs:
  update_domo:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install requests python-dotenv

      # 🔍 Debug Step - List All Files
      - name: Debug - List files
        run: ls -R

      - name: Run weather update script
        run: python ./send_to_domo.py  # Ensure correct file path
        env:
          OPENWEATHER_API_KEY: ${{ secrets.OPENWEATHER_API_KEY }}
          DOMO_WEBHOOK_URL: ${{ secrets.DOMO_WEBHOOK_URL }}
