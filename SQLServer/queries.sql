declare @name varchar(50) = 'Ke%'
select top 100
    firstname, middlename, lastname
from Person.Person
where firstname like @name;
select top 1
    *
from Person.Person