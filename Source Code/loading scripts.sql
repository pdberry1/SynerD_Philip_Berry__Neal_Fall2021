load local infile
INSERT INTO donor (first_name, middle_name, last_name, phone, 
	email, company, address, city, state, zip_code, country)
VALUES ('Tiger', 'Eldrick', 'Woods', '4432421111', 'twoods@gmail.com', 
	'TW Foundation', '123 Palms Street', 'Jupiter', 'FL', '13324', 'USA');

INSERT INTO company (company, address, city, state, zip_code, country)
VALUES ('TW Foundation', '123 Palms Street', 'Jupiter', 'FL', '13324', 'USA');

INSERT INTO donation (donation_date, donation_amount)
VALUES ('01/22/2021', '34001');

