from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
	(0,'Deleted'),
	(1,'Pending'),
	(2,'Processing'),
	(3,'Approved'),
	(4,'Rejected'),
	(5,'Cancelled')
	)
Dept = (
	(0,'CSE'),
	(1,'IT'),
	(2,'ECE'),
	(3,'ME'),
	(4,'TEX'),
	(5,'BBA')
	)


LEAVE_TYPES = (
	#(1,'Special Casual Leave'),
	(1,'Casual Leave'),
	(2,'Half Pay Leave'),
	(3,'Commuted Leave'),
	#(3,'On Duty Leave'),
	)
# class Department(models.Model):
# 	name = models.CharField(max_length=100)

# 	class Meta:
# 		ordering = ['name']
# 	def __str__(self):
# 		return self.name


# class Employee(models.Model):
# 	user = models.ForeignKey(User,on_delete=models.CASCADE)	
	# dept = models.ForeignKey('Department',on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.dept


class leave_model(models.Model):
	
	employee = models.OneToOneField(User,on_delete=models.CASCADE)
	dept_name = models.IntegerField(choices=Dept)
	is_new = models.BooleanField(default=True)
	# original= models.ForeignKey('self',null=True,on_delete=models.CASCADE)
	leave_type = models.IntegerField(choices=LEAVE_TYPES,default=1)
	date_from = models.DateField(null=False)
	date_to	= models.DateField(null=True)
	days=models.IntegerField(default=0)
	status = models.IntegerField(choices=STATUS,default=1)
	reason = models.TextField(max_length=200)
	time_generated = models.DateTimeField(auto_now_add=True)
	# time_received = models.DateTimeField(null=True)
	# time_approved = models.DateTimeField(null=True,blank=True)

	class Meta:
		ordering = ['time_generated']

	def __str__(self):
		 return str(self.employee) + ' has requested for leave from ' + str(self.date_from) + ' to ' + str(self.date_to)
