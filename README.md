Environment:
  VM1:(for web)
    Python2.7
    Apache2

  VM2: MySQL >= 5.7

Preprocess
  1. Set DB login profile and web host ip in default.config file 
  2. Install Python packages in web VM.
     #pip install Flask
     #pip install flask-mysql
     #pip install multiprocessing
  3. Create and insert data in MySqL VM.
	a. create database demo ;

	b. use demo;

	c. CREATE TABLE video (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	name VARCHAR(320),
	url VARCHAR(330));

	d.
	INSERT INTO `video` (`name`,`url`) VALUES ('The 7 Steps of Machine Learning','https://www.youtube.com/embed/nKW8Ndu7Mjw');
	INSERT INTO `video` (`name`,`url`) VALUES ('What is Artificial Intelligence (or Machine Learning)?','https://www.youtube.com/embed/mJeNghZXtMo');
	INSERT INTO `video` (`name`,`url`) VALUES ('Machine Learning with Python','https://www.youtube.com/embed/OGxgnH8y2NM');
	INSERT INTO `video` (`name`,`url`) VALUES ('A Friendly Introduction to Machine Learning','https://www.youtube.com/embed/IpGxLWOIZy4');
	INSERT INTO `video` (`name`,`url`) VALUES ('Learn Machine Learning in 3 Months (with curriculum)','https://www.youtube.com/embed/Cr6VqTRO1v0');
