import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel16FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel16FlatComponentChunk26

end RHP2Bridge
