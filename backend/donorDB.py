class donor:
    def __init__(self, username='', Password='', first_name='', middle_name='', last_name='', Phone='', Email='', Street='', City='', State='', ZipCode='' ):
        self.username = username
        self.Password = password
		self.first_name = firstName
		self.middle_name = middleName
		self.last_name = lastName
		self.Phone = phone
		self.Email = email
		self.Street = street
		self.City = city
		self.State = state
		self.ZipCode = ZipCode

   def getUsername(self):
       return self.username

   def setUsername(self, username):
       self.username = username
  
   def getPassword(self):
       return self.password

   def setPassword(self, password):
       self.password = password
  
   def getFirstName(self):
       return self.firstName
      
   def setFirstName(self, firstName):
       self.firstName = firstName
  
   def getMiddleName(self):
       return self.middleName

   def setMiddleName(self, middleName):
       self.middleName = middleName
  
   def getLastName(self):
       return self.lastName
      
   def setLastName(self, lastName):
       self.lastName = lastName

   def getPhone(self):
       return self.phone

   def setPhone(self, phone):
       self.phone = phone
  
   def getEmail(self):
       return self.email
      
   def setEmail(self, email):
       self.email = email
	   
   def getStreet(self):
       return self.street

   def setStreet(self, street):
       self.street = street
	   
   def getCity(self):
       return self.city

   def setCity(self, city):
       self.city = city
	   
   def getState(self):
       return self.state

   def setState(self, state):
       self.state = state
	   
   def getZipCode(self):
       return self.zipCode

   def setZipCode(self, zipCode):
       self.zipCode = zipCode
	   
class company:
    def __init__(self, company= '', Street='', City='', State='', ZipCode='' ):
       	self.Company = company
		self.Street = street
		self.City = city
		self.State = state
		self.ZipCode = ZipCode

   def getUsername(self):
       return self.username
	   
   def getCompany(self):
       return self.company
      
   def setCompany(self, company):
       self.company = company
	   
   def getStreet(self):
       return self.street

   def setStreet(self, street):
       self.street = street
	   
   def getCity(self):
       return self.city

   def setCity(self, city):
       self.city = city
	   
   def getState(self):
       return self.state

   def setState(self, state):
       self.state = state
	   
   def getZipCode(self):
       return self.zipCode

   def setZipCode(self, zipCode):
       self.zipCode = zipCode
	   
class donation:
    def __init__(self, donationDate= '', donationAmount=''):
		self.donationDate = donationDate
		self.donationAmount = donationAmount
	
	  def getDonationDate(self):
       return self.donationDate

   def setDonationDate(self, donationDate):
       self.state = donationDate
	   
   def getDonationAmount(self):
       return self.donationAmount

   def setDonationAmount(self, donationAmount):
       self.donationAmount = donationAmount