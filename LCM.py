import shutil, os
from datetime import datetime
from subprocess import call

class LCM(object):

	def __init__(self, 
		epm_instance_home="~/Oracle/Middleware/user_projects/epmsystem1/",
		epm_home="~/Oracle/Middleware/EPMSystem11R1/",
		lcm_utility="bin/Utility.sh",
		keep="30",
		dateformat="%Y%m%d-%H%M",
		output_path="./BackupFiles/",
		log_path="./Logs/",
		email_address_list="email@address.com"):
		
		self.epm_instance_home = epm_instance_home
		self.epm_home = epm_home
		self.lcm_utility = lcm_utility
		self.keep = keep
		self.datetoken = datetime.now().strftime(dateformat)
		self.output_path = output_path
		self.log_path = log_path
		self.email_address_list = email_address_list
	
	def execute(self, xml_file):
		self.tempfolder = "./" + self.datetoken
		self.command = self.epm_instance_home + self.lcm_utility
		self.output_file = self.tempfolder + "/temp" + self.datetoken + ".xml"
		if not os.path.exists(self.tempfolder): os.makedirs(self.tempfolder)
		shutil.copy2(xml_file, self.output_file)
		#call([self.command, self.output_file])
		
lcm = LCM()
lcm.execute('test.xml')