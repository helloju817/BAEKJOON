SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE,"%Y-%m-%d" ) as PUBLISHED_DATE
FROM BOOK AS B JOIN AUTHOR AS A ON B.AUTHOR_ID=A.AUTHOR_ID
WHERE B.CATEGORY="경제"
GROUP BY BOOK_ID
ORDER BY B.PUBLISHED_DATE;