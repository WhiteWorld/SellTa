create event e_user
	on schedule every 3 minute
	do
	delete from users where completed = 0 and updated_at < (now() - interval 10 minute);