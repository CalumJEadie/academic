-- MySQL implementation of division from tuple relational calculus / relational algebra.
--
-- http://www.cl.cam.ac.uk/teaching/1112/Databases/
-- Slide 71
--
-- Calum J. Eadie

create database if not exists test;
use test;

-- R = Students
-- S = Awards
-- T = Student ( Same structure, different data )

drop table if exists R;
create table R (
    name CHAR,
    award CHAR
);

drop table if exists S;
create table S (
    award CHAR
);

drop table if exists T;
create table T (
    name CHAR,
    award CHAR
);

insert into R
values
("F","w"),
("F","m"),
("E","m"),
("E","w"),
("E","d"),
("J","d");

insert into S
values
("m"),
("w"),
("d");

insert into T
values
("E","m"),
("E","w"),
("E","d"),
("J","d"),
("J","w");

select * from R;
select * from S;
select * from T;

-- Union

select "R union T";

select * from R union select * from T;

-- Set intersection and difference in MySQL

-- Intersection of R(a,b) and S(a,b)
--
-- select * from R intersect select * from S
-- 
-- select distinct *
-- from R
-- where exists ( select * from S where R.a = S.a and R.b = S.b )

select "R intersection T";

select distinct *
from R
where exists ( select * from T where R.name = T.name and R.award = T.award );

-- Difference of R(a,b) and S(a,b)
--
-- select * from R minus select * from S
--
-- select distinct *
-- from R
-- where not exists ( select * from S where R.a = S.a and R.b = S.b )

select "R minus T";

select distinct *
from R
where not exists ( select * from T where R.name = T.name and R.award = T.award );

-- Division of R(a,b) and S(b)

select "All possible combinations of name and award";

select distinct R.name,S.award from R join S;

select "Counter examples. All possible combinations - actual combinations";

select distinct R.name, S.award
from R
join S
where not exists (
    select R1.name,R1.award
    from R as R1
    where R.name = R1.name
    and S.award = R1.award
);

select "Names which are counter examples";

select distinct R.name
from R
join S
where not exists (
    select R1.name,R1.award
    from R as R1
    where R.name = R1.name
    and S.award = R1.award
);

select "R div S";

-- R div S.
select distinct R.name
from R
where not exists (
    -- Counter examples.
    -- Counter examples = All combinations = All combinatios - actual combinations.
    select distinct R1.name
    from R as R1
    join S
    where not exists (
        -- Actual combinations.
        select R2.name,R2.award
        from R as R2
        where R.name = R2.name
        and S.award = R2.award
    )
    and R.name = R1.name
)
