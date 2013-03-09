#Something I do a lot- Jon Owings
#VMware View and VDI Calculator 
#require 'rubygems'
require 'sinatra'

vdiType = "VMware View"
nDesktops = 1000.00
ioSteady = 10
conCurr = 1
maxLC = 4
avgRam = 2
memRes = 0.5
storProto = "NFS"
userData = 2
addStor = 4000
baseImg	= 8
ioPerBlock = 8200.00
addDrives = 15
diskPer = 15
diskOvr = 0.91


maxConCurr = nDesktops * conCurr
custIO = nDesktops * ioSteady
numBlk = custIO / ioPerBlock 
adjNumBlk = numBlk.ceil
numFlash = adjNumBlk * 2
numSAS = diskPer * adjNumBlk + addDrives
capReq = ((avgRam * memRes) + maxLC) * nDesktops /1000

puts "Type of VDI is #{vdiType}"
puts "Maximum Concurrent Desktops #{maxConCurr}"
puts "Number of Customer IOps #{custIO}"
puts "#{numBlk}"
puts "Number of Additional Drives needed for applications: #{addDrives}"
puts "Number of VDI Blocks #{adjNumBlk}"
puts "Number of Flash Drives needed #{numFlash}"
puts "Number of SAS drives #{numSAS}"
puts "Capacity Total Required for Linked Clones #{capReq}TB"




get '/' do
	greeting = "Hello, World!"
	
end

get '/calc_home' do
	erb :calc_home, :locals => {:capReq => params[:capReq]}
end


