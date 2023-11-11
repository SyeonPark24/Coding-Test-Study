-- 코드를 입력하세요
SELECT SUB_H.FLAVOR
FROM (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL
    FROM FIRST_HALF 
    GROUP BY FLAVOR) SUB_H,
    (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL
    FROM JULY
    GROUP BY FLAVOR) SUB_J
WHERE SUB_H.FLAVOR = SUB_J.FLAVOR
ORDER BY (SUB_H.TOTAL+SUB_J.TOTAL) DESC
LIMIT 3;


