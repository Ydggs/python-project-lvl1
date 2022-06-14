package-build: build publish

brain-games: ; poetry run brain-games # запуск проекта

brain-even: ; poetry run brain-even # запуск игры

install: ; poetry install # установка новых зависимостей

build: ; poetry build # сборка билда

publish: ; poetry publish --dry-run # заливка библиотеки

package-install: ; python3 -m pip install --user dist/*.whl

lint: ; poetry run flake8 brain_games # проверка качества кода