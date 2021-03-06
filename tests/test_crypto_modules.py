import unittest
from pygp import *

class Test_AES(unittest.TestCase):


    def test_removepadding(self):

        data = 'E3144F08A0000001510000009F70020101C5039EFE8080000000000000000000'
        dataunpadd = Remove_ISO_9797_M2_Padding(data)
        self.assertEqual(dataunpadd, 'E3144F08A0000001510000009F70020101C5039EFE80')
    
    def test_AES_CBC(self):

        echo('## Perform the AES_CBC operation')
        value = AES_CBC("22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22", "11223344556677881122334455667788")
        self.assertEqual(value, "A2405D73459F58CC8D157A856A2FBCD1")
        value = AES_INV_CBC("A2405D73459F58CC8D157A856A2FBCD1", "11223344556677881122334455667788")
        self.assertEqual(value, "22222222222222222222222222222222")

        echo('## Perform a AES CBC ENC with data not a multiple of 16 bytes, No Exception must be thrown')
        value = AES_CBC("222222222222222222222222222222222222", "11223344556677881122334455667788")
        self.assertEqual(value, "A2405D73459F58CC8D157A856A2FBCD165D412EF1B7194E111BB4559C48BBE2C")
        value = AES_INV_CBC("A2405D73459F58CC8D157A856A2FBCD165D412EF1B7194E111BB4559C48BBE2C", "11223344556677881122334455667788")
        self.assertEqual(value, "2222222222222222222222222222222222220000000000000000000000000000")

        echo('## Perform a AES CBC ENC with data not a multiple of 16 bytes, No Exception must be thrown')
        value = AES_CBC("22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 ", "11223344556677881122334455667788")
        self.assertEqual(value, "A2405D73459F58CC8D157A856A2FBCD1237D451383D6567D86B08ABF61CCC83D")
        value = AES_INV_CBC("A2405D73459F58CC8D157A856A2FBCD1237D451383D6567D86B08ABF61CCC83D", "11223344556677881122334455667788")
        self.assertEqual(value, "2222222222222222222222222222222222222222222222222222222222222200")

    def test_AES_ECB(self):

        echo('## Perform the AES_ECB operation')
        value = AES_ECB("22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22", "11223344556677881122334455667788")
        self.assertEqual(value, "A2405D73459F58CC8D157A856A2FBCD1")
        value = AES_INV_ECB("A2405D73459F58CC8D157A856A2FBCD1", "11223344556677881122334455667788")
        self.assertEqual(value, "22222222222222222222222222222222")

        echo('## Perform a AES CBC ENC with data not a multiple of 16 bytes, NotADirectoryError Exception must be thrown')
        value = AES_ECB("22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22", "11 22 33 44 55 66 77 88 11 22 33 44 55 66 77 88 1122334455667788")
        self.assertEqual(value, "EDEE2999166FEE5FD287D17E2A523B00EDEE2999166FEE5FD287D17E2A523B008EEC8515284925F8309C6591AB8D7D53")
        value = AES_INV_ECB("EDEE2999166FEE5FD287D17E2A523B00EDEE2999166FEE5FD287D17E2A523B008EEC8515284925F8309C6591AB8D7D53", "11 22 33 44 55 66 77 88 11 22 33 44 55 66 77 88 1122334455667788")
        self.assertEqual(value, "222222222222222222222222222222222222222222222222222222222222222222220000000000000000000000000000")

        echo('## Perform a AES CBC ENC with data not a multiple of 16 bytes, No Exception must be thrown')
        value = AES_ECB("22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22 22", "11 22 33 44 55 66 77 88 11 22 33 44 55 66 77 88 11223344556677881122334455667788")
        self.assertEqual(value, "FF2C4FB4B43B9E00B8A1D8C8498FC8B2FF2C4FB4B43B9E00B8A1D8C8498FC8B2D265047D885C507BCD3FA20230133845")
        value = AES_INV_ECB("FF2C4FB4B43B9E00B8A1D8C8498FC8B2FF2C4FB4B43B9E00B8A1D8C8498FC8B2D265047D885C507BCD3FA20230133845", "11 22 33 44 55 66 77 88 11 22 33 44 55 66 77 88 11223344556677881122334455667788")
        self.assertEqual(value, "222222222222222222222222222222222222222222222222222222222222222222220000000000000000000000000000")        

    def test_DES3_ECB(self):
        echo('## Perform the DES3_ECB operation')
        value = DES3_ECB("1111111111111111", "123456781234567812345678123456781234567812345678")
        self.assertEqual(value, "6590D1A7438AB751")
        value = DES3_INV_ECB("6590D1A7438AB751", "123456781234567812345678123456781234567812345678")
        self.assertEqual(value, "1111111111111111")
        value = DES3_ECB("1111111111111111", "11223344556677881122334455667788")
        self.assertEqual(value, "05E9DCD752678426")
        value = DES3_INV_ECB("05E9DCD752678426", "11223344556677881122334455667788")
        self.assertEqual(value, "1111111111111111")
        
        value = DES_ECB("1111111111111111", "1234567812345678")
        self.assertEqual(value, "6590D1A7438AB751")

        value = DES3_ECB("0000000000000000", "475627365635E6F6964707972736E654")
        self.assertEqual(value, "2E4A9941623FC04E")


    def test_DES3_CBC(self):
        echo('## Perform the DES3_CBC operation')
        value = DES3_CBC("620D8002001082010183020001A10080", "123456781234567812345678123456781234567812345678", "0000000000000000")
        self.assertEqual(value, "C2392DBE22F24367ED9FEBBA9A84C6A2")


        value = DES3_INV_CBC("C2392DBE22F24367ED9FEBBA9A84C6A2", "123456781234567812345678123456781234567812345678")
        self.assertEqual(value, "620D8002001082010183020001A10080")

        value = DES3_CBC("1111111111111111", "11223344556677881122334455667788")
        self.assertEqual(value, "05E9DCD752678426")
        value = DES3_INV_CBC("05E9DCD752678426", "11223344556677881122334455667788")
        self.assertEqual(value, "1111111111111111")
    

    def test_MAC33(self):
        echo('## Perform the MAC33 operation')
        value = MAC33("01020304050607080102030405060708", "1122334455667788 6655665523564465", "8992255663311589")
        self.assertEqual(value, "3435BDF4DF32605D")
        data = ISO_9797_M2_Padding("2B510AB489F05EEE0168393E465B5BDB", 8)
        value = MAC33(data, "F5FBE35D9ECCA2AF6A5DCDCD9DD0E443")
        self.assertEqual(value, "92B4251F9A74DCAB")

    
    def test_MAC(self):
        echo('## Perform the MAC operation')
        value = MAC("11111111111111111111111111111111", "1234567812345678", "4444444444444444")
        self.assertEqual(value, "5F65ED88D860723C")
        value = MAC("1111111111111111", "1234567812345678", "4444444444444444")
        self.assertEqual(value, "A592725543D72D93")
    
    def test_MAC3(self):
        echo('## Perform the MAC3 operation')
        value = MAC3("8482000010B1AF3A86C447E3C8", "9A2D5FBF78BD2ACC66BDC3FC62935476")
        self.assertEqual(value, "B42ABAB0B7C1BB01")
        
        value = MAC3("8482000010B1AF3A86C447E3C8", "9A2D5FBF78BD2ACC66BDC3FC62935476", 'ISO_9797_M2')
        self.assertEqual(value, "B42ABAB0B7C1BB01")

        value = MAC3("8482000010B1AF3A86C447E3C8", "9A2D5FBF78BD2ACC66BDC3FC62935476", 'ISO_9797_M2', '0000000000000000')
        self.assertEqual(value, "B42ABAB0B7C1BB01")
        
        
        value = MAC3("02003F08A00000007707020109A0000000010101010114738F8ADBF0E7F2DBC762FB799495A5D3284B377916EF00B612420660616263646545081434128014341280800000000000", "01020304050607080102030405060708", None, "0000000000000000")
        self.assertEqual(value, "8410AD6200722C04")

    def test_AES_CMAC(self):
        echo('## Perform the AES_CMAC operation')
        value = AES_CMAC("8482000010B1AF3A86C447E3C8800000", "9A2D5FBF78BD2ACC66BDC3FC62935476")
        self.assertEqual(value, "70EBAA284178BDC3BAC0D18E97CF2BEA")
        value = AES_CMAC("77ef0286361f65c5825f794ce0b08b46 9bbde9dd0a114309158857a5f603cec8 3d60605217aa3fc5cf8cb357950c0145 7f769269cd95510f71295505cf96c0f1", "C1DAE7E7DEC1B33BFC5C4794F3AFE242A4AA07D23A5BDCDF")
        self.assertEqual(value, "54106A2CD724145205827A65C562CED2")
        value = AES_CMAC("77ef0286361f65c5825f794ce0b08b46 9bbde9dd0a114309158857a5f603cec8 3d60605217aa3fc5cf8cb357950c0145 7f769269cd95510f71295505cf96c0f1", "c1dae7e7dec1b33bfc5c4794f3afe242a4aa07d23a5bdcdfb061d12b94a481ee")
        self.assertEqual(value, "1FC141E9A7D6F1D7C2749C0B95BEE7EC")
        
    
   
    def test_SHA_1(self):
        
        mod_1024_1 = '00010203040506070 8090A0B0C0D0E0F\
                       A8946168441642151 24842163EFC1321 \
                       00010203040506070 8090A0B0C0D0E0F \
                       A8946168441642151 24842163EFC1321 \
                       00010203040506070 8090A0B0C0D0E0F \
                       00010203040506070 8090A0B0C0D0E0F \
                       A8946168441642151 24842163EFC1321 \
                       A8946168441642151 24842163EFC1321'
        value = SHA1(mod_1024_1)
        
        self.assertEqual(value, "8EBC1D799622B65E7B10D7873C0C6A731CD17D1B")   
    
    def test_224_1(self):
    
        input = '00010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC132100010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC1321'
        value = SHA224(input)
        self.assertEqual(value, "D0DB3580E7259C096F9E52C9E6988CEC48E8C812704205E4381C1C64") 
    
    def test_256_1(self):
        input = '00010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC132100010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC1321'
        value = SHA256(input)
        self.assertEqual(value, "F652BAE15791BE1C35F0031C617ADD706111D705BABBEAD3D9A2B2B3F93D894B")    

    def test_384_1(self):
        input = '00010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC132100010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC1321'
        value = SHA384(input)
        self.assertEqual(value, "272A2791C6CC4382976FCE1EA9E6D9A75983CFCCF4FD0A14D64307FD51E1AF0938F444681A147C4BF98AAF81B0CE7833")

    def test_512_1(self):
        input = '00010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC132100010203040506070 8090A0B0C0D0E0FA8946168441642151 24842163EFC1321'
        value = SHA512(input)
        self.assertEqual(value, "282A974859C7AA6A3F1EF7D08FA83ECC7A8A17C085100ADC3A62B63EB8C1CF116EE4F9153E92021ABD4540653FF4AD99D52E3FC3C3C34D497327540579A981A1")

    def test_MD5_1(self):
        input = '000102030405060708090A0B0C0D0E0F'
        value = MD5(input)
        self.assertEqual(value, "1AC1EF01E96CAF1BE0D329331A4FC2A8")

    def test_DSA_1(self):
         private, public = generate_DSA_keys(1024)   
         input = '000102030405060708090A0B0C0D0E0F'
         signature = private.sign(input)
         isOk = public.verify(input, signature)
         self.assertEqual(isOk, True)


    def test_DSA_2(self):
        import binascii, struct
        p = "8E8CD60F9ADFA9C6A11D6C885147BB5502070E75330D71C5D777A4D4C6D8E6802F3DB6AF80A709BE4EDB1E056E292C6D09BCCE121DCF5225D450B2BD76B53E3FAAAE359F95F316EE8927B8E2EF24F2670D3C25C053D69FC07E69B3D29764D518EE6CD7C2233D87BB6E765F1560366D4990FE76A648889818985AEE0874E2BFB7"
        q = "FC02E2B45602977B83657180396E0749AB22DE4F"
        g = "89420A92C5E7D1D6DE9EC14A928E0F5DA8064FF5BA721F5E5356B70B7B6E61501527839746DEEE91429FE616D21EC2CFBF677DA829D222EBCF131792A3AF0D1CBA8DEB0E76ED206FEC35F6EE211FFC4DE6AEC8EE704E2BFBECD8749EFB7A1B6B7E4C8F562BB8C57A42AC9864050D8077782E11C9B6960EAF7F959B94BAA27570"
        private_key = "F06E13B7FD7D6BDCB2080ADFED4C076BB618D0E9"
        public_key = "36413F5B3E277F78C815BA8FAB9A39934367544F6A80768C49CEB6E71CFA95E74894D67FA0BC1096D07F1F2CBFBFFBB54261B1AAE5CE17235BEA228EC7765A0894172EDF658C3F455FE9DAD6CA567EED47FC74634C413E7D80A3311869370863DEEA4F6C851300C8671E79DA8E107597B22AB27636A8E0099B17A3A8B00FECF3"
        private, public = build_DSA_keys(p, q, g, public_key, private_key)  
        input = '000102030405060708090A0B0C0D0E0F'
        signature = private.sign(input)
        isOk = public.verify(input, signature)
        self.assertEqual(isOk, True)
    
    def test_DSA_3(self):
        
        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"
        q = "FC27439DF979A74A090C4B96C7D3FB5A5E43FB13"
        g = "C98C54A58DFB17C677405FD05C22CD494BD8D65B7DF8435182205612958B0662ABB12599C24BB7C10F68889246C1295C3174EFA040F871D72DB87D6884D47BC5C236F4318002281232CA296B45F6E6A763E55B6342336A9315A1DD78B349E1D3556E13739AD93E803BC84962BFDEB73A4DE60C92C0417C9C7430ACFB4D48F36B"
        private_key = "8008BB60C958BA9E07C040C0E74B9A413F0B6DEF"
        public_key = "A9CA9890875976F56BCBF7335CC9F7013809955DC13133561C0F86A09AA4F806E959252A13C419632353E5A2B124F7606FA51D3F5C0AE193A8F5D3EAC42294351A9D903409656B8D7F7766951FD0690BE5793B8AA9925ECDC1FAB47EEA5C4117D97E52B0AADA729846372D4490AA7219CF53A03F22E90276B33DC6B11C799841"
        private, public = build_DSA_keys(p, q, g, public_key, private_key)  
        input = '000102030405060708090A0B0C0D0E0F'
        signature = DSA_signature(input, private)
        isOk = DSA_verify(input, signature, public)
        self.assertEqual(isOk, True)

    def test_DSA_4(self):
        
        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"
        q = "FC27439DF979A74A090C4B96C7D3FB5A5E43FB13"
        g = "C98C54A58DFB17C677405FD05C22CD494BD8D65B7DF8435182205612958B0662ABB12599C24BB7C10F68889246C1295C3174EFA040F871D72DB87D6884D47BC5C236F4318002281232CA296B45F6E6A763E55B6342336A9315A1DD78B349E1D3556E13739AD93E803BC84962BFDEB73A4DE60C92C0417C9C7430ACFB4D48F36B"
        private_key = "8008BB60C958BA9E07C040C0E74B9A413F0B6DEF"
        public_key = "A9CA9890875976F56BCBF7335CC9F7013809955DC13133561C0F86A09AA4F806E959252A13C419632353E5A2B124F7606FA51D3F5C0AE193A8F5D3EAC42294351A9D903409656B8D7F7766951FD0690BE5793B8AA9925ECDC1FAB47EEA5C4117D97E52B0AADA729846372D4490AA7219CF53A03F22E90276B33DC6B11C799841"
        private, public = build_DSA_keys(p, q, g, public_key, private_key)  
        input = p
        signature = DSA_signature(input, private, 'SHA256')
        isOk = DSA_verify(input, signature, public, 'SHA256')
        self.assertEqual(isOk, True)
    
    def test_RSA_1(self):
         p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"
         private, public = generate_RSA_keys('03', 2048)   
         input = p
         signature = RSA_signature(input, private)
         isOK = RSA_verify(input, signature, public)
         self.assertEqual(isOK, True)
    
    def test_RSA_2(self):
        Message = "0001FFFFFFFFFFFFFFFFFFFFFFFFFFFF"
        Q = "db80f47f9db0417f2e463e0a45ca595b95a06f073cd060b493fbeef260989febb3954f3f49cfe7a9bc911fc0bccdd9ecd0e4354e111d669513592d14b157d74d6dc63006b5806d3067f1d6701734fcb731642d9b9c9c2ad9f34c6b19f5dd709485f9854593a74ea59f0c80759dbb62cf332465027b974af1b03164f06f9a6a79"
        P = "f3cbfe594733e1f48ac12b7d44bc9faa3efaabac1dc22a8e27daa20b3e7856104c8709f94bf6b10461fb7b8a3025d8482149ce14f6a2c9eccd6e97abdf0c56c4cef1d1d8bffa3f5d3f05d9d3ef43744020efd62a98a7a138cb34c5bd1b6c3ca47df9a09ea226c1e73cc9f29597746628d00c90ca78b5d946c1fc10ccc76b5a93"
        DQ= "9255f85513cad654c984295c2e86e63d0e6af4af7de0407862a7f4a195bb1547cd0e34d4dbdfefc67db6152b28893bf335ed78deb61399b8b790c8b8763a8f88f3d97559ce559e20454be44aba235324cb981e67bdbd71e6a232f2114e93a06303fbae2e626f89c3bf5daaf913d241df776d98ac5264dca12020edf59fbc46fb"
        DP= "a287fee62f77ebf85c80c7a8d87dbfc6d4a71d1d692c1c5ec53c6c077efae40addaf5bfb87f9cb584152525c20193adac0dbdeb8a46c869dde49ba7294b2e48334a136907ffc2a3e2a03e68d4a2cf82ac09fe41c65c51625dccdd928bcf2d31853fbc069c16f2bef7ddbf70e64f8441b355db5dc50793b848152b5ddda4791b7"
        PQ= "5d6057938fd7f0c1ec2cb7733b019bb755a688fd1e1ff8ee6fbff3107f49f3edecea8d9ec7aaa67807e15229316a094eff5350a06bbdeb7c5fc28860efd0aa8503265821658139fa2a96e2ad081eff5c66a0cbd6c76724fa31687210ef1d9d4189754a50dc5b54553730955384fce1def69c9ebf075329962dd4fc4a01318948"
        D = '8b5c3649023b7aaafca5505af785db2549af0a2de4e3ee1645bc5c719a558c60f0599d26531b47183288f584e2140048e273de9dfde2aae8470f185bddfb45f675ea7965e194fa9b8c48baf0fa8606a218adfa2d0850fa35d2af3ab943bf893589028b557f62250b72ac0c86c5d2bc3c3a4046280b262925ea990b41a80449ea3dbd6a01845b982abe2040bb40d15ac4c2eb5f06e62622ce0b4d44c2d7fe852ce503753666eb9406caa305f6de97d698bf55975d3d871489b4086bf83ee26dbaa217497e774286d8df3e86398b0c67405983e6a24f1e6d19d962f02d0f5ac542d9d8d9f66dbd103a4b35de2fd2983c73b611a333f39c365d332814312519f04b'	
        modulus = 'd10a516d835938007af7f8887348c8b7ee868f44d755e521689a8aaa6780529168866bb97ca8eaa44bcd7047531e006d53adcdecfcd4005c6a96a489ccf8e8f1b0dfb618d25f77e9526d186977c909f32504f7438c797750bc06d815e59f4dd04d83d1003f1337912c0212ca28bc1a5a5760693c10b93db8dfe590e27c066ee12be911db2b6d87b3d637caa06bc1012cf8fc293db3cbbf77ccca7821e30ebdbf57a1890a3027f6b84e81243d3ad7741a112e666ee40acf506ed466b4eeb7d2aa2fdaf01d285e76d2f5d5799a570b0bd7d899ddb9abf16fb98495991aa851d51d4ab86cd5da69a8e44ca74052f11423a5944b6a9ae1b775c43ee99406eeacad7b'
        exponent = '03'

        private, public = build_RSA_keys(modulus, exponent, P, Q, D, DP, DQ, PQ)  
        signature = RSA_signature(Message, private)
        isOK = RSA_verify(Message, signature, public)
        self.assertEqual(isOK, True)
    

    def test_RSA_3(self):
            Message = "0001FFFFFFFFFFFFFFFFFFFFFFFFFFFF"
            
            private_exponent = '8b5c3649023b7aaafca5505af785db2549af0a2de4e3ee1645bc5c719a558c60f0599d26531b47183288f584e2140048e273de9dfde2aae8470f185bddfb45f675ea7965e194fa9b8c48baf0fa8606a218adfa2d0850fa35d2af3ab943bf893589028b557f62250b72ac0c86c5d2bc3c3a4046280b262925ea990b41a80449ea3dbd6a01845b982abe2040bb40d15ac4c2eb5f06e62622ce0b4d44c2d7fe852ce503753666eb9406caa305f6de97d698bf55975d3d871489b4086bf83ee26dbaa217497e774286d8df3e86398b0c67405983e6a24f1e6d19d962f02d0f5ac542d9d8d9f66dbd103a4b35de2fd2983c73b611a333f39c365d332814312519f04b'	
            modulus = 'd10a516d835938007af7f8887348c8b7ee868f44d755e521689a8aaa6780529168866bb97ca8eaa44bcd7047531e006d53adcdecfcd4005c6a96a489ccf8e8f1b0dfb618d25f77e9526d186977c909f32504f7438c797750bc06d815e59f4dd04d83d1003f1337912c0212ca28bc1a5a5760693c10b93db8dfe590e27c066ee12be911db2b6d87b3d637caa06bc1012cf8fc293db3cbbf77ccca7821e30ebdbf57a1890a3027f6b84e81243d3ad7741a112e666ee40acf506ed466b4eeb7d2aa2fdaf01d285e76d2f5d5799a570b0bd7d899ddb9abf16fb98495991aa851d51d4ab86cd5da69a8e44ca74052f11423a5944b6a9ae1b775c43ee99406eeacad7b'
            exponent = '03'

            private, public = build_RSA_SFM_keys(modulus, exponent,private_exponent)
 
            signature = RSA_signature(Message, private)
            isOK = RSA_verify(Message, signature, public)
            self.assertEqual(isOK, True)

    def test_RSA_4(self):
         p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"
         private, public = generate_RSA_keys('03', 2048)   
         input = p
         encrypt_message = public.encrypt(input)
         decrypt_message = private.decrypt(encrypt_message)
         self.assertEqual(input, decrypt_message)


    def test_ECDSA_1(self):
    
        private, public = generate_EC_keys('brainpoolP256r1')  


        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"

        input = p
        signature = ECDSA_signature(input, private)

        isOK = ECDSA_verify(input, signature, public)
        self.assertEqual(isOK, True)
        pass
    
    def test_ECDH_1(self):

        private, public = generate_EC_keys('brainpoolP256r1')  

        secret = generate_ECDH_key_agreement(private, public)

    
    def test_ECDSA_2(self):
    
        private, public = generate_EC_keys('brainpoolP256t1')  


        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"

        input = p
        signature = ECDSA_signature(input, private)
        isOK = ECDSA_verify(input, signature, public)
        self.assertEqual(isOK, True)
        pass
    
    def test_ECDH_2(self):

        private, public = generate_EC_keys('brainpoolP256t1')  

        secret = generate_ECDH_key_agreement(private, public)
    
    def test_ECDSA_3(self):
    
        private, public = generate_EC_keys('brainpoolP384t1')  

        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"

        input = p
        signature = ECDSA_signature(input, private)
        isOK = ECDSA_verify(input, signature, public)
        self.assertEqual(isOK, True)
        pass
    
    def test_ECDH_3(self):

        private, public = generate_EC_keys('brainpoolP384t1')  

        secret = generate_ECDH_key_agreement(private, public)

    
    def test_ECDSA_4(self):
    
        private, public = generate_EC_keys('brainpoolP384r1')  


        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"

        input = p
        signature = ECDSA_signature(input, private)
 
        isOK = ECDSA_verify(input, signature, public)
        self.assertEqual(isOK, True)
        pass
    
    def test_ECDH_5(self):

        private, public = generate_EC_keys('brainpoolP384r1')  

        secret = generate_ECDH_key_agreement(private, public)

    
    def test_ECDSA_5(self):
    
        private, public = generate_EC_keys('brainpoolP512r1')  


        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"

        input = p
        signature = ECDSA_signature(input, private)

        isOK = ECDSA_verify(input, signature, public)
        self.assertEqual(isOK, True)
        pass
    
    def test_ECDH_5(self):

        private, public = generate_EC_keys('brainpoolP512r1')  

        secret = generate_ECDH_key_agreement(private, public)


    def test_ECDSA_6(self):
    
        private, public = generate_EC_keys('brainpoolP512t1')  

        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"

        input = p
        signature = ECDSA_signature(input, private)

        isOK = ECDSA_verify(input, signature, public)
        self.assertEqual(isOK, True)
        pass
    
    def test_ECDSA_7(self):
    
        private, public = generate_EC_keys('nistP256r1')  
        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"

        input = p
        signature = ECDSA_signature(input, private)
        isOK = ECDSA_verify(input, signature, public)
        self.assertEqual(isOK, True)
        pass


    def test_ECDH_6(self):

        private, public = generate_EC_keys('brainpoolP512t1')  

        secret = generate_ECDH_key_agreement(private, public)


    def test_ECDH_7(self):
        
        p = 38272814194707748759055608823005051133324986632225494580586893945708439049218

        EC_P= hex(p).lstrip("0x")
        
        x = 67425968852395269871462349947684551294552401186596675222940579909737866050534
        #coordinate x of base point
        TEST_ECC_KEY_256_1_G_x= hex(x).lstrip("0x")
        #coordinate y of base point
        y = 41855519159243923352127694423822506594545112885193621408050803330913062579667
        TEST_ECC_KEY_256_1_G_y =  hex(y).lstrip("0x")

        private_key, public_key = build_EC_keys(EC_P, TEST_ECC_KEY_256_1_G_x, TEST_ECC_KEY_256_1_G_y, 'brainpoolP256r1')
        secret = generate_ECDH_key_agreement(private_key, public_key)
        input = EC_P
        signature = ECDSA_signature(input, private_key)
        isOK = ECDSA_verify(input, signature, public_key)
        self.assertEqual(isOK, True)

  

    def test_ECDH_8(self):
        

        EC_P= '42A20881C8FE66C4B2FCEF469B80682F2431014D303E872B'
        Gx = 'C0A0647EAAB6A48753B033C56CB0F0900A2F5C4853375FD6'
        Gy = '14B690866ABD5BB88B5F4828C1490002E6773FA2FA299B8F'
        
        privateKeyTerminal='42A20881C8FE66C4B2FCEF469B80682F2431014D303E872B'
        
        terminal_Px = '9402B7E210FDAA55FFCD9E23B670D64735864B4263D0C8A1'   
        terminal_Py ='01ACBFD65055876A5632A2D6488CE7D4132D7D9B2337869B'
        
        
        privateKeyCarte =  '09647B346C04269C58A0AB1A0C89F804619A9C3D9A866323'
        carte_Px = '4465C0B92DF64564DC1A6F1A016BBC52E0871B74291EC890'
        carte_Py = '54B85710C16FAD9C27C987EA3ECF9427C9F407AE68B04F66'  

        private_key, public_key = build_EC_keys(privateKeyCarte, terminal_Px, terminal_Py, 'brainpoolP192r1')

        secret = generate_ECDH_key_agreement(private_key, public_key)

        private_key_2, public_key_2 = build_EC_keys(privateKeyTerminal, carte_Px, carte_Py, 'brainpoolP192r1')

        secret2 = generate_ECDH_key_agreement(private_key_2, public_key_2)
        
        self.assertEqual(secret, secret2)


    def test_DH_1(self):
        p = "E5062379A000F943962BB89D6347257B05813A03D5E7076F27A74908EFFAF20E7EAC5E7EB8E6848F4AD309D5D76AA357476465BA4FF2EBEE93885432BAE83BB83F913B142C759FC7E5328151C399BF90DFFBE77F12F0DB01F23A84189A99B4E1AF76485910247AAC673EFAD73729DD2D7B5A67E44FA49915A54FEC282A363E6B"
        private, public = generate_DH_keys('2', 512)   

        input = p
        secret = generate_DH_key_agreement(private, public)
        

    
    def test_DH_2(self):
        primeModulus= hex(11859949538425015739337467917303613431031019140213666129025407300654026585086345323066284800963463204246390256567934582260424238844463330887962689642467123).lstrip("0x")

        #generator g
        generator = '2'
        # private x
        private = hex(4093640654496734433978333585589265984693478134688160372684518471169824907334504631949214050699990086172315397147035896687401350877308899732826446337707128).lstrip("0x")
        # public y
        public = hex(3215578839553464064873996637315969779839696691982152572238852825117261342483718574508213761865276905503199969908098203345481366464874759377454476688391248).lstrip("0x")
        # parameters = dh.DHParameterNumbers(primeModulus, generator)
        # public = dh.DHPublicNumbers(public_key, parameters)
        # private = dh.DHPrivateNumbers(private, public)
        # key = private.private_key(backend=default_backend())
        private_key, public_key = build_DH_keys(primeModulus, generator, private, public)
        secret = generate_DH_key_agreement(private_key, public_key)



   

        

if __name__ == "__main__":

     unittest.main()
