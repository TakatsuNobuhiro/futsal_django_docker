# futsal_game_django

##　環境構築

```
docker-compose build
```

## サーバー起動
```
docker-compose up
```

## サーバーをダウン
```
docker-compose down
```
or

control + c

## ER図追加
```
docker compose run --rm web python futsal_django/manage.py graph_models match -o er.png
```
