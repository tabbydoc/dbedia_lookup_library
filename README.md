# DBpedia Lookup Library

Небольшой скрипт для работы с DBpedia Lookup Service.

## Использование

При импорте библиотеки порт задаётся по умолчанию 9274. 
Для изменения необходимо вызвать функцию ```init(port=)```.

Функция ```get_entities()``` возвращает список сущностей. 
Остальные параметры совпадают с параметрами запроса к [DBpedia Lookup Library](https://github.com/dbpedia/dbpedia-lookup/blob/master/README.md#static-query-parameters).
