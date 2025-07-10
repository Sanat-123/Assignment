-- Use the correct database
USE clique_bait;

-- 1. Total number of users
SELECT COUNT(DISTINCT user_id) AS total_users
FROM users;

-- 2. Average number of cookies per user
SELECT ROUND(COUNT(DISTINCT cookie_id) * 1.0 / COUNT(DISTINCT user_id), 2) AS avg_cookies_per_user
FROM users;

-- 3. Unique number of visits by all users per month
SELECT
  DATE_FORMAT(event_time, '%Y-%m') AS month,
  COUNT(DISTINCT visit_id) AS unique_visits
FROM events
GROUP BY DATE_FORMAT(event_time, '%Y-%m')
ORDER BY month;

-- 4. Number of events for each event type
SELECT
  ei.event_name,
  COUNT(*) AS total_events
FROM events e
JOIN event_identifier ei ON e.event_type = ei.event_type
GROUP BY ei.event_name
ORDER BY total_events DESC;

-- 5. Percentage of visits with a purchase event (event_type = 3)
SELECT
  ROUND(
    COUNT(DISTINCT CASE WHEN event_type = 3 THEN visit_id END) * 100.0 /
    COUNT(DISTINCT visit_id), 2
  ) AS purchase_visit_percentage
FROM events;

-- 6. Percentage of visits viewing checkout page (page_id = 12) but no purchase
SELECT
  ROUND(
    COUNT(*) * 100.0 /
    (SELECT COUNT(DISTINCT visit_id) FROM events),
    2
  ) AS checkout_without_purchase
FROM (
  SELECT visit_id
  FROM events
  WHERE page_id = 12
  GROUP BY visit_id
  HAVING SUM(CASE WHEN event_type = 3 THEN 1 ELSE 0 END) = 0
) AS filtered;

-- 7. Top 3 pages by number of views (event_type = 1)
SELECT
  ph.page_name,
  COUNT(*) AS views
FROM events e
JOIN page_hierarchy ph ON e.page_id = ph.page_id
WHERE e.event_type = 1
GROUP BY ph.page_name
ORDER BY views DESC
LIMIT 3;

-- 8. Number of views and cart adds for each product category
SELECT
  ph.product_category,
  COUNT(CASE WHEN e.event_type = 1 THEN 1 END) AS views,
  COUNT(CASE WHEN e.event_type = 2 THEN 1 END) AS cart_adds
FROM events e
JOIN page_hierarchy ph ON e.page_id = ph.page_id
GROUP BY ph.product_category;

-- 9. Top 3 products by purchases (event_type = 3)
SELECT
  ph.product_id,
  COUNT(*) AS purchases
FROM events e
JOIN page_hierarchy ph ON e.page_id = ph.page_id
WHERE e.event_type = 3
GROUP BY ph.product_id
ORDER BY purchases DESC
LIMIT 3;
