#Something I do a lot- Jon Owings
#VMware View and VDI Calculator 
#require 'rubygems'
require 'sinatra'
require 'rubygems'

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



helpers do
  def max_con(nDesktops,conCurr)
      @maxConCurr = @nDesktops * @conCurr
  end
end

custIO = nDesktops * ioSteady
numBlk = custIO / ioPerBlock 
adjNumBlk = numBlk.ceil
numFlash = adjNumBlk * 2
numSAS = diskPer * adjNumBlk + addDrives
capReq = ((avgRam * memRes) + maxLC) * nDesktops /1000







get '/' do
	erb :index
end

get '/calc_home' do
    @vditype=params[:vditype]
    @nDesktops=params[:nDesktops]
    @custIO=params[:custIO]
    @maxConCurr = max_con(@nDesktops,@ioSteady)
    @numBlk=params[:numBlk]
    @adjNumBlk=[:adjNumBlk]
    @numFlash=params[:numFlash]
    @numSAS=params[:numSAS]
    @capReq=params[:capReq]
		erb :calc_home 
end



