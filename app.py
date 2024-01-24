import streamlit as st
import random
import requests
import json
import os
import datetime

# API_URL = "http://localhost:8000/"

api_url = os.environ.get("API_URL")
if api_url is None:
    api_url = "http://localhost:8000/"
USERS_URL = api_url + "users"
ROOMS_URL = api_url + "rooms"
BOOKINGS_URL = api_url + "bookings"

page = st.sidebar.selectbox("メニュー", ["ユーザー", "会議室", "予約"])


def display_users():
    st.title("ユーザー")

    with st.form(key="user_form"):
        user_id: int = random.randint(1, 100)
        user_name: str = st.text_input("ユーザー名", max_chars=12)
        data = {
            "id": user_id,
            "user_name": user_name,
        }
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        st.write("### 送信データ")
        st.json(data)
        res = requests.post(USERS_URL, json.dumps(data))
        st.write("### 受信データ")
        st.write("status code:", res.status_code)
        st.json(res.json())


def display_rooms():
    st.title("会議室")

    with st.form(key="booing_form"):
        room_id: int = random.randint(1, 100)
        room_name: str = st.text_input("会議室名", max_chars=12)
        capacity: int = st.number_input("定員", min_value=1, max_value=6)

        data = {"id": room_id, "room_name": room_name, "capacity": capacity}
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        st.write("### 送信データ")
        st.json(data)
        res = requests.post(ROOMS_URL, json.dumps(data))
        st.write("### 受信データ")
        st.write("status code:", res.status_code)
        st.json(res.json())


def display_bookings():
    st.title("予約")

    with st.form(key="user_form"):
        booking_id: int = random.randint(1, 100)
        user_id: str = st.text_input("ユーザーID")
        room_id: str = st.text_input("会議室ID")
        reserved_num: int = st.number_input("予約人数", min_value=1, max_value=6)
        date: str = st.date_input("予約日", min_value=datetime.date.today())
        start_time: str = st.time_input("開始時間", value=datetime.time(9, 0), step=1800)
        end_time: str = st.time_input("終了時間", value=datetime.time(20, 0), step=1800)
        data = {
            "id": booking_id,
            "user_id": user_id,
            "room_id": room_id,
            "reserved_num": reserved_num,
            "start_datetime": datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute,
            ).isoformat(),
            "end_datetime": datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute,
            ).isoformat(),
        }
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        st.write("### 送信データ")
        st.json(data)
        res = requests.post(BOOKINGS_URL, json.dumps(data))
        st.write("### 受信データ")
        st.write("status code:", res.status_code)
        st.json(res.json())


if page == "ユーザー":
    display_users()
elif page == "会議室":
    display_rooms()
elif page == "予約":
    display_bookings()
