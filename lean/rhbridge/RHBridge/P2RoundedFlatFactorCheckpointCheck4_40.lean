import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel4FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel4FlatComponentChunk40

end RHP2Bridge
