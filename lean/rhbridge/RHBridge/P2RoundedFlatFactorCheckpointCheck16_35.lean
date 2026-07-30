import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel16FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel16FlatComponentChunk35

end RHP2Bridge
