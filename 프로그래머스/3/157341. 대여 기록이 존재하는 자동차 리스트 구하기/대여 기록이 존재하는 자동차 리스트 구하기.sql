-- 코드를 입력하세요
SELECT DISTINCT(C.CAR_ID) AS CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS C, CAR_RENTAL_COMPANY_RENTAL_HISTORY AS RH
WHERE C.CAR_ID = RH.CAR_ID
AND CAR_TYPE = '세단' AND START_DATE >= '2022-10-01'
ORDER BY CAR_ID DESC;


