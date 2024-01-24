# streamlit-sample

## DB設計

- users
  - id: int
    - ユーザーID
  - user_name: str
    - ユーザー名
    - 12文字上限
- rooms
  - id: int
    - 会議室ID
  - room_name: str
    - 会議室名
    - 12文字上限
  - capacity: int
    - 定員数
- bookings
  - id: int
    - 予約ID
  - user_id: int
    - ユーザーID(外部キー)
  - room_id: int
    - 会議室ID(外部キー)
  - reserved_num: int
    - 予約人数
    - rooms.capacityを上限とする
  - start_datetime: datetime
    - 開始時刻
    - 15分刻み
    - 09:00〜20:00
  - end_datetime: datetime
    - 終了時刻
    - 15分刻み
    - 09:00〜20:00

## 機能

- users(ユーザー)
  - 登録
  - 取得
- rooms(会議室)
  - 登録
  - 取得
- bookings(予約)
  - 登録
  - 一覧の取得
