# 会議室予約システムフロント

## 機能

- users(ユーザー)
  - 一覧
  - 登録フォーム
    - ユーザー名  
  - 詳細
- rooms(会議室)
  - 一覧
  - 登録フォーム
    - 会議室名
    - 定員数 
  - 詳細
- bookings(予約)
  - 一覧  
  - 登録フォーム
    - ユーザーID
    - 会議室ID
    - 予約人数
      - rooms.capacityを上限とする
    - 予約日
    - 開始時間
    - 終了時間
  - 詳細

## 参考

- [Documentation | 公式サイト](https://docs.streamlit.io/library/api-reference)
