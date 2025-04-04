select round(sum(DAILY_FEE)/count(DAILY_FEE)) from CAR_RENTAL_COMPANY_CAR 
where car_type='SUV'