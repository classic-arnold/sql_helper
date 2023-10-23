SELECT *, char_length(title) as char_len
FROM films
GROUP BY id
HAVING char_len >= 15;