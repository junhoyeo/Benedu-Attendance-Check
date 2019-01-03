# 베네듀 자동 출석체크 ![pylint](./pylint.svg)
베네듀에 자동으로 로그인해 준다.

1. `secret.json` 생성, 계정 정보(학생) 저장

```json
{
    "email": "email@example.com",
    "password": "password"
}
```

2. `pip3 install selenium`

3. 실행

```bash
$ python3 app.py
{"success": true, "points": 3, "rank": 4}
```

- `success`: 성공 여부
- `points`: 출석체크 이후 사용자 포인트
- `rank`: 출석체크 이후 사용자 등수

4. crontab

```bash
$ crontab -l
0 0 * * * python3 Desktop/Benedu-Attendance-Check/app.py
```

매일 0시 0분마다 자동 실행
