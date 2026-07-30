import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel16FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel16FlatComponentChunk46

end RHP2Bridge
