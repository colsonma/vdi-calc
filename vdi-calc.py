#Something I do a lot- Jon Owings
#Edited for Updated Model types by Mike Colson
#VMware View and Citrix VDI Calculator 
import os
import uuid
import urlparse
import redis
import json
import Tkinter as tk
from flask import Flask
app = Flask(__name__)


rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])
r.set("ioPerBlock", 8200.00
      "diskOvr", 0.91
      "maxDM_5300" = 2
      "maxDM_5500", 3
      "maxDM_5700", 4
      "maxDM_7500", 8
      "max1rg_1TB", 9940
      "max1rg_2TB", 19880
      "max1rg_3TB", 29820
      "Model", 5400, 5600, 5800, 7600)


class calc(object):
 
 def __init__(self, calc_home):
     print "calc __init__ has calc_home", calc_home
     self.calc_home = calc_home
 
 if IOPS == (<12300)
    Model == (5400)
    
 elif IOP == (>12300<24601)
    Model == (5600)

 elif
#get '/calc_home' do <old code from Ruby>
#Trying Tkinter for OptionMenu 
 def select():
	sf = "values is %s" % var.get()
	root.title(sf)
	
 
 def vditype=(self):
	vt = "value is %s" % var.get()
	Vdi.type(vt)

	Vdi = tk.Tk()
	Vdi.title("tk.VDITYPE")
	
	var = tk.StringVar(Vdi)
	var.set('Citrix PVS')
	
	choices = ['Citrix PVS', 'Citrix MCS', 'VMware Horizon']
	Option =tk.OptionMenu(Vdi, var, *choices)

   def avgRam=(self):
	action = raw_input("> ")
	
    @memRes=params[:memRes]
    @nDesktops=params[:nDesktops]
    @ioSteady=params[:ioSteady]
    @baseImg=params[:baseImg]
    @custIO= @nDesktops.to_f * @ioSteady.to_f
    @conCurr=params[:conCurr]
    @userData=params[:userData]
    @adjuserData= @userData.to_i * @nDesktops.to_i 
    @addStor=params[:addStor]
    @storProto=params[:storProto]
    @userDataType=params[:userDataType]
    @diskPer=(@vditype == "Citrix PVS" ? "16" : "15")
    @maxConCurr = @nDesktops.to_f * (@conCurr.to_f/100)
    @numBlk= @custIO / ioPerBlock
    @adjNumBlk= @numBlk.ceil
    @hsFlash= (@adjNumBlk * 2)/30
    @hsFlashUp= (@hsFlash > 1 ? 2 : 1) 
    @numFlash= (@adjNumBlk * 2) + @hsFlashUp
    @numSAS= (@diskPer.to_f * @adjNumBlk).to_i
    @capReq= ((@avgRam.to_f * (@memRes.to_f/100)) + @maxLC.to_f) * @nDesktops.to_f
    @hsSAS= @numSAS/30
    @hsSASUp= @hsSAS.ceil
    @numSAS= @diskPer.to_f * @adjNumBlk + @hsSASUp
    @driveType= (@maxLC.to_f < 3 ? "300" : "600")
    @dMover= @custIO/12300 + 1
    @adjMover= @dMover.ceil
    @dispMover= (@storProto == "NFS" ? @adjMover : "None")
    #@userDataType=(@adjuserData.to_i <= 9940 ? "1TB" : "2TB")
    #@userDataType=(@adjuserData.to_i >= 29820 ? "3TB" : @userDataType)
    @userDTnum=(@userDataType == "1TB" ? 1024 : 2048)
    @userDTnum=(@userDataType == "3TB" ? 3072 : 900)
    @userDiskRaid=(@userDataType == "1TB" ? 16 : 5)
    @userDiskRaid=(@userDataType == "2TB" ? 16 : @userDiskRaid)
    @userDiskRaid=(@userDataType == "3TB" ? 16 : @userDiskRaid)
    @userDiskRaidPenalty=(@userDiskRaid == "16" ? 2 : 1)
    @numuserRG= (@adjuserData.to_f / (@userDTnum * (@userDiskRaid - @userDiskRaidPenalty) * 0.71)).ceil
    @userDataNum= @userDiskRaid * @numuserRG
    @userDataNum=(@userData.to_i == 0 ? 0 : @userDataNum)
    @userDataHS = (@userDataNum.to_f/30).ceil
    @totaluserDataNum= @userDataNum + @userDataHS
    @totalDriveCount= @numSAS + @numFlash + @totaluserDataNum
    @vnxType= (@nDesktops.to_i < 1501 ? "VNX5400" : "VNX5600")
    @vnxType= (@nDesktops.to_i > 3000 ? "VNX5800" : @vnxType)
    @vnxType= (@nDesktops.to_i > 4500 ? "VNX7600" : @vnxType)
    @vnxType= (@nDesktops.to_i > 7500 ? "Use Multiple VNX Arrays" : @vnxType)
    @adjvnxType= (@adjMover.to_i == 2 ? "VNX5400" : "VNX5300")
    @adjvnxType= (@adjMover.to_i > 2 ? "VNX5600" : @adjvnxType)
    @adjvnxType=(@adjMover.to_i == 4 ? "VNX5800" : @adjvnxType)
    @adjvnxType=(@adjMover.to_i > 4 ? "VNX7600" : @adjvnxType)
    @adjvnxType=(@storProto == "NFS" ? @adjvnxType : "None Needed, FC Selected")
    @maxDrives=(@adjvnxType == "VNX5400" ? 125 : 250)
    @maxDrives=(@adjvnxType == "VNX5600" ? 250 : @maxDrives)
    @maxDrives=(@adjvnxType == "VNX5800" ? 500 : @maxDrives)
    @maxDrives=(@adjvnxType == "VNX7600" ? 1000 : @maxDrives)
    @adjvnxType= (@totalDriveCount <= 125 ? @adjvnxType : "VNX5600" )
    @adjvnxType= (@totalDriveCount >= 250 ? "VNX5800" : @adjvnxType)
    @adjvnxType=(@totalDriveCount >= 500 ? "VNX7600" : @adjvnxType)
    @adjvnxType=(@totalDriveCount > 1000 ? "Error, Total Drives exceeds suggested array Type's maximum" : @adjvnxType)    
    @moreFlash=(@nDesktops.to_i > 1000 && @vnxType == "VNX5400" ? 2 : "None")
    @baseFlashhelp=@adjNumBlk.to_i * 2
    @baseFlash=(@baseImg.to_i < 8 ? "None" : @baseFlashhelp)
    @lic=(@adjuserData.to_i > 0 ? "CIFS" : "No File")
    @lic=(@storProto == "NFS" && @adjuserData.to_i > 0 ? "NFS,CIFS" : @lic)
    erb :calc_home 

@app.route('/')
def hello():
	r.incr("hit_counter")
 
	return """
	<html>
	<body bgcolor="white">

	<head>
	 <meta charset="utf-8" />
	 <meta name="viewport" content="width=device-width" />
	 <title>VNX VDI Calculator</title>
	
	 <link rel="stylesheet" href="css/normalize.css" />
	  
	 <link rel="stylesheet" href="css/foundation.css" />
	  
	
	 <script src="js/vendor/custom.modernizr.js"></script>
	</head>
	<body>
	<div class="row">
	  <div class="panel">
	<h1>Results VNX Calculator*</h1>
	  <p><b>*Not official sanctioned by EMC, I did this in my spare time.</b> If you have questions please send me a message <a href="http://twitter.com/jon_2vcps">@jon_2vcps</a>. The <a href="https://github.com/2vcps/vdi-calc">source is on github</a> 
	
	<p>This calculator attempts to estimate the EMC VNX storage needed for VMware View, Citrix PVS and MCS environments. It is based on the math
	from this <a href=http://www.emc.com/collateral/software/white-papers/h11096-vdi-sizing-wp.pdf>whitepaper.</a>
	Remember this is just an estimation and real world experience can never be replaced. Use the as a guide in order to get started.
	<br>
	
	<table border=1>
	 <tr>
	 <td>Compenents</td><td>Quantity</td><td>Notes</td>
	 </tr>
	 <tr>
	 <td>VNX Model</td><td><%= @vnxType %></td><td>This is based on Desktops</td>
	 </tr>
	 <tr>
	<td>VNX Based on Data Movers and Drive Count</td><td><%= @adjvnxType %></td><td>Use this Model VNX if you are using NFS</td>
	</tr>
	 <tr>
	 <td><%= @driveType %>GB, 15k SAS Drives</td><td><%= @numSAS.to_i %></td><td>Includes hotspares</td>
	 </tr>
	 <tr>
	 <td>100 GB, EFD Drives</td><td><%= @numFlash %></td><td>Includes Hotspares and Additional Drives below</td>
	 </tr>
	 <tr>
	 <td><%= @userDataType %>, User Data Drives (900GB=10kSAS, 1TB+ = NL-SAS)</td><td><%= @totaluserDataNum %></td><td>Include Hotspares</td>
	 </tr>
	 <tr>
	 <td>Data Movers</td><td><%= @dispMover %></td><td>Active + One Standby</td>
	 </tr>
	
	  <tr>
	 <td>Additional FAST Cache</td><td><%= @moreFlash %></td><td>Included in Total EFD</td>
	 </tr>
	   <tr>
	 <td>Additional EFD For Base Images</td><td><%= @baseFlash %></td><td>Included in Total EFD</td>
	 </tr>
	 <tr>
	 <td>License</td><td><%= @lic %></td><td></td>
	 </tr>
	 <tr>
	 <td>Total Drives (All Types)</td><td><%= @totalDriveCount %></td><td></td>
	 </tr>
	 </table><br/>
	 </p>
	  <br />
	 </div>
	</div>
	<script>
	  document.write('<script src=' + 
	  ('__proto__' in {} ? 'js/vendor/zepto' : 'js/vendor/jquery') +'.js><\/script>')
	  </script>
	  <script src="js/foundation/foundation.js"></script>
	  <script src="js/foundation/foundation.alerts.js"></script>
	  <script src="js/foundation/foundation.clearing.js"></script>
	  <script src="js/foundation/foundation.cookie.js"></script>
	  <script src="js/foundation/foundation.dropdown.js"></script>
	  <script src="js/foundation/foundation.forms.js"></script>
	  <script src="js/foundation/foundation.joyride.js"></script>
	  <script src="js/foundation/foundation.magellan.js"></script>
	  <script src="js/foundation/foundation.orbit.js"></script>
	  <script src="js/foundation/foundation.placeholder.js"></script>
	  <script src="js/foundation/foundation.reveal.js"></script>
	  <script src="js/foundation/foundation.section.js"></script>
	  <script src="js/foundation/foundation.tooltips.js"></script>
	  <script src="js/foundation/foundation.topbar.js"></script>
	  <script>
	  $(document).foundation();
	  </script>	
	</body>

	</html>
	""".format(COLOR,my_uuid,r.get("hit_counter"))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))