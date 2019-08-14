<?php

/**
 *
 * @author ArachmadiPutra
 * @assistant FinaraImut
 *
 */

/**
 * WARNING !!!
 * These function are still not working,
 * if you read this from cimorepo.rf.gd/sancaes/ then 
 * you've been force enable the "Download Source Code (PHP)" button by inspect element (how gross you are !?)
 * let us finish these function, and we'll let you know by legally enable the "Download Source Code (PHP)" button
 **/

//making sure that map contains unique chars only (no repeated characters)
function fDelDup($asText) {
    return implode('', str_split(count_chars($asText, 3)));
}

//regenerates keymap based on password given by encryptor
function fGenKeyMap($asCodeBase) {
    $vasMap = str_split('	' . chr(10) . '' . chr(13) . ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ');
    $asCBFix = fDelDup($asCodeBase);
    $asNonCB = '';
    for ($ia = 0; $ia < count($vasMap); $ia++) {
        if (strpos($asCBFix, $vasMap[$ia]) == false) {
            $asNonCB .= $vasMap[$ia];
        }
    }
    return $asCBFix.$asNonCB;
}

//encryption engine
function sEncryptText($asText, $asKey, $iShift = 3) {
    $asKeyMap = fGenKeyMap($asKey);
    $ib = 0;
    $asResult = '';
    if ($iShift == 0) {
        $iShift = strlen($asKey);
    }
    for ($ia = 0; $ia < strlen($asText); $ia++) {
        $ib = strpos($asKeyMap, str_split($asText)[$ia]) + $iShift;
        if ($ib > strlen($asKeyMap)) {
            $ib = $ib - strlen($asKeyMap);
        }
        $asResult .=  str_split($asKeyMap)[$ib];
    }
    return $asResult;
}

//decryption engine
function sDecryptText($asText, $asKey, $iShift = 3) {
    $asKeyMap = fGenKeyMap($asKey);
    $ib = 0;
    $asResult = '';
    if ($iShift == 0) {
        $iShift = strlen($asKey);
    }
    for ($ia = 0; $ia < strlen($asText); $ia++) {
        $ib = strpos($asKeyMap, str_split($asText)[$ia]) + $iShift;
        if ($ib < 0) {
            $ib = $ib + strlen($asKeyMap);
        }
        $asResult .=  str_split($asKeyMap)[$ib];
    }
    return $asResult;
}

echo 'your text => '.$_GET['a'].'<br>';
echo 'your pass => '.$_GET['b'].'<hr>';
echo 'passer => '.fDelDup($_GET['b']).'<br>';
echo 'mapper => '. fGenKeyMap(fDelDup($_GET['b'])).'<br>';
$enc = sEncryptText($_GET['a'], $_GET['b'], 0);
echo 'encrypted =>'.$enc.'<br>';
$dec = sDecryptText($enc, $_GET['b'], 0);
echo 'decrypted =>'.$dec;
?>

