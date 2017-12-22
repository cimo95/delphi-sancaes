//making sure that map contains unique chars only (no repeated characters)
function fDelDup(asText) {
	return asText
		.split('')
		.filter(function (item, pos, self) {
			return self.indexOf(item) == pos;
		})
		.sort()
		.join('');
}

//regenerates keymap based on password given by encryptor
function fGenKeyMap(asCodeBase) {
	var acChar, asCBFix, asNonCB = '',
		ia, vasMap = '';
	//for compatibility with windows ascii, we use this map :
		vasMap = '	' + String.fromCharCode(10) + '' + String.fromCharCode(13) + ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ';
	//instead of generating automatically using this loop :
	/*
	  for(ia = 32; ia < 256; ia++)
	  { vasMap += String.fromCharCode(ia);}
	*/
	//by using that precreated map, encrypt~decryption between web-version and desktop-version will be equal
	asCBFix = fDelDup(asCodeBase);
	for (ia = 0; ia < vasMap.length; ia++) {
		if (asCBFix.indexOf(vasMap[ia]) == -1) {
			asNonCB += vasMap[ia];
		}
	}
	return asCBFix + asNonCB;
}

//encryption engine
function sEncryptText(asText, asKey, iShift = 3) {
	var ia, ib, asKeyMap = fGenKeyMap(asKey),
		asResult = '';
	if (iShift == 0) {
		iShift = asKey.length;
	}
	for (ia = 0; ia < asText.length; ia++) {
		ib = asKeyMap.indexOf(asText.split('')[ia]) + iShift;
		if (ib > asKeyMap.length) {
			ib = ib - asKeyMap.length;
		}
		asResult += asKeyMap.split('')[ib];
	}
	return asResult;
}

//decryption engine
function sDecryptText(asText, asKey, iShift = 3) {
	var ia, ib, asKeyMap = fGenKeyMap(asKey),
		asResult;
	asResult = '';
	if (iShift == 0) {
		iShift = asKey.length;
	}
	for (ia = 0; ia < asText.length; ia++) {
		ib = asKeyMap.indexOf(asText.split('')[ia]) - iShift;
		if (ib < 0) {
			ib = ib + asKeyMap.length;
		}
		asResult += asKeyMap.split('')[ib];
	}
	return asResult;
}