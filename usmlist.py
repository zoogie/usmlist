import os,sys,struct,binascii,requests
#python 3

count=0
with open("usmlist.bin","wb") as f:
	f.write(b"\x00"*(65*0x100))
	f.close()

def getcrc32(url):
	r = requests.get(url)
	return binascii.crc32(r.content)

def add_url(url,filepath):
	global count,f
	print("\n(%d)" % count)
	print("url:  %s\npath: %s" % (url,filepath))
	crc32=getcrc32(url)
	print("crc32: %08X" % crc32)
	if(len(url) > 0xC0 or len(filepath) > 0x40):
		print("string length error in %d" % count)
		f.close()
		os.system("rm usmlist.bin")
		exit()
	f.seek(count*0x100)
	f.write(url.encode('ascii'))
	f.seek(count*0x100 + 0xC0)
	f.write(filepath.encode('ascii'))
	f.seek(0x4000 + (count*4))
	f.write(struct.pack("<I",crc32))
	count+=1

f=open("usmlist.bin","rb+")
add_url("https://github.com/zoogie/unSAFE_MODE/releases/download/v1.2/usm.bin", 					"/usm.bin")
add_url("https://github.com/hax0kartik/luma-hourlies/releases/download/222-luma3ds-bb07a73/boot.firm",			"/boot.firm") 
add_url("https://github.com/zoogie/DSP1/releases/download/v1.0/DSP1.cia", 						"/cias/DSP1.cia")
add_url("https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.1.0/Anemone3DS.cia",			"/cias/Anemone3DS.cia")
add_url("https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.3dsx",						"/3ds/FBI.3dsx")
add_url("https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.cia",						"/cias/FBI.cia")
add_url("https://github.com/mariohackandglitch/homebrew_launcher_dummy/releases/download/v1.0/Homebrew_Launcher.cia",	"/cias/Homebrew_Launcher.cia")
add_url("https://github.com/KunoichiZ/lumaupdate/releases/download/v2.5/lumaupdater.cia",				"/cias/lumaupdater.cia")
add_url("https://github.com/ihaveamac/ctr-no-timeoffset/releases/download/v1.1/ctr-no-timeoffset.3dsx",			"/3ds/ctr-no-timeoffset.3dsx")
add_url("https://github.com/FlagBrew/Checkpoint/releases/download/v3.7.4/Checkpoint.cia",				"/cias/Checkpoint.cia")
add_url("https://github.com/zoogie/GodMode9/releases/download/v1.9.2pre1/GodMode9.firm",				"/luma/payloads/GodMode9.firm")
add_url("https://github.com/zoogie/GodMode9/releases/download/v1.9.2pre1/GM9Megascript.gm9",				"/gm9/scripts/GM9Megascript.gm9")
f.close()
if count > 64:
	print("error too many entries")
	os.system("rm usmlist.bin")