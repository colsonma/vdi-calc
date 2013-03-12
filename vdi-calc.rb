#Something I do a lot- Jon Owings
#VMware View and VDI Calculator 
require 'sinatra'
require 'rubygems'
#Samples::
#vdiType = "VMware View"
#nDesktops = params[:nDesktops]
#ioSteady = 10
#conCurr = params[:conCurr]
#maxLC = 4
#avgRam = 2
#memRes = 0.5
#storProto = "NFS"
#userData = 2
#addStor = 4000
#baseImg	= 8
ioPerBlock = 8200.00
#addDrives = 15
diskPer = 15
#diskOvr = 0.91

#capReq = ((avgRam * memRes) + maxLC) * nDesktops /1000







get '/' do
	erb :index
end

get '/calc_home' do
    @vditype=params[:vditype]
    @avgRam=params[:avgRam]
    @memRes=params[:memRes]
    @nDesktops=params[:nDesktops]
    @ioSteady=params[:ioSteady]
    @custIO= @nDesktops.to_f * @ioSteady.to_f
    @conCurr=params[:conCurr]
    @userData=params[:userData]
    @addStor=params[:addStor]
    @maxConCurr = @nDesktops.to_f * (@conCurr.to_f/100)
    @numBlk= @custIO / ioPerBlock
    @adjNumBlk= @numBlk.ceil
    @numFlash= @adjNumBlk * 2
    @addStorage = @addStor.to_f / 300
    @addDrives= @addStorage.ceil
    @numSAS= diskPer * @adjNumBlk + @addDrives
    @capReq= (@avgRam.to_f * @memRes.to_f + @maxLC.to_f) * @nDesktops.to_f/1000
	erb :calc_home 
end



