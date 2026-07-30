import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel9FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel9FlatComponentChunk40

end RHP2Bridge
