import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel6FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel6FlatComponentChunk25

end RHP2Bridge
