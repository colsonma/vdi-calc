#Something I do a lot- Jon Owings
#VMware View and Citrix VDI Calculator 
require 'sinatra'
require 'rubygems'

ioPerBlock = 8200.00
diskOvr = 0.91




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
    @storProto=params[:storProto]
    @diskPer=(@vditype == "Citrix PVS" ? "16" : "15")
    @maxConCurr = @nDesktops.to_f * (@conCurr.to_f/100)
    @numBlk= @custIO / ioPerBlock
    @adjNumBlk= @numBlk.ceil
    @hsFlash= (@adjNumBlk * 2)/30
    @hsFlashUp= (@hsFlash > 1 ? 2 : 1) 
    @numFlash= (@adjNumBlk * 2) + @hsFlashUp
    @numSAS= @diskPer.to_f * @adjNumBlk
    @capReq= ((@avgRam.to_f * (@memRes.to_f/100)) + @maxLC.to_f) * @nDesktops.to_f
    @hsSAS= @numSAS/30
    @hsSASUp= @hsSAS.ceil
    @driveType= (@maxLC.to_f < 3 ? "300" : "600")
    @dMover= @custIO/12300 + 1
    @adjMover= @dMover.ceil
    @dispMover= (@storProto == "NFS" ? @adjMover : "None")
    @userDataType=(@userData.to_i <= 10000 ? "1TB" : "2TB")
    @userDataNum=@adjNumBlk * 16
    @userDataHS = (@userDataNum.to_f/30).ceil
    @totaluserDataNum= @userDataNum + @userDataHS
    @vnxType= (@nDesktops < 1501 ? "VNX5300" : (@nDesktops < 3001 ? "VNX5500" : (@nDesktops < 4501 ? "VNX5700" : "VNX7500")))
    erb :calc_home 
end



