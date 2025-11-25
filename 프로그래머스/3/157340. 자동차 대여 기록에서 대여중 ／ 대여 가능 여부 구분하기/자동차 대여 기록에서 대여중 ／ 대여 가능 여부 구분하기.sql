-- 코드를 입력하세요
SELECT CAR_ID, 
    CASE
        -- 10월 16일이 대여 기간에 포함되는 기록이 하나라도 있으면(MAX = 1) '대여중'
        WHEN MAX('2022-10-16' BETWEEN START_DATE AND END_DATE) = 1 THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY CAR_ID
ORDER BY CAR_ID DESC

-- FLOW 예시) 그룹화하여 CAR_ID = 1인 튜플들을 SELECT에서 검사
