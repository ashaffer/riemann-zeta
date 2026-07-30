import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel6FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel6FlatComponentChunk47

end RHP2Bridge
