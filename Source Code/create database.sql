CREATE DATABASE foundation;

USE foundation;

CREATE TABLE donor (
	donor_id int NOT NULL AUTO_INCREMENT,
	first_name varchar(50),
	middle_name varchar(50),
	last_name varchar(50),
	phone int,
	email varchar(50),
	company varchar(50),
	company_id int NOT NULL,
	address varchar(50),
	city varchar(50),
	state varchar(50),
	zip_code int
);

USE foundation;

CREATE TABLE company (
	company_id int NOT NULL AUTO_INCREMENT,
	company varchar(50),
	address varchar(50),
	city varchar(50),
	state varchar(50),
	zip_code int
);

FROM donor;
JOIN company;
ON donor.company_id = company.company_id;

USE foundation;

CREATE TABLE donation (
	donor_id int NOT NULL,
	company_id int NOT NULL,
	donation_date date,
	donation amount decimal(9,2)
);
FROM donor;
JOIN donation;
ON donor.donor_id = donation.donor_id;

FROM company;
JOIN donation;
ON company.company_id = donation_company_id;