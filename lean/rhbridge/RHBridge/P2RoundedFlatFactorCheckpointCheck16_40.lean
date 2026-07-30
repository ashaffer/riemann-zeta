import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel16FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel16FlatComponentChunk40

end RHP2Bridge
