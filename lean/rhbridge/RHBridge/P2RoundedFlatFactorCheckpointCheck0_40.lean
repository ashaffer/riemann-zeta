import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel0FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel0FlatComponentChunk40

end RHP2Bridge
