package-build: build publish

brain-games: ; poetry run brain-games # запуск проекта

install: ; poetry install # установка новых зависимостей

build: ; poetry build # сборка билда

publish: ; poetry publish --dry-run # заливка библиотеки

package-install: ; python3 -m pip install --user dist/*.whl
