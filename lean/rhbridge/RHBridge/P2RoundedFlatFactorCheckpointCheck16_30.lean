import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel16FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel16FlatComponentChunk30

end RHP2Bridge
