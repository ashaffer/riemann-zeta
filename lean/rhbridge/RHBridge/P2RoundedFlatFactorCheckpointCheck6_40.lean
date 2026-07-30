import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel6FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel6FlatComponentChunk40

end RHP2Bridge
