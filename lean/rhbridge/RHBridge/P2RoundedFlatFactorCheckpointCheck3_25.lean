import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel3FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel3FlatComponentChunk25

end RHP2Bridge
