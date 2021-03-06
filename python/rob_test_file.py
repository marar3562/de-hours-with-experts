from next_biggest_number import next_biggest_number

def test_simple_cases():
    assert(next_biggest_number(12) == 21)
    assert(next_biggest_number(123) == 132)
    assert(next_biggest_number(67809) == 67890)

test_simple_cases()

def test_cases_full():
    assert(next_biggest_number(12) == 21)
    assert(next_biggest_number(123) == 132)
    assert(next_biggest_number(67809) == 67890)
    assert(next_biggest_number(21) == -1)
    assert(next_biggest_number(54321) == -1)
    assert(next_biggest_number(52210) == -1)
    assert(next_biggest_number(95701) == 95710)
    assert(next_biggest_number(71305) == 71350)
    assert(next_biggest_number(6358) == 6385)
    assert(next_biggest_number(25437) == 25473)
    assert(next_biggest_number(49893) == 49938)
    assert(next_biggest_number(76778) == 76787)
    assert(next_biggest_number(2372) == 2723)
    assert(next_biggest_number(45071) == 45107)
    assert(next_biggest_number(31233) == 31323)
    assert(next_biggest_number(50401) == 50410)
    assert(next_biggest_number(57067) == 57076)
    assert(next_biggest_number(40272) == 40722)
    assert(next_biggest_number(54998) == 58499)
    assert(next_biggest_number(22437) == 22473)
    assert(next_biggest_number(53510) == 55013)
    assert(next_biggest_number(78263) == 78326)
    assert(next_biggest_number(42661) == 46126)
    assert(next_biggest_number(45118) == 45181)
    assert(next_biggest_number(26075) == 26507)
    assert(next_biggest_number(93932) == 99233)
    assert(next_biggest_number(84252) == 84522)
    assert(next_biggest_number(33203) == 33230)
    assert(next_biggest_number(98037) == 98073)
    assert(next_biggest_number(74041) == 74104)
    assert(next_biggest_number(11856) == 11865)
    assert(next_biggest_number(47998) == 48799)
    assert(next_biggest_number(36708) == 36780)
    assert(next_biggest_number(93802) == 93820)
    assert(next_biggest_number(2902) == 2920)
    assert(next_biggest_number(71116) == 71161)
    assert(next_biggest_number(76532) == -1)
    assert(next_biggest_number(81848) == 81884)
    assert(next_biggest_number(93493) == 93934)
    assert(next_biggest_number(16332) == 21336)
    assert(next_biggest_number(97939) == 97993)
    assert(next_biggest_number(4386) == 4638)
    assert(next_biggest_number(6950) == 9056)
    assert(next_biggest_number(92232) == 92322)
    assert(next_biggest_number(39527) == 39572)
    assert(next_biggest_number(41766) == 46167)
    assert(next_biggest_number(3399) == 3939)
    assert(next_biggest_number(77957) == 77975)
    assert(next_biggest_number(81899) == 81989)
    assert(next_biggest_number(2403) == 2430)
    assert(next_biggest_number(23817) == 23871)
    assert(next_biggest_number(85520) == -1)
    assert(next_biggest_number(42882) == 48228)
    assert(next_biggest_number(56072) == 56207)
    assert(next_biggest_number(89101) == 89110)
    assert(next_biggest_number(25384) == 25438)
    assert(next_biggest_number(54443) == -1)
    assert(next_biggest_number(49459) == 49495)
    assert(next_biggest_number(84803) == 84830)
    assert(next_biggest_number(50766) == 56067)
    assert(next_biggest_number(43770) == 47037)
    assert(next_biggest_number(33285) == 33528)
    assert(next_biggest_number(42083) == 42308)
    assert(next_biggest_number(47482) == 47824)
    assert(next_biggest_number(45634) == 45643)
    assert(next_biggest_number(73784) == 73847)
    assert(next_biggest_number(97071) == 97107)
    assert(next_biggest_number(81003) == 81030)
    assert(next_biggest_number(32619) == 32691)
    assert(next_biggest_number(36448) == 36484)
    assert(next_biggest_number(22368) == 22386)
    assert(next_biggest_number(22794) == 22947)
    assert(next_biggest_number(58927) == 58972)
    assert(next_biggest_number(73399) == 73939)
    assert(next_biggest_number(81830) == 83018)
    assert(next_biggest_number(49685) == 49856)
    assert(next_biggest_number(73251) == 73512)
    assert(next_biggest_number(44595) == 44955)
    assert(next_biggest_number(81165) == 81516)
    assert(next_biggest_number(85034) == 85043)
    assert(next_biggest_number(31814) == 31841)
    assert(next_biggest_number(79768) == 79786)
    assert(next_biggest_number(88439) == 88493)
    assert(next_biggest_number(44697) == 44769)
    assert(next_biggest_number(52821) == 58122)
    assert(next_biggest_number(80263) == 80326)
    assert(next_biggest_number(71049) == 71094)
    assert(next_biggest_number(91362) == 91623)
    assert(next_biggest_number(17056) == 17065)
    assert(next_biggest_number(26130) == 26301)
    assert(next_biggest_number(83800) == 88003)
    assert(next_biggest_number(52246) == 52264)
    assert(next_biggest_number(56996) == 59669)
    assert(next_biggest_number(30281) == 30812)
    assert(next_biggest_number(51428) == 51482)
    assert(next_biggest_number(7654) == -1)
    assert(next_biggest_number(33095) == 33509)
    assert(next_biggest_number(50933) == 53039)
    assert(next_biggest_number(7558) == 7585)
    assert(next_biggest_number(75659) == 75695)
    assert(next_biggest_number(36639) == 36693)
    assert(next_biggest_number(75517) == 75571)
    assert(next_biggest_number(64149) == 64194)
    assert(next_biggest_number(44926) == 44962)
    assert(next_biggest_number(16230) == 16302)
    assert(next_biggest_number(36166) == 36616)
    assert(next_biggest_number(14134) == 14143)
    assert(next_biggest_number(66848) == 66884)
    assert(next_biggest_number(85420) == -1)
    assert(next_biggest_number(6447) == 6474)
    assert(next_biggest_number(70690) == 70906)
    assert(next_biggest_number(55511) == -1)
    assert(next_biggest_number(55224) == 55242)
    assert(next_biggest_number(73239) == 73293)
    assert(next_biggest_number(21166) == 21616)
    assert(next_biggest_number(69958) == 69985)
    assert(next_biggest_number(59609) == 59690)
    assert(next_biggest_number(28850) == 50288)
    assert(next_biggest_number(34085) == 34508)
    assert(next_biggest_number(68686) == 68866)
    assert(next_biggest_number(30015) == 30051)
    assert(next_biggest_number(95116) == 95161)
    assert(next_biggest_number(68150) == 68501)
    assert(next_biggest_number(80403) == 80430)
    assert(next_biggest_number(32154) == 32415)
    assert(next_biggest_number(34731) == 37134)
    assert(next_biggest_number(18099) == 18909)
    assert(next_biggest_number(13447) == 13474)
    assert(next_biggest_number(56296) == 56629)
    assert(next_biggest_number(1276) == 1627)
    assert(next_biggest_number(44944) == 49444)
    assert(next_biggest_number(75519) == 75591)
    assert(next_biggest_number(45632) == 46235)
    assert(next_biggest_number(27590) == 27905)
    assert(next_biggest_number(7251) == 7512)
    assert(next_biggest_number(90251) == 90512)
    assert(next_biggest_number(98728) == 98782)
    assert(next_biggest_number(51811) == 58111)
    assert(next_biggest_number(59358) == 59385)
    assert(next_biggest_number(24098) == 24809)
    assert(next_biggest_number(59176) == 59617)
    assert(next_biggest_number(54917) == 54971)
    assert(next_biggest_number(8165) == 8516)
    assert(next_biggest_number(34178) == 34187)
    assert(next_biggest_number(71652) == 72156)
    assert(next_biggest_number(26168) == 26186)
    assert(next_biggest_number(49396) == 49639)
    assert(next_biggest_number(78946) == 78964)
    assert(next_biggest_number(33316) == 33361)
    assert(next_biggest_number(15484) == 15844)
    assert(next_biggest_number(2211) == -1)
    assert(next_biggest_number(97203) == 97230)
    assert(next_biggest_number(70956) == 70965)


test_cases_full()