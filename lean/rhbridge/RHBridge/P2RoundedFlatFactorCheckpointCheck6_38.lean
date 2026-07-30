import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel6FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel6FlatComponentChunk38

end RHP2Bridge
