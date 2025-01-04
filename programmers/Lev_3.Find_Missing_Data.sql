# 1. ANIMAL_INS와 ANIMAL_OUTS에 ANIMAL_ID 컬럼 기준으로 right outer join를 적용
# 2. ANIMAL_INS.DATETIME 정보가 없는 row들만 찾기
# 3. ANIMAL_ID와 NAME만 출력하기

SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS as A right outer join ANIMAL_OUTS as B on A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME IS NULL