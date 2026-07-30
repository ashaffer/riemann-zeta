import RHBridge.P2RoundedFactorCheckpointData2
import RHBridge.P2RoundedDirectOuterComponent

namespace RHP2Bridge.P2RoundedFactorCheckpointData

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

def panel2OuterLength (n : Fin 48) : ℕ :=
  match n.val with
  | 0 => 13
  | 1 => 14
  | 2 => 13
  | 3 => 14
  | 4 => 13
  | 5 => 14
  | 6 => 13
  | 7 => 12
  | 8 => 13
  | 9 => 12
  | 10 => 13
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

def panel2OuterLengthTable
    (_k : Fin 32) (n : Fin 48) : ℕ :=
  panel2OuterLength n

def panel2TruncatedEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel2OuterLengthTable .even ⟨2, by decide⟩

def panel2TruncatedOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel2OuterLengthTable .odd ⟨2, by decide⟩

def panel2FlatDefect : RoundedRatPoly.Approx :=
  approxOfScaled [-61154864573594906410721851448878878485420, 1669732802372345003114878870965774543081, -16737382597158285740198094198406096652, -3023356854934673366798580963408997944, 229708550446190879208627510312103987, -5430222130298990610276177472471411, -292945675586809185088148033045517, 31504305900875915646032325013128, -1061374793553277429691476763345, -21629683411154592255511538428, 4077526582756813671669004918, -180572547097801739729746251, -278330703419343584971620, 495214363869673931948346, -28160173095465347204174, 329733276426550853387, 55453689665537180878, -4110648406325293550, 92786671818492592, 5488969831113191, -566429729717097, 18494653110506, 423202549828, -73753605386, 3181370673, 9982622, -9021192, 499893, -5309, -1021, 70, -65, -53, 11, 6, -60, -61, -1, -3, -63, -61, -2, -3, -62, -61, -1, -3, -63, -60, -1, -4, -62, -59, -1, -4, -62, -59, 0, -3, -61, -57, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0] 2050

def panel2FlatEven0 : RoundedRatPoly.Approx :=
  approxOfScaled [9318922346936612248865061709111690671956, -6396597718635650962461651729290170297, -289438372575722751656062504186571793, 119513749405381512684044232074987, 2701580831989217672564467690110, -797649160535848208162567346, -12014649629480855848218635, 2760629155953408154772, 31177052781914171208, -5863194936575563, -52960658809440, 8457355567, 64070875, 0] 73228130132824084

def panel2FlatEven1 : RoundedRatPoly.Approx :=
  approxOfScaled [-31487454920379632809264736144595593302, -5715739618031307204273361130211353876, -258125187806416062712830945052117559, 152640452147410424405616227573890, 3447279543048825726701869258550, -1188747803125865424601003293, -17895971793756892201487962, 4488621461703064062293, 50673856592858803470, -10083711067502758, -91059898518410, 15128977568, 114613467, 0] 134847540761959821

def panel2FlatEven2 : RoundedRatPoly.Approx :=
  approxOfScaled [15175045887796015336331935609101553, 5515361533799962913434793735554672, 751321259663750001878928203730322, 45417479978437468777280261480834, 1021574847494777739302903295097, -579453494101152562747263208, -8708187969461980498390585, 2778026379602466913306, 31330108105906237716, -7212844223519492, -65089739347027, 11939796094, 90453000, 0] 114263985944082847

def panel2FlatEven3 : RoundedRatPoly.Approx :=
  approxOfScaled [-2885393225627670949011797518416, -1573455300590544428506468795529, -357459665055767093250783985601, -43297945847227250895650149258, -2947975280777583749997345077, -106821372087308522902611320, -1595635825471921762685485, 889251461854739742089, 10004059318610498833, -3057394141637607, -27550796515196, 6042041691, 45773043, 0] 65395058667333904

def panel2FlatEven4 : RoundedRatPoly.Approx :=
  approxOfScaled [292703609458069762082776080, 212843675053203466858042748, 67708590304925824117422565, 12306726834569712524496935, 1397778018048154950701729, 101565778342808059570173, 4608374804818206404301, 119162599610963916157, 1329810840720764068, -734903148471623, -6601315806682, 1974096859, 14955278, 0] 26011625535357600

def panel2FlatEven5 : RoundedRatPoly.Approx :=
  approxOfScaled [-18442797881583791189477, -16764530357857540657229, -6857317218491888219349, -1662080016393543733640, -264353658207594336792, -28827427018272316966, -2182544001129525745, -113256001412928883, -3852619975214151, -77407470562208, -688313877553, 381580175, 2890759, 0] 6938692353693227

def panel2FlatEven6 : RoundedRatPoly.Approx :=
  approxOfScaled [] 2250886710744814899

def panel2FlatEven7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 83331958464001

def panel2FlatEven8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 2338788930

def panel2FlatEven9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 51477

def panel2FlatEven10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 6

def panel2FlatEven11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel2FlatEven12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel2FlatEven13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel2FlatEven14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatEven15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatEven16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatEven17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatEven18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatEven19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 3054

def panel2FlatEven20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 1512097

def panel2FlatEven21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 749705442

def panel2FlatEven22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 371297102844

def panel2FlatEven23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 183701792117465

def panel2FlatEvenComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel2FlatEven0
  | 1 => panel2FlatEven1
  | 2 => panel2FlatEven2
  | 3 => panel2FlatEven3
  | 4 => panel2FlatEven4
  | 5 => panel2FlatEven5
  | 6 => panel2FlatEven6
  | 7 => panel2FlatEven7
  | 8 => panel2FlatEven8
  | 9 => panel2FlatEven9
  | 10 => panel2FlatEven10
  | 11 => panel2FlatEven11
  | 12 => panel2FlatEven12
  | 13 => panel2FlatEven13
  | 14 => panel2FlatEven14
  | 15 => panel2FlatEven15
  | 16 => panel2FlatEven16
  | 17 => panel2FlatEven17
  | 18 => panel2FlatEven18
  | 19 => panel2FlatEven19
  | 20 => panel2FlatEven20
  | 21 => panel2FlatEven21
  | 22 => panel2FlatEven22
  | 23 => panel2FlatEven23
  | _ => panel2FlatEven0

def panel2FlatEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel2FlatEvenComponent

def panel2FlatOdd0 : RoundedRatPoly.Approx :=
  approxOfScaled [-810366701294161728837685823192781659619, -73336242024038718708820991117943856750, 45422567023142502523359953608922719, 1369022248011928521110754173423908, -505259473431120174558558616374, -9132609942731196899672928764, 2448153575608857885535571, 31597854089822054378243, -6685143797596473654, -67095405354601407, 11747316846650, 96448838799, -14464191, -101149, 0] 1224036734577224

def panel2FlatOdd1 : RoundedRatPoly.Approx :=
  approxOfScaled [800719266609912799171728294866205293, 218195009287813053559787393761487751, 19794342376112494420327079956300600, 594793691912206815908285322266778, -342791828816937734395807944381, -6187658519377987279280772163, 2038983039103185395146048, 26295758316512531446191, -6282466192581735027, -63020091125958424, 11960575441188, 98161504336, -15596061, -109066, 0] 1377712462519526

def panel2FlatOdd2 : RoundedRatPoly.Approx :=
  approxOfScaled [-229404473563882463094072964464952, -104238473151996133996268398925481, -18940906109819343624553473963129, -1719802405652942288556055892287, -77934533801302027979619311578, -1399676096766740327235896106, 785639367692159175947075, 10110608851184549894891, -3148271259017007418, -31541715176854888, 7052805502885, 57834895868, -10289838, -71955, 0] 986893876033235

def panel2FlatOdd3 : RoundedRatPoly.Approx :=
  approxOfScaled [31077565517020930589014144126, 19772873559065096937791408979, 5391064293076773081298018257, 816455242749296372291562817, 74163929233606709772891206, 4038841428115884198618919, 121899757965345697966560, 1557719399505800031861, -863820624405671489, -8629727402195730, 2610912283275, 21577787462, 0] 3425407590794099784

def panel2FlatOdd4 : RoundedRatPoly.Approx :=
  approxOfScaled [-2449470104484109606287917, -2003871945452022505704927, -728560728328701870536468, -154506827491422450584361, -21061676118144555919736, -1913616123962978660345, -115862008502077860141, -4505164516946627523, -101882164566567933, -1008590022235637, 559711395383, 4625714013, 0] 1005729622656616669

def panel2FlatOdd5 : RoundedRatPoly.Approx :=
  approxOfScaled [126266340154412536424, 126266340154412536424, 57393790979278425647, 15652852085257752447, 2845973106410500442, 362214758997700052, 32928614454336367, 2138221717814046, 97191896264271, 2945208977702, 53549254136, 442555817, 0] 177059261837526207

def panel2FlatOdd6 : RoundedRatPoly.Approx :=
  approxOfScaled [] 14213340069088776

def panel2FlatOdd7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 455963041004

def panel2FlatOdd8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 11290167

def panel2FlatOdd9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 228

def panel2FlatOdd10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel2FlatOdd11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel2FlatOdd12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel2FlatOdd13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel2FlatOdd14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatOdd15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatOdd16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatOdd17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel2FlatOdd18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 138

def panel2FlatOdd19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 67885

def panel2FlatOdd20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 33674224

def panel2FlatOdd21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 16686432761

def panel2FlatOdd22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8259807656904

def panel2FlatOdd23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 4084664607230351

def panel2FlatOddComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel2FlatOdd0
  | 1 => panel2FlatOdd1
  | 2 => panel2FlatOdd2
  | 3 => panel2FlatOdd3
  | 4 => panel2FlatOdd4
  | 5 => panel2FlatOdd5
  | 6 => panel2FlatOdd6
  | 7 => panel2FlatOdd7
  | 8 => panel2FlatOdd8
  | 9 => panel2FlatOdd9
  | 10 => panel2FlatOdd10
  | 11 => panel2FlatOdd11
  | 12 => panel2FlatOdd12
  | 13 => panel2FlatOdd13
  | 14 => panel2FlatOdd14
  | 15 => panel2FlatOdd15
  | 16 => panel2FlatOdd16
  | 17 => panel2FlatOdd17
  | 18 => panel2FlatOdd18
  | 19 => panel2FlatOdd19
  | 20 => panel2FlatOdd20
  | 21 => panel2FlatOdd21
  | 22 => panel2FlatOdd22
  | 23 => panel2FlatOdd23
  | _ => panel2FlatOdd0

def panel2FlatOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel2FlatOddComponent

def panel2FlatCache : PanelCache where
  defect := panel2FlatDefect
  evenComponents := panel2FlatEvenComponents
  oddComponents := panel2FlatOddComponents

end RHP2Bridge.P2RoundedFactorCheckpointData
