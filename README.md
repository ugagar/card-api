# card-api
Простой проект для изучения FastAPI.

# Задачи
- [ ] Написать модель карт (Pydantic)
- [ ] Добавить endpoints:
	GET
	- [ ] Получение всей колоды (`get "/cards/all"`)
	- [ ] Получение карт по значению (`get "/cards/card?value=<value>&suit=<suit>"`)
	- [ ] Получение карт по масти (`get "/cards/{suit}"`)
	- [ ] Получение карт по значению (`get "/cards/{value}"`)
	- [ ] Получение случайной карты (`get "cards/random"`)
	POST
	- [ ] Добавить карту в колоду (`post "/cards/card?value=<value>&suit=<suit>"`)
	DELETE
	- [ ] Удалить карту из колоды (`delete "/cards/card?value=<value>&suit=<suit>"`)
- [ ] Использование бд
	- [ ] Сохранять собранные колоды в базу данных (PostgreSQL, SQLAlchemy) (`put /save/` пока не представляю как)
- [ ] Бизнес логика
	- [ ] Перемешивание колоды
	- [ ] Выдача случайной колоды
