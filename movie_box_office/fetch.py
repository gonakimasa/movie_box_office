from datetime import datetime
import requests
import logging

def fetch_movie_data():
    """
    映画データを外部APIから取得してログに出力する。
    （あとで加工や保存処理を追加予定）
    """
    today = datetime.today().strftime('%Y-%m-%d')
    url = "https://api.example.com/movies" #仮記載
    params = {
        "date" : today,
        "api_key": "your_api_key" #のちに変更
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        logging.info(f"取得データ: {data}")
    except Exception as e:
        logging.error(f"データ取得エラー: {e}")
        raise
