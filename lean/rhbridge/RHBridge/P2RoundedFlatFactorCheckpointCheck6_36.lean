import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel6FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel6FlatComponentChunk36

end RHP2Bridge
