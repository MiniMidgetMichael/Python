#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
from alphabet_dict import alphabet, alphabet_items, alphabet_values, alphabet_keys
from collections import OrderedDict

##print (alphabet_keys, alphabet_values)

nums_1 = (23, 5, 12, 12, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 8, 9, 4, 4, 5, 14, 27, 8, 5, 18, 5, 27, 2, 21, 20, 27, 6, 9, 18, 19, 20, 27, 23, 5, 27, 8, 1, 22, 5, 27, 19, 15, 13, 5, 27, 20, 5, 24, 20, 27, 20, 15, 27, 3, 15, 14, 6, 21, 19, 5, 27, 25, 15, 21, 27, 14, 15, 23, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 9, 14, 27, 6, 1, 3, 20, 27, 19, 5, 3, 18, 5, 20, 19, 28, 1, 18, 5, 28, 8, 9, 4, 4, 5, 14, 28, 9, 14, 28, 20, 8, 9, 19, 28, 12, 9, 19, 20, 27, 4, 15, 14, 20, 27, 9, 14, 3, 12, 21, 4, 5, 27, 20, 8, 5, 27, 16, 1, 18, 20, 19, 27, 20, 8, 1, 20, 27, 1, 18, 5, 27, 19, 5, 16, 5, 18, 1, 20, 5, 4, 27, 23, 9, 20, 8, 27, 19, 16, 1, 3, 5, 19)
alphas = []

for i in nums_1:
    alphas += alphabet_keys[alphabet_values.index(i)]
    ##print (i)

##print (alphas)

print (''.join(alphas))

nums_2 = [22,12,200,12,1000,212,12,1000,210,201,12,1000,202,12,200,112,1,200,221,1000,202,120,1000,21,12,202,1000,202,22,12,1000,20,110,1,21,1000,202,22,200,12,12,1001,11,100,21,100,202,201,1001,100,201,112,202,1001,211,12,200,221,1001,201,12,10,210,200,12]

nums_2 = list([str(i) for i in nums_2])

text = ""
for x in nums_2:
    num = int(x, 3)
    ##print(num)
    if num == 27:
        text += " " 
    elif num == 28:
        text += "_"
    else:
        text += chr(num+96)

print(text)

string = """caanqaaeamdwaagarapabseaawaabawaoaalaaaaaxxaapsxeaagragaaadawaoaanaawpqatdaaatakwsaaaayaaaaealabjxaaaeaaauamjawnsaataaaoaaqaxaaaaaeaajrahaaaaaa
            djaaqtewhspaaaaannaoaaaaaboaaaaaaaaaataqadihaaaaqawwaaazoaxaoapabuzwaaaaaaaahlaauakaaiyjavwcaasxaaturabanuataoikpkaoalaaaaaaafgaalwuxzaazaaltaz
            jdaaasalraabaqjmaaadaaaaaaaaiauaqbajaaactaarwrcavmaaxxaqrxaaaaaaaeaaaqaajafaaadaciaaaakadraacafaahlaiaaaakefahalaaparxaaagaacnoraaytaloasaadaaa
            afataaoqarcazjmqeafajgaaaaaaavvaaaaaiaaaaiaaczrbalomaakgilacaayaayaxwaotaarlaxpaaraapaaaswhxxaajeagfaaaaeaaalaaaaeeaatoamayaaauaadaueccvaauvaak
            owasxaaatgnwaawtrxtudppfaaqfypaaaaanraiaaaynagqqaabdaayaaazaesasaaaaaaoaaaaacvawcasaiaaaavxafaqeaaadaciaaanujgxamxiaadazanaamaygabwrfazalaaawkp
            aalsaafiiataatavvaqaqzdatyaaaaanpsaaaajvaydxacyadaolabhocaaawaniniuaaakaaiaaanxaaxaccfaarlaakaabenevaaacaydaaxaaxepasmaasadabanaaafaalaladaagaf
            aaaaaahagnixwemathayfagaxapkaaaafaasaacawaaaaackawamaaaawaatnaaoaaatbaniafawaalkaaumqzaoaauaamazaztamvdaxdaraeasaaaaachoavaaaqaajwaaaaaacarlaxa
            aapaaaaamfaaoeaoaaamapkacamraalbnavaaaxiaqazaamcmanagaicraawaaascbmraaavabaawaagqataazuaaaaakawxwazparaaaaaaaaasaiedhfaaaetaaaapaaapiaaaawembhm
            afalgayaaodamqazqwaasdeaappaacaarahnalaeaaaaanasasbzaaaaoaraeaazhaaevoiaazpypuggeayaapanzakaaaavzaacaaraaaaaaaxsvyacoxvttzgtbcuazxkuaaaiflbjzaa
            ojaboxmaadkaaakzsbxaaaajanaatgaaaazarfaawujasaanxazowlfaayahaaaaaabdoayufltoaiabayaaafawiazaqaasaafchifgpjuvauaaayaaatvaxaaeaaharrazavlayaaaaaa
            agxcfaemvyaaaaaaulxajahazgapaasagswmahaapbaaafnaaywpagqiauaaaavbmgifaweatvaayhaadajaaaaragaminaafixwuaaexaajawzaazlaxastaatmdaaaaairfnraaaaaaax
            aafgaattgakkaacioaabatahfqabmvzfzafifsbbnaaouaahalaahuaawaagataamarjgaaaamianabhaaaaaaiahtpxvaaaaaaahaahtgaaaazvafaaaavzkamalawaaqeaaaavgjkanen
            airaalazaaaayafsazaacodeawvamtdyaaaynaaxaazvssadaqdvstaaolcsecwszzaajahawajooaahgumavaabriwaazgrtaauaxpaaawbhaberaqltaaaaqaaaaxayldaaxgakmwmaax
            xayualfaaijsaaaazxpaaaewcngnaaaypvmayaiaamaasaaakattsadqclclafadaaaadsnwdnaaqasataabasaataaaapajqatuakaygaaoamatgaacaaaaaljwzaaaqajafanaaxaagxq
            aaibgaslawuadeaaxbaweaxxaaaaesnaacatahaitatqsabkaaaaatlajpavaaadlnvzaeaascaaaahqmatanapciszqefcalacjraamhaaaaoanaganaaaaacaqcnaayaawaagazaayyaa
            yjagasarbuafzpmpqeaohaaaglidaanrheaaaabnnaairalrbjuzaakaabgaeaadaaetaauaaaaazaadzxaaaagavazehulaauazvcaajcaaaaqgexaaaaajcirxauaahaoaaahohaanaay
            oaalukbaauaaaaioaaakcobkoaqdvalasraaawuaakaaaaaadamsaaaaaqakaanaxaaaiwaodazaanaaaravbqimznaataaesaavyqjakgabaeaiasamapaaaalwzaikpbclaaaacalakus
            aapaaaaqnaanaaahoaaaecaarwwaaaabxaaaaaepalaaaaaaaxaxgamawmalaaaaanqeaaaaxaomajaaaiavaaqxwaazaaaaaaaaapqpaaaaaastgdydwxaalahaiziaamauayaqaxyryai
            zkaefuaaaaaaaeaaanaaiaaaaayaaaaaaiywaaahaaaaajtawmanmadayaaawaaaaxagaaicaiagaaanaaakaodapaaaaabaaaaaadauevaaywbaaaaaaaaaaygaaawaazimwasraazoagv
            zpaabrnmlhqghhoaaanbaaanaaaaaqxauaaataaaabaahaaaafzaawaapaaaaaarazalqhobgzacazasauaaaaaujafowabywlaagaaadaaatamaaagnpmaeaaaaahmmxapanaraagsxout
            baaaauaqamlazaaaaaaaazaalnsacxltaavaaxpldaqqhapasmalaasutapuasaaatuloaaadaizmaaaaaqqyalyopwakaayhvyaaaczjeauavauxypyenmaaqiaaqiaahuaaakaauja
        """

"""
Find the number of sub-strings with the following properties in the given string:

Length >= 2
Contains only A's
Bound on both sides by either the beginning of the string, the end of the string, or by any character other than a.

For example, lets take the string "aabaaacadaa". It contains three such sub-strings, indexes 0-1, 3-5, and 9-10. The sub-string from indexes 3-4 is not
valid because it is bound on the right side by an "a". The character with index eight[? nine] is not valid either, because although it is an "a" and is
bounded by the correct characters, it only has a length of one.
"""

sub_len = 0
num_subs = 0
last_a = False

for index, i in enumerate(string):
    if i == "a":
        if last_a == True:
            sub_len += 1
        else:
            sub_len = 1
            last_a = True
    else:
        if last_a == True:
            if sub_len >= 2:
                ##print (index, sub_len)
                num_subs += 1
        sub_len = 0

print (num_subs)
