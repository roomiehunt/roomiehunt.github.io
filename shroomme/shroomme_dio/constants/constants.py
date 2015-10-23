#---------------CONSTANTS OF THE PROJECT IS STORED HERE------------------------------------------------------#
#---------------ALL APP NAMES START WITH LOWER LETTER-------------#
#---------------ALL MODEL NAMES START WITH CAPITALS---------------#

class constants():
	GENDER_CHOICES = (
		('M','Male'),
		('F','Female'),
		#('U','Unspecified'),
	)
	FRIEND_STATUS = (
		('F','Friends'),
		('P','Pending'),
		('B','Blocked'),
		('N','NotFriends')
	)
	ROOMATE_STATUS = (
		('Looking for roomates','Looking for roomates'),
		('Looking for place and roomate','Looking for place and roomate'),
		('Unspecified','Unspecified'),
	)
	NOTIFICATION_TYPE = (
		('FR','Friend_Request'), #Friend request
		('FA','Friend_Accept'), #Friend request
		('NM','New_Message'), #Messaging
		('U','Unspecified'), #Unspecified
	)
	LEVEL = (
		(0,"0"),
		(1,"1"),
		(2,"2"),
		(3,"3"),
		(4,"4"),
		(5,"5"),
	)


def gethome():
	from shroomme.views import home
	return home