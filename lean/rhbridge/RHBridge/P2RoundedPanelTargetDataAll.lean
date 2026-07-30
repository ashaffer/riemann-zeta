import RHBridge.P2RoundedPanelTargetData0
import RHBridge.P2RoundedPanelTargetData1
import RHBridge.P2RoundedPanelTargetData2
import RHBridge.P2RoundedPanelTargetData3
import RHBridge.P2RoundedPanelTargetData4
import RHBridge.P2RoundedPanelTargetData5
import RHBridge.P2RoundedPanelTargetData6
import RHBridge.P2RoundedPanelTargetData7
import RHBridge.P2RoundedPanelTargetData8
import RHBridge.P2RoundedPanelTargetData9
import RHBridge.P2RoundedPanelTargetData10
import RHBridge.P2RoundedPanelTargetData11
import RHBridge.P2RoundedPanelTargetData12
import RHBridge.P2RoundedPanelTargetData13
import RHBridge.P2RoundedPanelTargetData14
import RHBridge.P2RoundedPanelTargetData15
import RHBridge.P2RoundedPanelTargetData16
import RHBridge.P2RoundedPanelTargetData17
import RHBridge.P2RoundedPanelTargetData18
import RHBridge.P2RoundedPanelTargetData19
import RHBridge.P2RoundedPanelTargetData20
import RHBridge.P2RoundedPanelTargetData21
import RHBridge.P2RoundedPanelTargetData22
import RHBridge.P2RoundedPanelTargetData23
import RHBridge.P2RoundedPanelTargetData24
import RHBridge.P2RoundedPanelTargetData25
import RHBridge.P2RoundedPanelTargetData26
import RHBridge.P2RoundedPanelTargetData27
import RHBridge.P2RoundedPanelTargetData28
import RHBridge.P2RoundedPanelTargetData29
import RHBridge.P2RoundedPanelTargetData30
import RHBridge.P2RoundedPanelTargetData31
import RHBridge.P2PanelCertificateAggregate

namespace RHP2Bridge.P2RoundedPanelTargetData

open P2PanelCertificateAggregate

/-- Panels `0` through `30` retain their independently rounded numerical
centers.  Panel `31` is stored as the exact residual against the published
band target, making the 32-panel center identity algebraic by construction.
Its separate analytic refinement check validates this residual center. -/
def first31PanelTargetSumQ (r : Fin 600) : ℚ :=
  panel0TargetQ r + panel1TargetQ r + panel2TargetQ r +
    panel3TargetQ r + panel4TargetQ r + panel5TargetQ r +
    panel6TargetQ r + panel7TargetQ r + panel8TargetQ r +
    panel9TargetQ r + panel10TargetQ r + panel11TargetQ r +
    panel12TargetQ r + panel13TargetQ r + panel14TargetQ r +
    panel15TargetQ r + panel16TargetQ r + panel17TargetQ r +
    panel18TargetQ r + panel19TargetQ r + panel20TargetQ r +
    panel21TargetQ r + panel22TargetQ r + panel23TargetQ r +
    panel24TargetQ r + panel25TargetQ r + panel26TargetQ r +
    panel27TargetQ r + panel28TargetQ r + panel29TargetQ r +
    panel30TargetQ r

def panelTargetQ (k : Fin 32) (r : Fin 600) : ℚ :=
  match k.val with
  | 0 => panel0TargetQ r
  | 1 => panel1TargetQ r
  | 2 => panel2TargetQ r
  | 3 => panel3TargetQ r
  | 4 => panel4TargetQ r
  | 5 => panel5TargetQ r
  | 6 => panel6TargetQ r
  | 7 => panel7TargetQ r
  | 8 => panel8TargetQ r
  | 9 => panel9TargetQ r
  | 10 => panel10TargetQ r
  | 11 => panel11TargetQ r
  | 12 => panel12TargetQ r
  | 13 => panel13TargetQ r
  | 14 => panel14TargetQ r
  | 15 => panel15TargetQ r
  | 16 => panel16TargetQ r
  | 17 => panel17TargetQ r
  | 18 => panel18TargetQ r
  | 19 => panel19TargetQ r
  | 20 => panel20TargetQ r
  | 21 => panel21TargetQ r
  | 22 => panel22TargetQ r
  | 23 => panel23TargetQ r
  | 24 => panel24TargetQ r
  | 25 => panel25TargetQ r
  | 26 => panel26TargetQ r
  | 27 => panel27TargetQ r
  | 28 => panel28TargetQ r
  | 29 => panel29TargetQ r
  | 30 => panel30TargetQ r
  | 31 => generatedBandIntegralQ (p2UpperEntryAt r).val -
      first31PanelTargetSumQ r
  | _ => 0

end RHP2Bridge.P2RoundedPanelTargetData
