import RHBridge.P2RoundedFactorCheckpointData4
import RHBridge.P2RoundedDirectOuterComponent

namespace RHP2Bridge.P2RoundedFactorCheckpointData

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

def panel4OuterLength (n : Fin 48) : ℕ :=
  match n.val with
  | 0 => 15
  | 1 => 14
  | 2 => 15
  | 3 => 14
  | 4 => 15
  | 5 => 14
  | 6 => 15
  | 7 => 14
  | 8 => 13
  | 9 => 14
  | 10 => 13
  | 11 => 14
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

def panel4OuterLengthTable
    (_k : Fin 32) (n : Fin 48) : ℕ :=
  panel4OuterLength n

def panel4TruncatedEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel4OuterLengthTable .even ⟨4, by decide⟩

def panel4TruncatedOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  componentVectorFromTruncatedOuters
    P2RoundedCanonical.gridCells sphericalOuters
    panel4OuterLengthTable .odd ⟨4, by decide⟩

def panel4FlatDefect : RoundedRatPoly.Approx :=
  approxOfScaled [-54884736910458827296849115476296745719344, 1441527551912722344479354559570342619258, -35013388663716227441512093654595976578, -371695398987598137738290062909100171, 102144472900024031593692567760738190, -5641566607234336504642962963722131, 139225400183219908013223737147273, 3050014081461164390043078462871, -479681203872545309265355317652, 23576136208928028225567283311, -473183358724413190813213339, -19502283490120103607815540, 2200106941259063106434895, -96675526828821899277261, 1455631900789317529760, 110200769212163438095, -9899490624058889024, 388324219418974071, -3638744192693274, -580378157278876, 43763178608754, -1522904783749, 3999927031, 2916646449, -190227343, 5800772, 33686, -14224, 752, -23, -4, -62, -3, 57, 25, -55, -59, -1, -4, -63, -60, -1, -6, -62, -58, -2, -4, -61, -58, -2, -5, -61, -57, -1, -5, -60, -56, 0, -4, -59, -55, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0] 2038

def panel4FlatEven0 : RoundedRatPoly.Approx :=
  approxOfScaled [9288713281719555541147451211194815499786, -8705677529302682633510863806075927769, -287745412391767940544949409729771781, 162596066620930152701187942349843, 2682751074567487872974056643103, -1084961644466979471323971452, -11923419057364214296992369, 3754511639829593005093, 30927941567846222015, -7973363397884910, -52523766311864, 11462697180, 62903201, -11978, -58, 0] 723044898477286

def panel4FlatEven1 : RoundedRatPoly.Approx :=
  approxOfScaled [-58469766195409854937303660971300287434, -7772533506631244718891272146229586388, -255963392961311356928390530677240395, 207583861464036784610735626259806, 3419220514964049201199194588230, -1616561682998844622985789060, -17747647603703585598561665, 6103678624546364990560, 50245450561083812371, -13711339405181761, -90278513511859, 20501409969, 112463234, -22053, -105, 0] 1361500280924702

def panel4FlatEven2 : RoundedRatPoly.Approx :=
  approxOfScaled [52425245075645118193317835556875157, 13966698691207935747161552776395633, 1393997978413890385619632000052611, 61658845183797099805532967829989, 1007902595728109900679619775118, -787404550834103148119518585, -8616409612570560690094737, 3775936381371707970850, 31023715604094430002, -9804788482420080, -64473379411174, 16172219859, 88630993, -18690, -90, 0] 1217770412696928

def panel4FlatEven3 : RoundedRatPoly.Approx :=
  approxOfScaled [-18540224860052109300096664369519, -7412623830372990575204403137901, -1234513293958926989586438692704, -109590843470564929835418738895, -5465184542790030676832851033, -144782094579478900772529724, -1566272881007283096009788, 1207409228597800932817, 9874224418295154033, -4153541945365335, -27239191155776, 8176582708, 44730294, -10695, -51, 0] 763614177019509

def panel4FlatEven4 : RoundedRatPoly.Approx :=
  approxOfScaled [3497796015757439013626069507, 1864974989529496482085172482, 434988792427929321412509363, 57964107163498730740340724, 4825757484281871286989247, 256946044618321483966738, 8536378115026988361806, 161242723095667267514, 1298624121590805690, -997008005170063, -6498662769948, 2691950260, 14955278, 0] 1460008115283089601

def panel4FlatEven5 : RoundedRatPoly.Approx :=
  approxOfScaled [-409853721488810969152103, -273185805608735522873832, -81935738195765274237788, -14561463715793621889650, -1698022476637369928354, -135744003306363279214, -7532640643720065283, -286378213921708978, -7130479103709000, -104563533227771, -668471708595, 520336599, 2890759, 0] 389471849789405237

def panel4FlatEven6 : RoundedRatPoly.Approx :=
  approxOfScaled [32738390242087514451, 26190712193670011562, 9603261137679004235, 2134058030595334274, 320108704589300140, 34144928489525346, 2655716660296411, 151755237731220, 6323134905467, 187352145345, 3747042903, 45418697, 252323, 0] 62962726969313191

def panel4FlatEven7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 4678434361722520

def panel4FlatEven8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 233421414515

def panel4FlatEven9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 9132312

def panel4FlatEven10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 294

def panel4FlatEven11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel4FlatEven12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel4FlatEven13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel4FlatEven14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatEven15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatEven16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatEven17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatEven18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatEven19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 3054

def panel4FlatEven20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 1512097

def panel4FlatEven21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 749705442

def panel4FlatEven22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 371297102844

def panel4FlatEven23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 183701792117465

def panel4FlatEvenComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel4FlatEven0
  | 1 => panel4FlatEven1
  | 2 => panel4FlatEven2
  | 3 => panel4FlatEven3
  | 4 => panel4FlatEven4
  | 5 => panel4FlatEven5
  | 6 => panel4FlatEven6
  | 7 => panel4FlatEven7
  | 8 => panel4FlatEven8
  | 9 => panel4FlatEven9
  | 10 => panel4FlatEven10
  | 11 => panel4FlatEven11
  | 12 => panel4FlatEven12
  | 13 => panel4FlatEven13
  | 14 => panel4FlatEven14
  | 15 => panel4FlatEven15
  | 16 => panel4FlatEven16
  | 17 => panel4FlatEven17
  | 18 => panel4FlatEven18
  | 19 => panel4FlatEven19
  | 20 => panel4FlatEven20
  | 21 => panel4FlatEven21
  | 22 => panel4FlatEven22
  | 23 => panel4FlatEven23
  | _ => panel4FlatEven0

def panel4FlatEvenComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel4FlatEvenComponent

def panel4FlatOdd0 : RoundedRatPoly.Approx :=
  approxOfScaled [-1102897429581746459337173345713476082933, -72907289440168417719054909986030216899, 61796494299056649741041312852287120, 1359480295193129169724202001469923, -687253464678505662915543212530, -9063263498513479253810373039, 3329538517910321319476449, 31345380889764482362182, -9091103788699073439, -66540859872564320, 15973940151813, 95628324700, -19723897, -101149, 0] 91602095934871612

def panel4FlatOdd1 : RoundedRatPoly.Approx :=
  approxOfScaled [2028181495972921178569508199937457964, 405004183878020177217624836954394746, 26895006956441347713802008759594283, 588321842414399792221828899818171, -465996861478563921959480409988, -6129912097508109075965651685, 2772111620478839212217667, 26058519962349532729396, -8541543393378620147, -62455525539955971, 16261215898519, 97276782462, -21267355, -109066, 0] 103102824645116609

def panel4FlatOdd2 : RoundedRatPoly.Approx :=
  approxOfScaled [-1080861343450507718717817451053307, -360053947130469893850009932909374, -47952809030457047892513223867562, -3189607103882845219948318020870, -105716915004844392516879746318, -1377435886252620816028470748, 1067156828219348172227892, 9991755185541494123336, -4278085647680932142, -31208866300306062, 9585357751509, 57251181360, -14031597, -71955, 0] 73855772955441944

def panel4FlatOdd3 : RoundedRatPoly.Approx :=
  approxOfScaled [272325727634876053444298834246, 127040419151382694001490629820, 25394611021576655044804969677, 2819229090979700504818898351, 187669399537557217187969069, 7484455652901899520729821, 165082657282786843225512, 1525127665551642700137, -1172414376971713123, -8507461138139304, 3529436791902, 21016003100, -6242052, -32012, 0] 37498485699181067

def panel4FlatOdd4 : RoundedRatPoly.Approx :=
  approxOfScaled [-39917040928346650890571423, -23944894594980153870491508, -6383351231088193134357886, -992531620054078630875851, -99188061742415886480121, -6605596176959622760873, -293042481725246463134, -8341835973228824749, -137748750681440628, -982471125461602, 754171148651, 4460774682, -1832659, -9395, 0] 13505415963532763

def panel4FlatOdd5 : RoundedRatPoly.Approx :=
  approxOfScaled [3824779904829201952704, 2804409278660834576046, 934617054994248998885, 186873800894130903829, 24907411600018989586, 2323479057886421567, 154777334714226355, 7361109718211277, 244831349963181, 5416742266860, 71424750258, 413520181, -322622, -1656, 0] 3302218404090636

def panel4FlatOdd6 : RoundedRatPoly.Approx :=
  approxOfScaled [] 598489416366849970

def panel4FlatOdd7 : RoundedRatPoly.Approx :=
  approxOfScaled [] 34130955252676

def panel4FlatOdd8 : RoundedRatPoly.Approx :=
  approxOfScaled [] 1502386665

def panel4FlatOdd9 : RoundedRatPoly.Approx :=
  approxOfScaled [] 52593

def panel4FlatOdd10 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel4FlatOdd11 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel4FlatOdd12 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel4FlatOdd13 : RoundedRatPoly.Approx :=
  approxOfScaled [] 7

def panel4FlatOdd14 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatOdd15 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatOdd16 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatOdd17 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8

def panel4FlatOdd18 : RoundedRatPoly.Approx :=
  approxOfScaled [] 138

def panel4FlatOdd19 : RoundedRatPoly.Approx :=
  approxOfScaled [] 67885

def panel4FlatOdd20 : RoundedRatPoly.Approx :=
  approxOfScaled [] 33674224

def panel4FlatOdd21 : RoundedRatPoly.Approx :=
  approxOfScaled [] 16686432761

def panel4FlatOdd22 : RoundedRatPoly.Approx :=
  approxOfScaled [] 8259807656904

def panel4FlatOdd23 : RoundedRatPoly.Approx :=
  approxOfScaled [] 4084664607230351

def panel4FlatOddComponent
    (i : Fin 24) : RoundedRatPoly.Approx :=
  match i.val with
  | 0 => panel4FlatOdd0
  | 1 => panel4FlatOdd1
  | 2 => panel4FlatOdd2
  | 3 => panel4FlatOdd3
  | 4 => panel4FlatOdd4
  | 5 => panel4FlatOdd5
  | 6 => panel4FlatOdd6
  | 7 => panel4FlatOdd7
  | 8 => panel4FlatOdd8
  | 9 => panel4FlatOdd9
  | 10 => panel4FlatOdd10
  | 11 => panel4FlatOdd11
  | 12 => panel4FlatOdd12
  | 13 => panel4FlatOdd13
  | 14 => panel4FlatOdd14
  | 15 => panel4FlatOdd15
  | 16 => panel4FlatOdd16
  | 17 => panel4FlatOdd17
  | 18 => panel4FlatOdd18
  | 19 => panel4FlatOdd19
  | 20 => panel4FlatOdd20
  | 21 => panel4FlatOdd21
  | 22 => panel4FlatOdd22
  | 23 => panel4FlatOdd23
  | _ => panel4FlatOdd0

def panel4FlatOddComponents :
    Vector RoundedRatPoly.Approx 24 :=
  Vector.ofFn panel4FlatOddComponent

def panel4FlatCache : PanelCache where
  defect := panel4FlatDefect
  evenComponents := panel4FlatEvenComponents
  oddComponents := panel4FlatOddComponents

end RHP2Bridge.P2RoundedFactorCheckpointData
