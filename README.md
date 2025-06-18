# API_project_fake_store
В этом репозитории находится фраймеворк на Python + Pytest + Request
1. Для запуска теста в репозитории нажать Action 
2. На странице Action на левой стороне страницы нажать Python autotests
3. В правой стороне появится Run workflow нажать, далее нажать зелёную Run workflow
4. Если 3 пункт Run workflow не отображается значит у вас нет прав на запуск
5. Чтоб иметь право запуска нужно стать соавтором "Collaborators" репозитория
6. Отправте на skachat30913@gmail.com ваше имя в github. У вас появится право запуска продолжайте 3. пункт
7. Для связи
8. https://t.me/Vladimir_30913
9. skachat30913@gmail.com

10. Чек-лист API проверок




Get token
authorization token
check token not empty
check authorization token is valid
check status code is correct  




Refresh token
authorization token
check token not empty
check status code is correct




Get one element
check id is correct
check first name is correct
check last name is correct
check total price is correct
check deposit paid is correct
check booking dates is correct
check additional needs is correct
check url is correct
check response is list
check status code is correct




Get all element
get all element
check response is list
check url not empty
check id not empty
check firstname not empty
check lastname not empty
check total price not empty
check booking dates is correct
check additional needs is correct
check status code is correct




Post new element
create new element
check first name is correct
check last name is correct
check total price is correct
check deposit paid is correct
check booking dates is correct
check additional needs is correct
check status code is correct






Put update element
make changes in element
check first name is correct
check last name is correct
check total price is correct
check deposit paid is correct
check booking dates is correct
check additional needs is correct
check status code is correct


Patch update element
update test
check first name is correct
check last name is correct
check total price is correct
check deposit paid is correct
check booking dates is correct
check additional needs is correct
check status code is correct




Update element unauthorized
make changes in element
check status code 403 is unauthorized




Update element with negative data
make changes in element
check status code 400 is bad request




Post add element with negative data
new element
check status code 400 is bad request




Delete element
delete element
check status code 201 200 204

   
   

