import RHBridge.P2RoundedFactorCheckpointData1
import RHBridge.P2RoundedDirectOuterComponent

namespace RHP2Bridge.P2RoundedFactorCheckpointData

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

def panel1OuterLength (n : Fin 48) : ℕ :=
  match n.val with
  | 0 => 13
  | 1 => 12
  | 2 => 13
  | 3 => 12
  | 4 => 13
  | 5 => 12
  | 6 => 13
  | 7 => 12
  | 8 => 13
  | 9 => 12
  | 10 => 11
  | 11 => 12
  | 12 => 0
  | 13 => 0
  | 14 => 0
  | 15 => 0
  | 16 => 0
  | 17 => 0
  | 18 => 0
  | 19 => 0
  | 20 => 0
  | 21 => 0
  | 22 => 0
  | 23 => 0
  | 24 => 0
  | 25 => 0
  | 26 => 0
  | 27 => 0
  | 28 => 0
  | 29 => 0
  | 30 => 0
  | 31 => 0
  | 32 => 0
  | 33 => 0
  | 34 => 0
  | 35 => 0
  | 36 => 0
  | 37 => 0
  | 38 => 0
  | 39 => 0
  | 40 => 0
  | 41 => 0
  | 42 => 0
  | 43 => 0
  | 44 => 0
  | 45 => 0
  | 46 => 0
  | 47 => 0
  | _ => 0

def panel1OuterLengthTable
    (_k : Fin 32) (n : Fin 48) : ℕ :=
  panel1OuterLength n

def panel1TruncatedEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel1OuterLengthTable .even ⟨1, by decide⟩

def panel1TruncatedOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel1OuterLengthTable .odd ⟨1, by decide⟩

def panel1FlatDefect : RoundedRatPoly.Approx :=
  approxOfScaled [-64533266787145850690831516534358278809022, 1692688332754395303412826279275267881968, 7256953293286266018989877700396607283, -5012004782371917692677621905392862807, 256573480170650865886882398297907949, 1125378443447049093274854312859386, -822121875415240806246214074970698, 40577722701218453893117401005667, 272223869569236769161605567349, -134949747851037316491122552680, 6400208139641013373741092938, 58593629562908400337439929, -22121345387763505592552377, 1007687178705076440549001, 11818920421861995852767, -3621447314735670652133, 158359439876088056749, 2287766756053990751, -592104574135841057, 24837138214880431, 430374143227618, -96688049830807, 3887272266250, 79279373936, -15769439227, 607034216, 14370393, -2568911, 94504, 2570, -420, -49, -61, -1, -2, -63, -61, -1, -3, -63, -61, -1, -2, -63, -62, -1, -2, -63, -61, -1, -3, -62, -60, -1, -3, -62, -60, 0, -2, -61, -59, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0] 2051

def panel1FlatEven0 : RoundedRatPoly.Approx :=
  approxOfScaled [9330556876023634218743343676286527273402, -5237496575430434323335977999848942310, -290090556205569614822527823718036873, 97871120617039396350618113246045, 2708835706581871013695024619261, -653255450845506816904300624, -12049802845754690045571604, 2261002896635396726451, 31273046715918816482, -4802233906902705, -53129805920802, 6919654555, 64070875, 0] 5703315114884625

def panel1FlatEven1 : RoundedRatPoly.Approx :=
  approxOfScaled [-21089642365793147214495928882513961021, -4681517585987090266801119218247005905, -258958205008401834529181731757433866, 125017531669149441892562670098473, 3458092062752602128023602121564, -973641818879772037425000276, -17953130552206645594796533, 3676475196302418351178, 50838953547828803195, -8259386441770442, -91362478069774, 12378254374, 114613467, 0] 10502487110604368

def panel1FlatEven2 : RoundedRatPoly.Approx :=
  approxOfScaled [6802631201423724159290184704877502, 3022351176671399190444085610778361, 503378440636757589543415911107684, 37223097868303757550823471172138, 1026846148428163224962346728296, -474735934156020065933668723, -8743566738509928454293845, 2275768547239235984566, 31448208104704042860, -5908581878719117, -65328535268950, 9768924077, 90453000, 0] 8899338996364862

def panel1FlatEven3 : RoundedRatPoly.Approx :=
  approxOfScaled [-865789270431920898340807896392, -577095741104219399530275187895, -160261219178131324724305388858, -23731216714892195236509429425, -1975737483338815251663843664, -87603532818787356757714900, -1606962929382635563466900, 728772727507138654485, 10054125656814710571, -2505129522717676, -27671637349000, 4943488658, 45773043, 0] 5093214402059182

def panel1FlatEven4 : RoundedRatPoly.Approx :=
  approxOfScaled [58791173252449115227479990, 52253615034623876705558620, 20317958480814966650535951, 4514138040520036356737012, 626749457486023575890362, 55677755520784985232461, 3089508870619447047419, 97786147413431016160, 1341848373186006764, -602468852320216, -6640797743888, 1615170157, 14955278, 0] 2025872869298503

def panel1FlatEven5 : RoundedRatPoly.Approx :=
  approxOfScaled [-2480496602698763707233, -2756107336331959674702, -1378053668165979837351, -408312197975105136993, -79394038495159332193, -10585871799354577623, -980173314755053483, -62233226333654187, -2593051097235591, -64025953018163, -711399477978, 0] 2891299284510911226

def panel1FlatEven6 : RoundedRatPoly.Approx :=
  approxOfScaled [] 252413478052624081

def panel1FlatEven7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 6489579167848

def panel1FlatEven8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 126485306

def panel1FlatEven9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 1935

def panel1FlatEven10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 6

def panel1FlatEven11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel1FlatEven12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel1FlatEven13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel1FlatEven14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatEven15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatEven16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatEven17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatEven18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatEven19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 3054

def panel1FlatEven20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 1512097

def panel1FlatEven21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 749705442

def panel1FlatEven22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 371297102844

def panel1FlatEven23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 183701792117465

def panel1FlatEvenComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel1FlatEven0
  | 1 => panel1FlatEven1
  | 2 => panel1FlatEven2
  | 3 => panel1FlatEven3
  | 4 => panel1FlatEven4
  | 5 => panel1FlatEven5
  | 6 => panel1FlatEven6
  | 7 => panel1FlatEven7
  | 8 => panel1FlatEven8
  | 9 => panel1FlatEven9
  | 10 => panel1FlatEven10
  | 11 => panel1FlatEven11
  | 12 => panel1FlatEven12
  | 13 => panel1FlatEven13
  | 14 => panel1FlatEven14
  | 15 => panel1FlatEven15
  | 16 => panel1FlatEven16
  | 17 => panel1FlatEven17
  | 18 => panel1FlatEven18
  | 19 => panel1FlatEven19
  | 20 => panel1FlatEven20
  | 21 => panel1FlatEven21
  | 22 => panel1FlatEven22
  | 23 => panel1FlatEven23
  | _ => panel1FlatEven0

def panel1FlatEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel1FlatEvenComponent

def panel1FlatOdd0 : RoundedRatPoly.Approx :=
  approxOfScaled [-663523486947731237941903337495880047946, -73501488587916674155884179061490452583, 37197038482815432984160889546986604, 1372698645403513424804272869271059, -413795339405067376419175350888, -9159330706301147420287068806, 2005080009232849762965122, 31695143976636071942905, -5475431720175122642, -67308634149377488, 9642944064011, 97403475395, 0] 1011561321818322507

def panel1FlatOdd1 : RoundedRatPoly.Approx :=
  approxOfScaled [438742981466378045980340692994811455, 146165638032452194043277249997350290, 16217848705103409673442477033348745, 597288208701224911630664509010642, -280800274235218609240783014490, -6209914784739791747878218156, 1670181175590238496527183, 26387192018455929577345, -5146073052564889905, -63237169273744331, 9819893576788, 99190844209, 0] 1090722893102638675

def panel1FlatOdd2 : RoundedRatPoly.Approx :=
  approxOfScaled [-84134846373696346777664252209089, -46730692896708186460776997408823, -10380364645768603339408788395913, -1152433213998970054668917043976, -63893468840826763381863008275, -1408253131249296739533687835, 643759456859558888653693, 10156432784892513739560, -2579321832995332397, -31669692764722059, 5792888499114, 58514025245, 0] 719633218217385862

def panel1FlatOdd3 : RoundedRatPoly.Approx :=
  approxOfScaled [7629415550951072469508790677, 5933234847941351965716055743, 1977367470242195229462019098, 366067329128298252226850330, 40652406348647752301597192, 2707262335783129307359637, 100000746092804599768998, 1570295456205300460864, -708044049634612501, -8677198534618944, 2136200959043, 21577787462, 0] 320137569785485704

def panel1FlatOdd4 : RoundedRatPoly.Approx :=
  approxOfScaled [-402529681245320514828502, -402497423510403441028280, -178868030722174428690208, -46365892016775925713871, -7725823386108293113822, -858100325860146137654, -63520922957605793890, -3020799746253059531, -83632902057652632, -1018766593060780, 457945687135, 4625714013, 0] 93994237603702333

def panel1FlatOdd5 : RoundedRatPoly.Approx :=
  approxOfScaled [13887870547007071829, 16974064001897532234, 9430035556609740130, 3143345185536580040, 698521152341462227, 108658845919783010, 12073205102198109, 958190881126830, 53232826729268, 1971586175157, 43813026113, 442555817, 0] 16547385182330786

def panel1FlatOdd6 : RoundedRatPoly.Approx :=
  approxOfScaled [] 1328245540427482

def panel1FlatOdd7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 29590808606

def panel1FlatOdd8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 508828

def panel1FlatOdd9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 12

def panel1FlatOdd10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel1FlatOdd11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel1FlatOdd12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel1FlatOdd13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel1FlatOdd14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatOdd15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatOdd16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatOdd17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel1FlatOdd18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 138

def panel1FlatOdd19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 67885

def panel1FlatOdd20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 33674224

def panel1FlatOdd21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 16686432761

def panel1FlatOdd22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8259807656904

def panel1FlatOdd23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 4084664607230351

def panel1FlatOddComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel1FlatOdd0
  | 1 => panel1FlatOdd1
  | 2 => panel1FlatOdd2
  | 3 => panel1FlatOdd3
  | 4 => panel1FlatOdd4
  | 5 => panel1FlatOdd5
  | 6 => panel1FlatOdd6
  | 7 => panel1FlatOdd7
  | 8 => panel1FlatOdd8
  | 9 => panel1FlatOdd9
  | 10 => panel1FlatOdd10
  | 11 => panel1FlatOdd11
  | 12 => panel1FlatOdd12
  | 13 => panel1FlatOdd13
  | 14 => panel1FlatOdd14
  | 15 => panel1FlatOdd15
  | 16 => panel1FlatOdd16
  | 17 => panel1FlatOdd17
  | 18 => panel1FlatOdd18
  | 19 => panel1FlatOdd19
  | 20 => panel1FlatOdd20
  | 21 => panel1FlatOdd21
  | 22 => panel1FlatOdd22
  | 23 => panel1FlatOdd23
  | _ => panel1FlatOdd0

def panel1FlatOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel1FlatOddComponent

def panel1FlatCache : PanelCache where
  defect := panel1FlatDefect
  evenComponents := panel1FlatEvenComponents
  oddComponents := panel1FlatOddComponents

end RHP2Bridge.P2RoundedFactorCheckpointData
