import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel3FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel3FlatComponentChunk47

end RHP2Bridge
