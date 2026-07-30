import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel25FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel25FlatComponentChunk40

end RHP2Bridge
