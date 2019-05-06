use paijiu_data if exists paijiu_data
#drop table mana_user;
CREATE TABLE mana_user(
	id INT PRIMARY KEY AUTO_INCREMENT,\
	username VARCHAR(32),\
	password VARCHAR(32),\
	level INT\
);
INSERT INTO mana_user (username,password,level) VALUES ('admin','admin',0);
