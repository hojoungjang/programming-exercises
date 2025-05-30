"""
프로그래머스
호텔 대실
https://school.programmers.co.kr/learn/courses/30/lessons/155651
"""

from heapq import heapify, heappush, heappop

def time_to_minutes(time_str):
    hours, minutes = time_str.split(":")
    return int(hours) * 60 + int(minutes)

def solution(book_time):
    times = [tuple(map(time_to_minutes, slot)) for slot in book_time]
    times.sort()
    max_rooms = 0
    room_end_time = []
    for start, end in times:
        while room_end_time and room_end_time[0] + 10 <= start:
            heappop(room_end_time)
        heappush(room_end_time, end)
        max_rooms = max(max_rooms, len(room_end_time))
    return max_rooms
    