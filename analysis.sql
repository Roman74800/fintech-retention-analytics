-- PostgreSQL: cohort retention by signup month and age in months
WITH cohorts AS (
 SELECT user_id, DATE_TRUNC('month', signup_month)::date AS cohort_month FROM users
), activity AS (
 SELECT DISTINCT user_id, DATE_TRUNC('month', activity_month)::date AS activity_month FROM monthly_activity
), cohort_sizes AS (
 SELECT cohort_month, COUNT(*) AS cohort_size FROM cohorts GROUP BY 1
), active AS (
 SELECT c.cohort_month,
        (EXTRACT(YEAR FROM a.activity_month) - EXTRACT(YEAR FROM c.cohort_month))*12
        + EXTRACT(MONTH FROM a.activity_month) - EXTRACT(MONTH FROM c.cohort_month) AS age_months,
        COUNT(DISTINCT c.user_id) AS active_users
 FROM cohorts c JOIN activity a USING (user_id)
 WHERE a.activity_month >= c.cohort_month GROUP BY 1,2
)
SELECT a.cohort_month, a.age_months, a.active_users, s.cohort_size,
       ROUND(a.active_users::numeric / NULLIF(s.cohort_size,0),4) AS retention
FROM active a JOIN cohort_sizes s USING (cohort_month)
ORDER BY 1,2;
