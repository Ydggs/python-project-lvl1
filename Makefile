package-build: build publish

brain-games: ; poetry run brain-games # запуск проекта

brain-even: ; poetry run brain-even # запуск игры "Четность"

brain-calc: ; poetry run brain-calc # запуск игры "Калькулятор"

brain-gcd: ; poetry run brain-gcd # запуск игры "Наибольший общий делитель"

brain-progression: ; poetry run  brain-progression # запуск игры "Арефмитическая прогрессия"

brain-prime: ; poetry run brain-prime # запуск игры "Простое число"

install: ; poetry install # установка новых зависимостей

build: ; poetry build # сборка билда

publish: ; poetry publish --dry-run # заливка библиотеки

package-install: ; python3 -m pip install --user dist/*.whl

lint: ; poetry run flake8 brain_games # проверка качества кода
