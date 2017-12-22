package sancaes;

/**
 *
 * @author ArachmadiPutra
 * @assistant FinaraImut
 *
 */
import java.util.*;

public class Sancaes {

    /**
     *
     * @param args the command line arguments
     *
     * @info the following script created based on adaptation from the
     * javascript version
     *
     */
//making sure that map contains unique chars only (no repeated characters)
//fDelNul and fDelDup code, copied from Javarevisited problems answer for how to remove duplicate chars from string :
//http://javarevisited.blogspot.co.id/2016/06/how-to-remove-duplicate-characters-from-String-Java.html
    private static String fDelNul(char[] cResChar) {
        StringBuilder sbRCFix = new StringBuilder(cResChar.length);
        for (char c : cResChar) {
            if (c != 0) {
                sbRCFix.append(c);
            }
        }
        return sbRCFix.toString();
    }

    private static String fDelDup(String asText) {
        if (asText == null || asText.length() < 2) {
            return asText;
        }

        boolean[] bAscii = new boolean[256];
        char[] cResChar = asText.toCharArray();
        bAscii[asText.charAt(0)] = true;

        int iDupIdx = 1;
        for (int ia = 1; ia < asText.length(); ia++) {
            if (!bAscii[asText.charAt(ia)]) {
                cResChar[iDupIdx] = cResChar[ia];
                ++iDupIdx;
                bAscii[cResChar[ia]] = true;

            } else {
                cResChar[iDupIdx] = 0;
                ++iDupIdx;
            }
        }

        Arrays.sort(cResChar);
        return fDelNul(cResChar);
    }

//a little help to equal to javascript's String.fromCharCode
    private static String fromCharCode(int... iAsciiIdx) {
        return new String(iAsciiIdx, 0, iAsciiIdx.length);
    }

//regenerates keymap based on password given by encryptor
    private static String fGenKeyMap(String asCodeBase) {
        String asNonCB = "";
        String vasMap = "	" + fromCharCode(10) + "" + fromCharCode(13) + " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ";
        String[] vasMapx = vasMap.split("");
        String asCBFix = fDelDup(asCodeBase);
        for (int ia = 0; ia < vasMap.length(); ia++) {
            if (asCBFix.indexOf(vasMapx[ia]) == -1) {
                asNonCB += vasMapx[ia];
            }
        }
        return asCBFix + asNonCB;
    }

//encryption engine
    public static String fEncryptText(String asText, String asKey, int iShift) {
        int ib;
        String asKeyMap = fGenKeyMap(asKey), asResult = "";
        String[] asTextx = asText.split(""), asKeyMapx = asKeyMap.split("");
        if (iShift == 0) {
            iShift = asKey.length();
        }
        for (int ia = 0; ia < asText.length(); ia++) {
            ib = asKeyMap.indexOf(asTextx[ia]) + iShift;
            if (ib > asKeyMap.length()) {
                ib = ib - asKeyMap.length();
            }
            asResult += asKeyMapx[ib];
        }
        return asResult;
    }

//decryption engine
    public static String fDecryptText(String asText, String asKey, int iShift) {
        int ib;
        String asKeyMap = fGenKeyMap(asKey), asResult = "";
        String[] asTextx = asText.split(""), asKeyMapx = asKeyMap.split("");
        if (iShift == 0) {
            iShift = asKey.length();
        }
        for (int ia = 0; ia < asText.length(); ia++) {
            ib = asKeyMap.indexOf(asTextx[ia]) - iShift;
            if (ib < 0) {
                ib = ib + asKeyMap.length();
            }
            asResult += asKeyMapx[ib];
        }
        return asResult;
    }

//console test
    public static void main(String[] args) {
        String sSumber, sSandi, sHasilEnc, sHasilDec;
        Scanner ScTest = new Scanner(System.in);
        System.out.print("Type text you want to encrypt : ");
        sSumber = ScTest.nextLine();
        System.out.println();
        System.out.print("Type password to encrypt : ");
        sSandi = ScTest.nextLine();
        System.out.println();
        sHasilEnc = fEncryptText(sSumber, sSandi, 0);
        System.out.print("The encryption result : " + sHasilEnc);
        System.out.println("\n");
        sHasilDec = fDecryptText(sHasilEnc, sSandi, 0);
        System.out.print("The decryption result (from encryption) : " + sHasilDec);
        System.out.println("\n");
    }

}
