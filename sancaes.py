#EN:manually define ascii charmap for compatibility with other version of sancaes
#ID:mendefinisikan deret karakter ASCII secara manual agar sesuai dengan versi sancaes lainnya (Pascal, Java, dan Javascript)
sAscii = "	" + chr(10) + "" + chr(13) + " !#$%&\"()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

###SIMPLE STRING ENCRYPT / DECRYPT

#EN:normal simple string encrypt/decryption using only shift number
#ID:enkripsi/dekripsi string sederhana hanya dengan menggunakan angka banyaknya geseran
def dSimpleCrypt(sTeks,iGeserDari=0,bDekrip=False):
    sHasil = ""
    for cHuruf in sTeks:
        iPos = sAscii.find(cHuruf)-iGeserDari if bDekrip else sAscii.find(cHuruf)+iGeserDari
        iGeserKe = iPos + 255 if iPos < 0 else iPos - 255 if iPos > 255 else iPos
        sHasil+=sAscii[iGeserKe]
    return sHasil

#EN:normal simple string encrypt/decryption using only shift number with Ren'Py built-in variable and tag script compatible
#ID:enkripsi/dekripsi string sederhana hanya dengan menggunakan angka banyaknya geseran yang kompatibel dengan skrip Ren'Py yang mengandung variabel dan tag
def dSimpleCryptRenPy(sTeks,iGeserDari=0,bDekrip=False):
    sHasil = ""
    iModeTag = 0 #1 = [] // 2 = {}
    for cHuruf in sTeks:
        if iModeTag == 0:
            iModeTag = 2 if cHuruf == '{' else 1 if cHuruf == '[' else 0
        if iModeTag != 0:
            sHasil+=cHuruf
            if (cHuruf == '}' and iModeTag == 2) or (cHuruf == ']' and iModeTag == 1):
                iModeTag = 0
        else:
            iPos = sAscii.find(cHuruf)-iGeserDari if bDekrip else sAscii.find(cHuruf)+iGeserDari
            iGeserKe = iPos + 255 if iPos < 0 else iPos - 255 if iPos > 255 else iPos
            sHasil+=sAscii[iGeserKe]
    return sHasil

### SANCAES STRING ENCRYPT / DECRYPT ###

#EN:New ascii charmap generator based on given keyword
#ID:deret karakter ascii baru berdasarkan kata-kunci yang diberikan
def dGenAsciiMap(sKunci):
    sNonAH = ""
    sAsciiHasil = "".join(set(sKunci))
    for cDariAscii in sAscii:
        if sAsciiHasil.find(cDariAscii) == -1:
            sNonAH += cDariAscii
    return sAsciiHasil + sNonAH

#EN:sancaes string encrypt/decryption using keyword to generate ASCII map and shift number
#ID:enkripsi/dekripsi string sancaes menggunakan kata-kunci untuk membuat deret karakter ASCII dan angka banyaknya pergeseran
def dSancaesCrypt(sTeks,sKataKunci,bDekrip=False,iGeserDari = 3):
    iGeserKe=0
    sAsciiMap = dGenAsciiMap(sKataKunci)
    sHasil=""
    if iGeserDari == 0:
        iGeserDari = len(sKataKunci)
    for cHuruf in sTeks:
        iPos = sAsciiMap.find(cHuruf) - iGeserDari if bDekrip else sAsciiMap.find(cHuruf) + iGeserDari
        iGeserKe = iPos + 255 if iPos < 0 else iPos - 255 if iPos > 255 else iPos
        sHasil += sAsciiMap[iGeserKe]
    return sHasil

#EN:sancaes string encrypt/decryption using keyword to generate ASCII map and shift number with Ren'Py built-in variable and tag script compatible
#ID:enkripsi/dekripsi string sancaes menggunakan kata-kunci untuk membuat deret karakter ASCII dan angka banyaknya pergeseran yang kompatibel dengan skrip Ren'Py yang mengandung variabel dan tag
def dSancaesCryptRenPy(sTeks,sKataKunci,bDekrip=False,iGeserDari=3):
    sHasil = ""
    iModeTag = 0
    if iGeserDari == 0:
        iGeserDari = len(sKataKunci)
    for cHuruf in sTeks:
        if iModeTag == 0:
            iModeTag = 2 if cHuruf == '{' else 1 if cHuruf == '[' else 0
        if iModeTag != 0:
            sHasil+=cHuruf
            if (cHuruf == '}' and iModeTag == 2) or (cHuruf == ']' and iModeTag == 1):
                iModeTag = 0
        else:
            iPos = sAsciiMap.find(cHuruf) - iGeserDari if bDekrip else sAsciiMap.find(cHuruf) + iGeserDari
            iGeserKe = iPos + 255 if iPos < 0 else iPos - 255 if iPos > 255 else iPos
            sHasil += sAsciiMap[iGeserKe]
    return sHasil