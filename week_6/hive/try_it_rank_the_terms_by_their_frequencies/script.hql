CREATE TABLE abcnews (
    NewsDate STRING,
    Headline STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'abcnews.txt' OVERWRITE INTO TABLE abcnews;

CREATE VIEW year_terms AS SELECT substr(NewsDate, 0, 4) as year, term FROM abcnews LATERAL VIEW EXPLODE
(SPLIT(Headline, ' ')) terms AS term;

SELECT year,term,count(*) AS num FROM year_terms GROUP BY year,term;

CREATE VIEW termcount AS SELECT year,term,count(*) AS num FROM year_terms GROUP BY year,term;

SELECT a.year, a.term FROM (select *, rank() over (ORDER BY year, num DESC, term) FROM termcount) as a;