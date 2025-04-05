-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) as count FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE 
HAVING ANIMAL_TYPE = 'Cat' Or ANIMAL_TYPE = 'Dog' order by animal_type