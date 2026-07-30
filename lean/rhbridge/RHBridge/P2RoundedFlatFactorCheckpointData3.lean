import RHBridge.P2RoundedFactorCheckpointData3
import RHBridge.P2RoundedDirectOuterComponent

namespace RHP2Bridge.P2RoundedFactorCheckpointData

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

def panel3OuterLength (n : Fin 48) : ℕ :=
  match n.val with
  | 0 => 13
  | 1 => 14
  | 2 => 13
  | 3 => 14
  | 4 => 13
  | 5 => 14
  | 6 => 13
  | 7 => 14
  | 8 => 13
  | 9 => 14
  | 10 => 13
  | 11 => 12
  | 12 => 13
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

def panel3OuterLengthTable
    (_k : Fin 32) (n : Fin 48) : ℕ :=
  panel3OuterLength n

def panel3TruncatedEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel3OuterLengthTable .even ⟨3, by decide⟩

def panel3TruncatedOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel3OuterLengthTable .odd ⟨3, by decide⟩

def panel3FlatDefect : RoundedRatPoly.Approx :=
  approxOfScaled [-57903048779329740799552562582160726726205, 1573375996104473704144668560980348636471, -29850032069909139699842107418594199190, -1434089401238113959162888048648130193, 165422136594188114372661322687654125, -6790660394153822851534895254682168, 25808255970359606704472021345915, 14404392012928377787338456432476, -941923821025142658627669367350, 23730122208238285429099298931, 764568028311804612779524953, -102609047137725599110180203, 4478275049352099896700330, -32532023351187776955664, -8546923231641722790242, 599416536424905782817, -16559780537122032841, -397322923532027660, 63271003649594947, -2935819226728410, 30730108811766, 5027850347346, -379892277280, 11410232553, 195826359, -38827577, 1914562, -25831, -2990, 238, -10, -64, -26, 40, 20, -54, -59, -2, -3, -63, -60, -1, -4, -63, -60, -1, -4, -62, -58, -1, -5, -61, -58, -2, -4, -61, -57, 0, -4, -60, -56, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0] 2066

def panel3FlatEven0 : RoundedRatPoly.Approx :=
  approxOfScaled [9304972397318033261438465775853438135237, -7552830659476530634312299189899648813, -288656518832860490855159435598681193, 141092569352722375471153816813295, 2692884269276201293949193007633, -941579108167891276944621815, -11972513109271922285354969, 3258566904439360620674, 31061994025620796116, -6920434729798443, -52757682275805, 9995056579, 64070875, 0] 633794578565493287

def panel3FlatEven1 : RoundedRatPoly.Approx :=
  approxOfScaled [-43950158666762727788085732898613164368, -6746298469419613033334050016920699796, -257126709776248795260882489176141819, 180168277828568956008831689846528, 3434319620236789605295139649346, -1403099739623021053968194201, -17827462703339300916024651, 5297863778078272098788, 50475979889899483874, -11901378943105074, -90696803056774, 17879700764, 114613467, 0] 1167115820232085541

def panel3FlatEven2 : RoundedRatPoly.Approx :=
  approxOfScaled [29590719931966120206976480056603915, 9098298700341048102276796676729108, 1048295491552552011746540378772314, 53565508920355081461062906292344, 1015258634182749383944385958901, -683704374695993682568059633, -8665791693590659899943084, 3278207038913571004804, 31188577233719035174, -8511853058037543, -64803184240719, 14110668112, 90453000, 0] 988965580514625593

def panel3FlatEven3 : RoundedRatPoly.Approx :=
  approxOfScaled [-7859213946518078884202312762654, -3626056183189071356885425779595, -696926793753039570487855813303, -71409388817782302457694190275, -4111666968920662981944167413, -125889829437293969676271017, -1582067997409778122933537, 1048849730493509448426, 9944075418705819109, -3607000262213805, -27405787514629, 7140594727, 45773043, 0] 566002491971731190

def panel3FlatEven4 : RoundedRatPoly.Approx :=
  approxOfScaled [1113604217505285767492428734, 685152469939167635095394097, 184409352791621706799747102, 28358032106096432379844539, 2724790154032106987938199, 167470154886718626171224, 6425074008264986804184, 140327420548199833416, 1315397071456739474, -866468842004514, -6553937482038, 2333023561, 14955278, 0] 225135331472699473

def panel3FlatEven5 : RoundedRatPoly.Approx :=
  approxOfScaled [-98005109989952819878598, -75378184738966968919411, -26087666375572911625939, -5349967357372079309853, -719928524601506731929, -66419025347554513131, -4253946200751723957, -186703290093064409, -5369324362656208, -91084712739787, -679155953418, 450958387, 2890759, 0] 60056324072094376

def panel3FlatEven6 : RoundedRatPoly.Approx :=
  approxOfScaled [5878715461519544138, 5426506579864194591, 2295829706865620789, 588674283811697634, 101885933736639975, 12539807229124916, 1125367315434287, 74200042775882, 3567309748839, 121959307648, 2814445557, 39362871, 252323, 0] 9708547932451947

def panel3FlatEven7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 721331215351873

def panel3FlatEven8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 27554971470

def panel3FlatEven9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 825401

def panel3FlatEven10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 24

def panel3FlatEven11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel3FlatEven12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel3FlatEven13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel3FlatEven14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatEven15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatEven16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatEven17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatEven18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatEven19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 3054

def panel3FlatEven20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 1512097

def panel3FlatEven21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 749705442

def panel3FlatEven22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 371297102844

def panel3FlatEven23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 183701792117465

def panel3FlatEvenComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel3FlatEven0
  | 1 => panel3FlatEven1
  | 2 => panel3FlatEven2
  | 3 => panel3FlatEven3
  | 4 => panel3FlatEven4
  | 5 => panel3FlatEven5
  | 6 => panel3FlatEven6
  | 7 => panel3FlatEven7
  | 8 => panel3FlatEven8
  | 9 => panel3FlatEven9
  | 10 => panel3FlatEven10
  | 11 => panel3FlatEven11
  | 12 => panel3FlatEven12
  | 13 => panel3FlatEven13
  | 14 => panel3FlatEven14
  | 15 => panel3FlatEven15
  | 16 => panel3FlatEven16
  | 17 => panel3FlatEven17
  | 18 => panel3FlatEven18
  | 19 => panel3FlatEven19
  | 20 => panel3FlatEven20
  | 21 => panel3FlatEven21
  | 22 => panel3FlatEven22
  | 23 => panel3FlatEven23
  | _ => panel3FlatEven0

def panel3FlatEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel3FlatEvenComponent

def panel3FlatOdd0 : RoundedRatPoly.Approx :=
  approxOfScaled [-956846551272396869273961542186337460651, -73138140387397756445780249481426305695, 53623844283834635549300341263294948, 1364615277213800401482558553161836, -596429844002478233537294004455, -9100581010191523407905697042, 2889729749544644215786754, 31481241836985800884615, -7890619383201766741, -66839266887243945, 13865141326775, 96070139984, -17094043, -101149, 0] 12359764125846187

def panel3FlatOdd1 : RoundedRatPoly.Approx :=
  approxOfScaled [1321039321684811978402468526018034801, 304498439147264485637793629536554326, 23354383018027709109181836697149582, 591804191892210320730620878477273, -404538719506337041207895266825, -6160984820704169085728402650, 2406377711457361955444880, 26186175964347007827399, -7414545484096297919, -62759312782928556, 14115761640162, 97753171162, -18431707, -109066, 0] 13911526598248663

def panel3FlatOdd2 : RoundedRatPoly.Approx :=
  approxOfScaled [-528695154154037646241610854377374, -203245450259476922972882682509267, -31241928100719154582810074818197, -2399134361505400300757198147690, -91881329089572344397888381297, -1389400607165973932166451698, 926814113746967408206664, 10055701579847655332022, -3714676369606333126, -31387954323010717, 8322292056985, 57565489171, -12160717, -71955, 0] 9965236131923560

def panel3FlatOdd3 : RoundedRatPoly.Approx :=
  approxOfScaled [100043078280233954695195347589, 53855048391791970670117061993, 12423138502600175680906266829, 1591695022299910488390463457, 122301487943679208515211185, 5632082552174669364702039, 143605288116572775330383, 1542657944039157169129, -1018672567105464063, -8573415733489295, 3065510062849, 21155824986, -5409776, -32012, 0] 5059586681576930

def panel3FlatOdd4 : RoundedRatPoly.Approx :=
  approxOfScaled [-11013755336240105431788421, -7623633028404386394070554, -2345194090236943338881114, -420794051661096539658038, -48529242133607406739356, -3730075789048797448968, -191021949619399302610, -6280032210389877698, -119934421966555748, -996570060040778, 655571786859, 4501826248, -1588302, -9395, 0] 1822242655595393

def panel3FlatOdd5 : RoundedRatPoly.Approx :=
  approxOfScaled [793131011571096263389, 671110855944773761330, 258119559978759138970, 59566052302790570529, 9164008046583164693, 986893174247417734, 75914859557493670, 4171146129532616, 160428697289715, 4113556340761, 63285482164, 442555817, 0] 1313608660887506289

def panel3FlatOdd6 : RoundedRatPoly.Approx :=
  approxOfScaled [] 105457431702666837

def panel3FlatOdd7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 4604637466742

def panel3FlatOdd8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 155186097

def panel3FlatOdd9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 4160

def panel3FlatOdd10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel3FlatOdd11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel3FlatOdd12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel3FlatOdd13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel3FlatOdd14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatOdd15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatOdd16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatOdd17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel3FlatOdd18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 138

def panel3FlatOdd19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 67885

def panel3FlatOdd20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 33674224

def panel3FlatOdd21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 16686432761

def panel3FlatOdd22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8259807656904

def panel3FlatOdd23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 4084664607230351

def panel3FlatOddComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel3FlatOdd0
  | 1 => panel3FlatOdd1
  | 2 => panel3FlatOdd2
  | 3 => panel3FlatOdd3
  | 4 => panel3FlatOdd4
  | 5 => panel3FlatOdd5
  | 6 => panel3FlatOdd6
  | 7 => panel3FlatOdd7
  | 8 => panel3FlatOdd8
  | 9 => panel3FlatOdd9
  | 10 => panel3FlatOdd10
  | 11 => panel3FlatOdd11
  | 12 => panel3FlatOdd12
  | 13 => panel3FlatOdd13
  | 14 => panel3FlatOdd14
  | 15 => panel3FlatOdd15
  | 16 => panel3FlatOdd16
  | 17 => panel3FlatOdd17
  | 18 => panel3FlatOdd18
  | 19 => panel3FlatOdd19
  | 20 => panel3FlatOdd20
  | 21 => panel3FlatOdd21
  | 22 => panel3FlatOdd22
  | 23 => panel3FlatOdd23
  | _ => panel3FlatOdd0

def panel3FlatOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel3FlatOddComponent

def panel3FlatCache : PanelCache where
  defect := panel3FlatDefect
  evenComponents := panel3FlatEvenComponents
  oddComponents := panel3FlatOddComponents

end RHP2Bridge.P2RoundedFactorCheckpointData
